# import the os module
import os 

# creation of base directory for applicatiion
basedir = os.path.abspath(os.path.dirname(__file__))

# Mac = documents/chicodes_sept2020/week_5/day_3_homework--this is what the line above says


# Config Class**
# Configure the database (when we have one) AND configure the 
# secret key for the encryption of our submitted forms
class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess this....'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False