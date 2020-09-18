from flask import render_template
from . import main

@main.app_errorhandler(404)
def fo_o_fo(error):
    return render_template('fo_o_fo.html'),404