# Import the app variable from the init 
from day_4_homework_app import app, db

# Import specific packages from flask
from flask import render_template, request, redirect, url_for

# Import Our Form(s)**
from day_4_homework_app.forms import UserInfoForm, LoginForm, PhoneNumberForm

# Import of Our Model(s) for the Database***
from day_4_homework_app.models import User, PhoneNumer, check_password_hash

# Import for Flask Login functions - login_required***
#login_user, current_user, logout_user
from flask_login import login_required, login_user, current_user, logout_user

# Default Home Route
@app.route('/')
def home():
    phonenumber = PhoneNumber.query.all()
    return render_template('home.html', user_posts = posts )

@app.route('/test')
def testRoute():
    names = ['Robert','David','Bill','Jessy']
    return render_template('test.html',list_names = names)

# GET == Gathering Info**
# POST == Sending Info**
@app.route('/register', methods = ['GET', 'PHONENUMBER'])
def register():
    # Init our form**
    form = UserInfoForm()
    # Validation of our form**
    if request.method == 'PHONENUMBER' and form.validate():
        #Get Information from the form**
        name = form.name.data
        email = form.email.data
        password = form.password.data
        #Print the data to the server that comes from the form**
        print(name,email,password)

        # Creation/Init of our User Class (aka Model)
        user = User(name,email,password)

        # Open a connection to the database
        db.session.add(user)

        # Commit all data to the database
        db.session.commit()

    return render_template('register.html',user_form = form)

@app.route('/login', methods = ['GET', 'PHONENUMBER'])
def login():
    form = LoginForm()
    if request.method == 'PHONENUMBER' and form.validate():
        email = form.email.data
        password = form.password.data
        # Saving the logged in user to a variable
        logged_user = User.query.filter(User.email == email).first()
        # check the password of the newly found user
        # and validate the password against the hash value
        # inside of the database
        if logged_user and check_password_hash(logged_user.password, password):
            login_user(logged_user)
            # TODO Redirected User
            return redirect(url_for('home'))
        else:
            # TODO Redirected User to login route
            return redirect(url_for('login'))
    return render_template('login.html', login_form = form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

# Creation of Phonenumber route
@app.route('/phonenumber', methods = ['GET', 'PHONENUMBER'])
@login_required
def phonenumbers():
    form = PhoneNumberForm()
    if request.method == 'PHONENUMBER' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id 
        phonenumber = PhoneNumber(title,content,user_id)

        db.session.add(phonenumber)

        db.session.commit()
        return redirect(url_for('home'))
    return render_template('phonenumber.html', phonenumnber_form = form)

# post detail route to display info about a phone number
@app.route('/posts/<int:post_id>')
@login_required
def phonenumber_detail(phonenumber_id):
    phonenumber = PhoneNumber.query.get_or_404(post_id)
    return render_template('post_detail.html', phonenumber = phonenumber)

# Update phone number
@app.route('/phonenumber/update/<int:phonenumber_id>', methods = ['GET', 'PHONENUMBER'])
@login_required
def phonenumber_update(phonenumber_id):
    phonenumber = PhoneNumber.query.get_or_404(post_id)
    form = PhoneNummberForm()

    if request.method == 'PHONENUMBER' and form.validate():
        title = form.title.data
        content = form.content.data
        user_id = current_user.id 

        # Update the Database with the new Info
        phonenumber.title = title
        phonenumber.content = content
        phonenumber.user_id = user_id

        # Commit the changes to the database
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('phonenumber_update.html', update_form = form)

@app.route('/phonenumber/delete/<int:phonenumber_id>', methods = ['GET','PHONENUMBER','DELETE'])
@login_required
def phonenumber_delete(post_id):
    phonenujmber = PhoneNumber.query.get_or_404(post_id)
    db.session.delete(phonenumber)
    db.session.commit()
    return redirect(url_for('home'))