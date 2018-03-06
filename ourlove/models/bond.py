from datetime import datetime
from ourlove import db

class Bond(db.Model):
    __tablename__ = 'Bond'

    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    user2_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    isActive = db.Column(db.Boolean, default=True)
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Chronicle %r>' % self.content