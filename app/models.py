from . import db
from mylog import time_print
import random


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    url_num = db.Column(db.Integer)
    title = db.Column(db.String(10))
    img = db.Column(db.String(64))
    content = db.Column(db.String())
    timestamp = db.Column(db.String, default=time_print())
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), default='游客')
    img = db.Column(db.String(64))
    content = db.Column(db.String())
    timestamp = db.Column(db.String, default=time_print())
    reply_id = db.Column(db.Integer, default=0)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))


    def __init__(self, content):
        self.content = content
        # self.img = '/static/img/' + str(random.randint(1,3)) + '.jpg'
        self.img = '/static/img/1.jpg'


    def save(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        extra = dict(
            post_id = self.post_id,
        )
        d = {k: v for k, v in self.__dict__.items() if k not in self.blacklist()}
        d.update(extra)
        return d

    def blacklist(self):
        b = [
            '_sa_instance_state',
        ]
        return b

    def get_replys(self):
        replys = Comment.query.filter_by(reply_id=self.id).all()
        for reply in replys:
            yield reply.json()







