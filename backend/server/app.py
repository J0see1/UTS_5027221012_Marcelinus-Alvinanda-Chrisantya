from flask import Flask, jsonify, request
from flask_cors import CORS
import sys
sys.path.append('../')  # Assuming the parent directory of 'backend' is two levels up
import grpc
import jobs_pb2
import jobs_pb2_grpc

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# gRPC channel initialization
channel = grpc.insecure_channel('localhost:50051')
stub = jobs_pb2_grpc.JobServiceStub(channel)

@app.route('/jobs', methods=['GET'])
def get_all_jobs():
    # Send gRPC request to get all jobs
    try:    
        response = stub.GetAll(jobs_pb2.Empty())
        job_list = [{'id': job.id, 'title': job.title, 'company': job.company, 'location': job.location, 'salary': job.salary} for job in response.jobs]
        return jsonify({'jobs': job_list})
    except grpc.RpcError as e:
        return jsonify({'error': 'Failed to fetch jobs: {}'.format(e.details())}), 500

@app.route('/jobs', methods=['POST'])
def add_job():
    # Parse request data
    data = request.json
    job = jobs_pb2.Job(
        id=data.get('id'),
        title=data.get('title'),
        company=data.get('company'),
        location=data.get('location'),
        salary=data.get('salary')
    )
    # Send gRPC request to add job
    try:
        response = stub.AddJob(job)
        return jsonify({'message': 'Job added successfully', 'job': {'id': response.id, 'title': response.title, 'company': response.company, 'location': response.location, 'salary': response.salary}})
    except grpc.RpcError as e:
        return jsonify({'error': 'Failed to add job: {}'.format(e.details())}), 500

if __name__ == '__main__':
    app.run(debug=True)
