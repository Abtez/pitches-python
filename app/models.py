from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(255),unique=True,index=True)
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure  = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    my_pitch = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    pitches = db.relationship('Pitch',backref='pitches', lazy='dynamic')
    upvote = db.relationship('Upvote',backref='upvotes',lazy='dynamic')
    downvote = db.relationship('Downvote',backref='downvotes',lazy='dynamic')
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
        
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def save_user(self):
        db.session.add(self)
        db.session.commit()
        
    def __repr__(self):
        return f'User{self.username}'
    
class Pitch(db.Model):
    __tablename__ = 'pitches'
    id = db.Column(db.Integer, primary_key = True)
    pitch = db.Column(db.Text())
    category = db.Column(db.String(255), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.filter_by(user_id=id).all()
        return pitches

class Comment(db.Model):
    __tablename__ = 'comments' 
    id = db.Column(db.Integer, primary_key = True)
    comments = db.Column(db.Text())
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_comments(cls,pitch_id):
        comments = Comment.query.filter_by(pitch_id=pitch_id).all()

        return comments
        
    def __repr__(self):
        return f'Comment{self.comments}'
    
class Upvote(db.Model):
    __tablename__ = 'upvotes' 
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_upvote(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_upvotes(cls,id):
        upvotes = Upvote.query.filter_by(pitch_id=id).all()

        return upvotes
        
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
class Downvote(db.Model):
    __tablename__ = 'downvotes' 
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    
    def save_downvote(self):
        db.session.add(self)
        db.session.commit()
        
    @classmethod
    def get_downvotes(cls,id):
        downvotes = Downvote.query.filter_by(pitch_id=id).all()

        return downvotes
        
    def __repr__(self):
        return f'{self.user_id}:{self.pitch_id}'
    
       
    
    
