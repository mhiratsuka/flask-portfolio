from flask import render_template, url_for, flash, redirect
from myportfolio import app
from myportfolio.forms import RegistrationForm, LoginForm
from myportfolio.models import User, Post

posts = [
    {
        'workTitle': 'Work1',
        'skill': 'work1 work1'
    },
    {
        'workTitle': 'Work2',
        'skill': 'work2 work2'
    },
    {
        'workTitle': 'Work3',
        'skill': 'work3 work3'
    }
]
 
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/work')
def work():
    return render_template('work.html', title='Work', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
             flash('You have been logged in!', 'success')
             return redirect(url_for('home'))
        else: 
            flash('Login unseccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)