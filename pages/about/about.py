from flask import Blueprint
from flask import render_template, redirect, url_for


# homepage blueprint definition
about = Blueprint(
    'about',
    __name__,
    static_folder='static',
    static_url_path='/about',
    template_folder='templates'
)


# Routes
@about.route('/About')
def index():
    return render_template('about.html')

