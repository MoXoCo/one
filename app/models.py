from . import db
from datetime import datetime


class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    url_num = db.Column(db.Integer)
    title = db.Column(db.String(10))
    img = db.Column(db.String(64))
    content = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def save(self):
        db.session.add(self)
        db.session.commit()


class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), default='游客')
    img = db.Column(db.String(64), default='http://placekitten.com/80/80')
    content = db.Column(db.String())
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    reply_id = db.Column(db.Integer, default=0)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))


    def __init__(self, content):
        self.content = content


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







