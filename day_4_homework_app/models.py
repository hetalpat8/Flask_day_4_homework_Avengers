from day_4_homework_app import app, db, login_manager

# Import all of the Werkzeug Security Methods
from werkzeug.security import generate_password_hash, check_password_hash

# import for DateTime Module(This comes from Python)
from datetime import datetime

# Import for the Login Manager UserMixin***
from flask_login import UserMixin

# The User class will have 
# An id, username, email
# password, post

#create the current user_manager using the user_loader function***
#Which is a decorator(used in thid class to send info to the user model)***
#specifically the User's ID***

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(150), nullable = False, unique = True)
    email = db.Column(db.String(150), nullable = False, unique = True)
    password = db.Column(db.String(256), nullable = False)
    post = db.relationship('PhoneNumber', backref = 'author', lazy = True)

    def __init__(self,username,email,password):
        self.name = name
        self.email = email
        self.password = self.set_password(password)

    def set_password(self,password):
        """
                Grab the password that is passed into the method
                return the hashed version of the password
                which will be stored inside the database
        """
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def __repr__(self):
        return f'{self.name} has been created with the following email: {self.email}'


# Creation of the Post Model
# The Post Model will have an
# id, title, content, date_created
# user_id
class PhoneNumer(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

# CREATE TABLE post(
    # id SERIAL PRIMARY KEY,
    # title VARCHAR(100),
    # content VARCHAR(300),
    #date_created DATE DEFAULT CURRENT_DATE,
    #user_id INTEGER NOT NULL,
    #FOREIGN KEY(user_id) REFERENCES user(user_id)
    #);
    #This is what the above looks like in SQL Postgres


    def __init__(self,title,content,user_id):
        self.title = title
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return f'The title of the phonenumber is {self.title} \n and the content is {self.content}'
    
