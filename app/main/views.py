from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm
from .. import db

@main.route('/',methods=['GET','POST'])
def index():
    form = ReviewForm()
    if form.validate_on_submit():
        category = form.category.data
        pitch = form.pitch.data
        return redirect(url_for('main.new_pitch'))
    return render_template('index.html', review_form=form)

@main.route('/pitches/new_pitch', methods=['GET','POST'])
def new_pitch():
    return render_template('new_pitch.html')
