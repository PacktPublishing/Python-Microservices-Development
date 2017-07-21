import subprocess
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

def read_file(filename):
	with open(filename) as f:
		data = yaml.load(f.read())

def run_command(cmd):
	return subprocess.check_call(cmd, shell=True)

db = create_engine('sqlite:///somedatabase')
Session = sessionmaker(bind=db)

def get_user(uid):
	session = Session()
	query = "select * from user where id='%s'" % uid
	return session.execute(query)