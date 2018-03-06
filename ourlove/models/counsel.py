from datetime import datetime
from ourlove import db
from sqlalchemy.dialects.postgresql import ARRAY

class Counsel(db.Model):
    __tablename__ = 'Counsel'

    id = db.Column(db.Integer, primary_key=True)
    situation_id = db.Column(db.Integer, db.ForeignKey('Situation.id'), nullable=False)
    upvotes = db.Column(ARRAY(db.Integer, dimensions=1))
    downvotes = db.Column(ARRAY(db.Integer, dimensions=1))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    content = db.Column(db.String(500), nullable=True)
    isEdited = db.Column(db.Boolean, default=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Counsel %r>' % self.content