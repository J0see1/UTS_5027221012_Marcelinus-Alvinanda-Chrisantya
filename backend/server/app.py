from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import sys
sys.path.append('../')
import grpc
import jobs_pb2
import jobs_pb2_grpc
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# gRPC client setup
grpc_channel = grpc.insecure_channel('localhost:5000') 
grpc_stub = jobs_pb2_grpc.JobServiceStub(grpc_channel)

# Set the html template folder
template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../frontend/src/'))
app.template_folder = template_dir

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/addJob", methods=['GET', 'POST'])
def add_job():
    if request.method == 'GET':
        return render_template("addJob.html")
    elif request.method == 'POST':
        data = request.json
        job_request = jobs_pb2.Job(
            id=data['id'],
            title=data['title'],
            company=data['company'],
            location=data['location'],
            salary=data['salary']
        )
        response = grpc_stub.AddJob(job_request)
        return jsonify({"message": "Job added successfully"})

@app.route("/allJob")
def get_all_jobs():
    response = grpc_stub.GetAll(jobs_pb2.Empty())
    job_list = [{"id": job.id, "title": job.title, "company": job.company, "location": job.location, "salary": job.salary} for job in response.jobs]
    return jsonify({"jobs": job_list})

@app.route("/job/<job_title>")
def get_job(job_title):
    response = grpc_stub.GetJob(jobs_pb2.JobTitle(title=job_title))
    if response.id:
        job_data = {"id": response.id, "title": response.title, "company": response.company, "location": response.location, "salary": response.salary}
        return jsonify(job_data)
    else:
        return jsonify({"message": "Job not found"}), 404
    
@app.route("/updateJob/<job_id>", methods=['PUT'])
def update_job(job_id):
    data = request.json
    job_request = jobs_pb2.Job(
        id=job_id,
        title=data.get('title', ''),
        company=data.get('company', ''),
        location=data.get('location', ''),
        salary=data.get('salary', 0)
    )
    response = grpc_stub.UpdateJob(job_request)
    if response.id:
        return jsonify({"message": "Job updated successfully"})
    else:
        return jsonify({"message": "Job not found"}), 404

@app.route("/deleteJob/<job_id>", methods=['DELETE'])
def delete_job(job_id):
    grpc_stub.DeleteJob(jobs_pb2.JobId(id=job_id))
    return jsonify({"message": "Job deleted successfully"})

if __name__ == '__main__':
    app.run(debug=True)