from core import app, db

@app.route('/')
def index():
    return "<h1>Hello World</h1>"