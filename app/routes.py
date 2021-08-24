from app import app
from flask import request, Response
import json

members = 0
projects = 0
events = 0


@app.post('/members')
def save_number_of_members():
    global members
    if request.args.get('count') != "" and request.args.get('count') is not None:
        members = request.args.get('count')
        return Response(status=200)
    else:
        message = json.dumps({"message": "fill in the parameter"})
        return Response(message, status=400, mimetype='application/json')


@app.post('/projects')
def save_number_of_projects():
    global projects
    if request.args.get('count') != "" and request.args.get('count') is not None:
        projects = request.args.get('count')
        return Response(status=200)
    else:
        message = json.dumps({"message": "fill in the parameter"})
        return Response(message, status=400, mimetype='application/json')


@app.post('/events')
def save_number_of_events():
    global events
    if request.args.get('count') != "" and request.args.get('count') is not None:
        events = request.args.get('count')
        return Response(status=200)
    else:
        message = json.dumps({"message": "fill in the parameter"})
        return Response(message, status=400, mimetype='application/json')


@app.get('/members')
def get_number_of_members():
    global members
    return {"message": f"number of members is {members}"}


@app.get('/projects')
def get_number_of_projects():
    global projects
    return {"message": f"number of projects is {projects}"}


@app.get('/events')
def get_number_of_events():
    global events
    return {"message": f"number of events is {events}"}

