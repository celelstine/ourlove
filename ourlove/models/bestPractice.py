from datetime import datetime
from ourlove import db
from sqlalchemy.dialects.postgresql import ARRAY

class BestPractice(db.Model):
    __tablename__ = 'BestPractice'

    id = db.Column(db.Integer, primary_key=True)
    mediatype = db.Column(db.Integer, db.ForeignKey('MediaType.id'), nullable=False)
    content = db.Column(db.String(500), nullable=True)
    upvotes =  db.Column(ARRAY(db.Integer, dimensions=1))
    downvotes = db.Column(ARRAY(db.Integer, dimensions=1))
    tags = db.Column(ARRAY(db.String(20), dimensions=1))
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    isEdited = db.Column(db.Boolean, default=False)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<BestPractice %r>' % self.content