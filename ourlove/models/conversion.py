from datetime import datetime
from ourlove import db

class Conversion(db.Model):
    __tablename__ = 'Conversion'

    id = db.Column(db.Integer, primary_key=True)
    sender = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    text = db.Column(db.String(200), nullable=False)
    isEdited = db.Column(db.Boolean, default=False)
    status = db.Column(db.String(20), default='sent')
    situation_id = db.Column(db.Integer, db.ForeignKey('Situation.id'), nullable=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Conversion %r>' % self.text