import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session
import sqlalchemy.ext.declarative as dec
from mars.data import db_session
from mars.data.jobs import Jobs
from mars.data.users import User
import datetime
SqlAlchemyBase = dec.declarative_base()

__factory = None

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
