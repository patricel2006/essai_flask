from flask import Flask, render_template

from mocks import Post

from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


#class Post(db.Model):

    #id = db.Column(db.Integer, primary_key=True)
    #title = db.Column(db.String(255))
    #content = db.Column(db.Text)


@app.context_processor
def inject_now():
    return dict(now=datetime.now())


@app.context_processor
def utility_processor():
    def pluralize(count, singular, plural=None):
        if not isinstance(count, int):
            raise ValueError('"{}" must be an integer'.format(count))

        if plural is None:
            plural = singular + 's'

        if count == 1:
            string = singular
        else:
            string = plural

        return "{} {}".format(count, string)

    return dict(pluralize=pluralize)


@app.route('/')
def home():
    return render_template('pages/home.html')


@app.route('/about')
def about():
    return render_template('pages/about.html')


@app.route('/contact')
def contact():
    return render_template('pages/contact.html')


@app.route('/blog')
def posts_index():
    posts = Post.all()
    return render_template('posts/index.html', posts=posts)


@app.route('/blog/posts/<int:id>')
def posts_show(id):
    post = Post.find(id)
    return render_template('posts/show.html', post=post)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html'), 404


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=3000)
