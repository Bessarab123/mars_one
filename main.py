import sqlalchemy as sa
import sqlalchemy.orm as orm
from flask import app, Flask, make_response, jsonify
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
from data import db_session
from data.jobs import Jobs
from data.users import User
import datetime
import jobs_api
from requests import get
from flask_restful import Api
from api.users_resource import UserResource, UsersListResource

SqlAlchemyBase = dec.declarative_base()

app = Flask(__name__)
api = Api(app)
api.add_resource(UsersListResource, '/api/v2/users')
api.add_resource(UserResource, '/api/v2/user/<int:user_id>')
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
__factory = None


def main():
    db_session.global_init("mars_explorer.sqlite")
    app.register_blueprint(jobs_api.blueprint)
    app.run()


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def older_main():
    db_session.global_init("mars_explorer.sqlite")
    session = db_session.create_session()
    user = User()
    user.surname = "Scott"
    user.name = 'Ridley'
    user.age = 21
    user.position = 'captain'
    user.address = 'module_1'
    user.email = 'scott_chief@mars.org'
    session.add(user)
    user = User()
    user.surname = "Scott"
    user.name = 'Mark'
    user.age = 21
    user.position = 'captain_helper'
    user.address = 'module_2'
    user.email = 'scott_mark@mars.org'
    session.add(user)
    user = User()
    user.surname = "DOCTOR"
    user.name = 'WHO'
    user.age = 1821
    user.position = 'solder'
    user.address = 'TARDIS'
    user.email = 'TARDIS@mars.org'
    session.add(user)
    user = User()
    user.surname = "MASK"
    user.name = 'ILON'
    user.age = 31
    user.position = 'sponser'
    user.address = 'Earth'
    user.email = 'MARS_ONE@mars.org'
    session.add(user)
    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 3'
    job.start_date = datetime.datetime.now()
    job.is_finished = False
    session.add(job)
    session.commit()


if __name__ == '__main__':
    main()
