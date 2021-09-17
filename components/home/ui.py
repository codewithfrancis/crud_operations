from flask import Blueprint, render_template

index = Blueprint('index',__name__, template_folder='boiletplate')

@index.route('/home')
def Home():
    return render_template('home/home.html')