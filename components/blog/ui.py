from flask import Blueprint, render_template, redirect, url_for

blog = Blueprint('blog',__name__, template_folder='boilerplate')

@blog.route('/')
def HomeRedirector():
    return redirect(url_for('index.Home'))