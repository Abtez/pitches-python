from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm
from .. import db

@main.route('/')
def index():
    form = ReviewForm()
    return render_template('index.html', location=str)
