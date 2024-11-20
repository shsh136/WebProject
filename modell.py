from multiprocessing.managers import Array

from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

def init_app(app):
    db.init_app(app)

class Song(db.Model):
    __tablename__ = 'songs_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False)

    __table_args__ = (
        db.CheckConstraint('duration > 0', name='check_duration_positive'),
        db.CheckConstraint('upload_time >= now()', name='check_upload_time_future'),
    )


class Podcast(db.Model):
    table_name = 'podcast_table'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    upload_time = db.Column(db.DateTime, nullable=False)
    host = db.Column(db.String(100), nullable=False)
    participants = db.Column(db.ARRAY(db.String), nullable=True)  # PostgreSQL-specific

    __table_args__ = (
        db.CheckConstraint('duration > 0', name='check_duration_positive'),
        db.CheckConstraint('upload_time >= now()', name='check_upload_time_future'),
    )






