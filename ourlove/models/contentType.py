from datetime import datetime
from ourlove import db

class ContentType(db.Model):
    __tablename__ = 'ContentType'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<ContentType %r>' % self.title