from flask import Flask
from flask import url_for #Used for testing
from flask import request #used to manage http requests
from flask import render_template #used to render html templates
from markupsafe import Markup #not used yet
from markupsafe import escape

app = Flask(__name__)
app.run(debug=True) #debug mode

def setup():
    url_for('static', filename='style.css')

app.before_first_request(setup) # calls function before first request

@app.route('/')
@app.route('/index')
def index():
    items = [{"href": "http://127.0.0.1:5000/login", "caption":"login"}]
    return render_template('index.html', navigation = items)

@app.route("/<name>")
def name(name):
    return f"Hello, {escape(name)}!"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

def valid_login(username, password):
    return True

def log_the_user_in(username):
    return f'Logged in as {username}!'

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('badlogin.html', error=error)

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

with app.test_request_context():
    #print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

with app.test_request_context('/hello', method='POST'): 
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'
"""
The other possibility is passing a whole WSGI environment to the request_context() method:

with app.request_context(environ):
    assert request.method == 'POST'
"""
