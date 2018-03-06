from datetime import datetime
from ourlove import db

class MediaType(db.Model):
    __tablename__ = 'MediaType'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<MediaType %r>' % self.title