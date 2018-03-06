from datetime import datetime
from ourlove import db

class AuthToken(db.Model):
    __tablename__ = 'AuthToken'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(80), unique=True, nullable=False)
    token_hash = db.Column(db.String(328))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    expires = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='active')
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<authToken %r>' % self.token