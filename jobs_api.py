from flask import jsonify
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
