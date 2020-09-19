from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm
from .. import db

@main.route('/',methods=['GET','POST'])
def index():
    form = ReviewForm()
    return render_template('index.html', review_form=form)
