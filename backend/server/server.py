import grpc
import sys
sys.path.append('../') 
import pymongo
from concurrent import futures
import jobs_pb2
import jobs_pb2_grpc
import logging

class JobService(jobs_pb2_grpc.JobServiceServicer):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/") 
        self.db = self.client["JobVacancy"]  
        self.collection = self.db["JobList"]  
        logging.info("Connected to MongoDB")  

    def AddJob(self, request, context):
        logging.info("Received AddJob request: %s", request)
        job_data = {
            "id": request.id,
            "title": request.title,
            "company": request.company,
            "location": request.location,
            "salary": request.salary
        }
        self.collection.insert_one(job_data) 
        return request

    def GetAll(self, request, context):
        logging.info("Received GetAll request")
        job_list = []
        for job_data in self.collection.find():
            job = jobs_pb2.Job(
                id=job_data["id"],
                title=job_data["title"],
                company=job_data["company"],
                location=job_data["location"],
                salary=job_data["salary"]
            )
            job_list.append(job)
        return jobs_pb2.JobList(jobs=job_list)
    
    def GetJob(self, request, context):
        logging.info("Received GetJob request for job title: %s", request.title)
        job_data = self.collection.find_one({"title": request.title})
        if job_data:
            job = jobs_pb2.Job(
                id=job_data["id"],
                title=job_data["title"],
                company=job_data["company"],
                location=job_data["location"],
                salary=job_data["salary"]
            )
            return job
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Job not found")
            return jobs_pb2.Job()
        
    def UpdateJob(self, request, context):
        logging.info("Received UpdateJob request for job ID: %s", request.id)
        job_data = self.collection.find_one({"id": request.id})
        if job_data:
            update_data = {}
            if request.title:
                update_data["title"] = request.title
            if request.company:
                update_data["company"] = request.company
            if request.location:
                update_data["location"] = request.location
            if request.salary:
                update_data["salary"] = request.salary

            self.collection.update_one({"id": request.id}, {"$set": update_data})
            return jobs_pb2.Job(id=request.id, title=request.title, company=request.company, location=request.location, salary=request.salary)
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Job not found")
            return jobs_pb2.Job()

    def DeleteJob(self, request, context):
        logging.info("Received DeleteJob request for job ID: %s", request.id)
        result = self.collection.delete_one({"id": request.id})
        if result.deleted_count > 0:
            return jobs_pb2.Empty()
        else:
            context.set_code(grpc.StatusCode.NOT_FOUND)
            context.set_details("Job not found")
            return jobs_pb2.Empty()

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jobs_pb2_grpc.add_JobServiceServicer_to_server(JobService(), server)
    server.add_insecure_port('[::]:5000')
    server.start()
    logging.info("Server started. Listening on port 5000...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
