from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'muchui'} #fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    return render_template('index.html',
                          title='home',
                          user=user)
    #return '''
#<html>
#<head>
#<body>
#<h1> Hello, ''' + user['nickname'] +'''</h1>
#</body>
#</html>
#'''