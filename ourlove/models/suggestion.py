from datetime import datetime
from ourlove import db

class Suggestion(db.Model):
    __tablename__ = 'Suggestion'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    header = db.Column(db.String(70), nullable=False)
    content = db.Column(db.String(400), nullable=False)
    isEdited = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='sent')
    response = db.Column(db.String(200), nullable=True)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Suggestion %r>' % self.header