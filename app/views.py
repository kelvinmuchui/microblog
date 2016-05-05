from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'muchui'}
    return '''
<html>
<head>
<body>
<h1> Hello, ''' + user['nickname'] +'''</h1>
</body>
</html>
'''