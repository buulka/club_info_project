from app import app
from flask import request

members = 0
projects = 0
events = 0


@app.post('/members')
def save_number_of_members():
    global members
    if request.args.get('count') != "" and request.args.get('count') is not None:
        members = request.args.get('count')
        return {"message": f"number of members saved: {members}"}
    else:
        return {"message": "fill in the parameter"}


@app.post('/projects')
def save_number_of_projects():
    global projects
    if request.args.get('count') != "" and request.args.get('count') is not None:
        projects = request.args.get('count')
        return {"message": f"number of members saved: {projects}"}
    else:
        return {"message": "fill in the parameter"}


@app.post('/events')
def save_number_of_events():
    global events
    if request.args.get('count') != "" and request.args.get('count') is not None:
        events = request.args.get('count')
        return {"message": f"number of members saved: {events}"}
    else:
        return {"message": "fill in the parameter"}


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

