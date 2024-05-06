import grpc
import sys
sys.path.append('../')  # Assuming the parent directory of 'backend' is two levels up
import jobs_pb2
import jobs_pb2_grpc

def create_job(stub):
    job_id = input("Enter job ID: ")
    title = input("Enter job title: ")
    company = input("Enter company name: ")
    location = input("Enter job location: ")
    salary = int(input("Enter job salary: "))

    job = jobs_pb2.Job(id=job_id, title=title, company=company, location=location, salary=salary)
    response = stub.AddJob(job)
    print("AddJob Response:", response)

def get_all_jobs(stub):
    all_jobs = stub.GetAll(jobs_pb2.Empty())
    print("GetAll Response:", all_jobs)

def get_job(stub):
    job_id = input("Enter job ID: ")
    job = stub.GetJob(jobs_pb2.JobId(id=job_id))
    print("GetJob Response:", job)

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = jobs_pb2_grpc.JobServiceStub(channel)

    while True:
        print("\n1. Add Job\n2. Get All Jobs\n3. Get Job\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_job(stub)
        elif choice == '2':
            get_all_jobs(stub)
        elif choice == '3':
            get_job(stub)
        elif choice == '4':
            break
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == '__main__':
    run()
