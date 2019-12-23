from flask import Flask, render_template, redirect, url_for,request
from Class import BlogPost

app = Flask(__name__)

@app.route('/')
def index():
    allPosts = BlogPost().getAllPosts()
    return render_template('index.html', posts=allPosts)

@app.route('/post/<id>')
def post(id):
    allPosts = BlogPost().getPost(id)
    return str(allPosts)

@app.route('/remove/<id>')
def remove(id):
    BlogPost().togglePost(id, 0)
    return redirect(url_for('index'))

@app.route('/activate/<id>')
def activate(id):
    BlogPost().togglePost(id, 1)
    return redirect(url_for('index'))

@app.route('/createPost/', methods=['POST', 'GET'])
def createPost():
    if request.method == 'POST':
        title = request.form['title']
        text = request.form['text']
        BlogPost().createPost(title, text)
        return redirect(url_for('index'))
    return render_template('createPost.html')

app.run(host= '0.0.0.0')