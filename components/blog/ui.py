from flask import Blueprint, render_template, redirect

blog = Blueprint('blog',__name__, template_folder='boiletplate')

@blog.route('/home')
def HomeRedirector():
    return redirect('index.Home')