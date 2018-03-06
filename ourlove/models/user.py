from datetime import datetime
from ourlove import db
from sqlalchemy.dialects.postgresql import ARRAY

class User(db.Model):
    __tablename__ = 'User'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password_hash = db.Column(db.String(328))
    password = db.Column(db.String(128))
    crimecount = db.Column(db.Integer, default=0)
    tags = db.Column(ARRAY(db.String(20), dimensions=1))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    situations = db.relationship('Situation', lazy='select',
                                backref=db.backref('user', lazy='joined'))
    counsels = db.relationship('Counsel', lazy='select',
                                 backref=db.backref('user', lazy='joined'))
    suggestions = db.relationship('Suggestion', lazy='select',
                               backref=db.backref('user', lazy='joined'))

    def __repr__(self):
        return '<User %r>' % self.username