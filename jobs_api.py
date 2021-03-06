from flask import jsonify, request
from data import db_session
from data.jobs import Jobs
import flask

blueprint = flask.Blueprint('jobs_api', __name__,
                            template_folder='templates')


@blueprint.route('/api/jobs', methods=['GET'])
def get_jobs():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return jsonify(
        {
            'jobs':
                [item.to_dict()
                 for item in jobs]
        }
    )


@blueprint.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_one_jobs(job_id):
    session = db_session.create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify({'jobs': job.to_dict()})


@blueprint.route('/api/jobs', methods=['POST'])
def create_job():
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in
                 ['id', 'job', 'work_size', 'collaborators', 'start_date', 'end_date', 'is_finished', 'team_leader']):
        return jsonify({'error': 'Bad request'})
    session = db_session.create_session()
    if get_one_jobs(request.json['id']) != {'error': 'Not found'}:
        return jsonify({'error': 'Id already exists'})
    job = Jobs(
        id=request.json['id'],
        job=request.json['job'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        start_date=request.json['start_date'],
        end_date=request.json['end_date'],
        is_finished=request.json['is_finished'],
        team_leader=request.json['team_leader']
    )
    session.add(job)
    session.commit()
    return jsonify({'success': 'OK'})
