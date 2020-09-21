from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm, CommentForm, BioForm
from .. import db,photos
from flask_login import login_required,current_user
from ..models import User,Pitch, Comment,Upvote,Downvote

@main.route('/')
def index():
   
    return render_template('index.html')

@main.route('/new_pitch', methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = form.my_pitches.data
        category = form.my_category.data
        user_id = current_user     
        new_pitch=Pitch(pitch=pitch,category=category,user_id=current_user._get_current_object().id)
        
        new_pitch.save_pitch()
        return redirect(url_for('.index'))
        
    return render_template('new_pitch.html', review_form=form)

@main.route('/pitches/marketing_pitches')
def marketing_pitches():
    pich = Pitch.query.all()
    marketing = Pitch.query.filter_by(category='Marketing').all()
    return render_template('marketing.html',marketing=marketing)

@main.route('/pitches/promotional_pitches')
def promotion_pitches():
    pich = Pitch.query.all()
    promotional = Pitch.query.filter_by(category='Promotional').all()
    return render_template('promotion.html',promotional=promotional)

@main.route('/pitches/scholarship_pitches')
def scholar_pitches():
    pich = Pitch.query.all()
    scholarship = Pitch.query.filter_by(category='Scholarship').all()
    return render_template('scholar.html',scholarship=scholarship)

@main.route('/pitches/comments/<uname>/<int:pitch_id>', methods=['GET','POST'])
@login_required
def leave_comment(pitch_id,uname):
    user = User.query.filter_by(username = uname).first()
    comment_form = CommentForm()
    pitches = Pitch.query.get(pitch_id)
    comment = Comment.query.filter_by(pitch_id=pitch_id).all()
    if comment_form.validate_on_submit():
        comments = comment_form.comment.data
        
        pitch_id= pitch_id
        user_id = current_user._get_current_object().id
        new_comment= Comment(comments=comments,pitch_id=pitch_id, user_id=user_id)
        new_comment.save_comment()      
        
        return redirect(url_for('.index',comment_form=comment_form,pitch_id=pitch_id,user=user))
        
    return render_template('new_comment.html',comment_form=comment_form, comment=comment,pitch_id=pitch_id,user=user)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/pitches',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    
    if user is None:
        abort(404)

    form = PitchForm()

    if form.validate_on_submit():
        user.my_pitch = form.my_pitches.data
        category = form.my_category.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username,category=category))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/bio',methods = ['GET','POST'])
@login_required
def update_bio(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    bioform = BioForm()

    if bioform.validate_on_submit():
        user.bio = bioform.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/bio.html',bioform=bioform)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))

@main.route('/pitches')
def pitch_page():    
    user = User.query.all()
    pitches = Pitch.query.all()
    user=current_user
    return render_template('pitches.html',pitches=pitches,user=user)
    
