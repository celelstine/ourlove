from datetime import datetime
from ourlove import db
from sqlalchemy.dialects.postgresql import ARRAY

class Situation(db.Model):
    __tablename__ = 'Situation'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(2000), nullable=False)
    tags = db.Column(ARRAY(db.String(20), dimensions=1))
    status = db.Column(db.String(20), default='posted')
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    isEdited = db.Column(db.Boolean, default=False)
    testimony = db.Column(db.String(1000), nullable= True)
    counsels = db.relationship('Counsel', lazy='select',
                                 backref=db.backref('situation', lazy='joined'))
    conversions = db.relationship('Comment', lazy='select',
                                 backref=db.backref('conversions', lazy='joined'))
    dateCreated = db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self):
        return '<Situation %r>' % self.description