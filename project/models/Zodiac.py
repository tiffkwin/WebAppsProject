from .. import db

class Zodiac(db.Model):
    __tablename__ = 'zodiac'

    zodiac_name = db.Column(db.String(25), primary_key=True, nullable=False)
    dates = db.Column(db.String(25), unique=True, nullable=False)
    strengths = db.Column(db.String(100), unique=False, nullable=False)
    weaknesses = db.Column(db.String(100), unique=False, nullable=False)
    likes = db.Column(db.String(100), unique=False, nullable=False)
    dislikes = db.Column(db.String(100), unique=False, nullable=False)
    description = db.Column(db.String(1500), unique=False, nullable=False)


