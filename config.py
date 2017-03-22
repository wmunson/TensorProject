class Config:
	# PUT IN YOUR DATABSE BELOW
	# SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/YOURDATABASE.db'
	# SQLALCHEMY_TRACK_MODIFICATIONS = False
	pass


class DevConfig(Config):
	DEBUG = True


class ProdConfig(Config):
	DEBUG = False
	ALLOWED_HOSTS = ["*"]