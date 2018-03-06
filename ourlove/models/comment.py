from datetime import datetime
from ourlove import db

class Comment(db.Model):
    __tablename__ = 'Comment'

    id = db.Column(db.Integer, primary_key=True)
    content_type = db.Column(db.Integer, db.ForeignKey('ContentType.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    ref = db.Column(db.Integer, default=0)
    isEdited = db.Column(db.Boolean, default=False)
    content_id = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('Comment.id'))
    childrenComment = db.relationship('Comment', remote_side='Comment.id',
                                     backref=db.backref('childrenComment'))
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Comment %r>' % self.text