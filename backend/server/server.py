import grpc
import sys
sys.path.append('../')  # Assuming the parent directory of 'backend' is two levels up
import logging
import pymongo
from concurrent import futures
import jobs_pb2
import jobs_pb2_grpc

class JobService(jobs_pb2_grpc.JobServiceServicer):
    def __init__(self):
        self.client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
        self.db = self.client["JobVacancy"]  # Specify the database name
        self.collection = self.db["JobList"]  # Specify the collection name
        logging.info("Connected to MongoDB")  # Log when connected to MongoDB

    def AddJob(self, request, context):
        logging.info("Received AddJob request: %s", request)
        job_data = {
            "id": request.id,
            "title": request.title,
            "company": request.company,
            "location": request.location,
            "salary": request.salary
        }
        self.collection.insert_one(job_data)  # Insert job data into MongoDB
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
        logging.info("Received GetJob request for job ID: %s", request.id)
        job_data = self.collection.find_one({"id": request.id})
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

    # Implement other methods (GetJob, UpdateJob, DeleteJob) similarly

def serve():
    logging.basicConfig(level=logging.INFO)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jobs_pb2_grpc.add_JobServiceServicer_to_server(JobService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()