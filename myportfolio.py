from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '82e4e6312839d16f95075c7228437e50'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    worktitle = db.Column(db.String(100), nullable=False)
    skill = db.Column(db.String(120), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.worktitle}', '{self.skill}', '{self.date_posted}')"

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

# def main():
#     app.debug = True
#     app.run()
 
if __name__ == '__main__':
    app.run(debug = True)