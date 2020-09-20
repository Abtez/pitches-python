from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm, CommentForm
from .. import db
from flask_login import login_required
from ..models import User,Pitch, Comment,Upvote,Downvote

@main.route('/')
def index():
   
    return render_template('index.html')

@main.route('/pitches/new_pitch', methods=['GET','POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
    return render_template('new_pitch.html', review_form=form)

@main.route('/pitches/marketing_pitches')
def marketing_pitches():
    return render_template('marketing.html')

@main.route('/pitches/promotional_pitches')
def promotion_pitches():
    return render_template('promotion.html')

@main.route('/pitches/scholarship_pitches')
def scholar_pitches():
    return render_template('scholar.html')

@main.route('/pitches/comments', methods=['GET','POST'])
@login_required
def leave_comment():
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment = comment_form.comment.data
    return render_template('new_comment.html', comment_form=comment_form)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
        
    form = PitchForm()

    if form.validate_on_submit():
        user.pitches = form.pitches.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))


    return render_template("profile/profile.html", user = user)
    


    
