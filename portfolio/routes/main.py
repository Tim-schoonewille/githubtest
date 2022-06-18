from flask import Blueprint
from ..extensions import db
from ..models import *


main = Blueprint('main', __name__, url_prefix='/')


@main.route('/')
def main_index():
    return 'Main index'


@main.route('/add-user/<name>')
def create_user(name):

    user = User(name=name)

    db.session.add(user)
    db.session.commit()

    return f'Added user: {name}'


@main.route('/add-portfolio-item/<name>')
def add_portfolio_item(name):

    get_user = User.query.filter_by(name=name).first()

    new_item = PortfolioItem(name='My first portfolio item', body='My first body.', user_id=get_user.id)

    db.session.add(new_item)
    db.session.commit()

    return 'Added portfolio item!'


@main.route('/get-portfolio/<name>')
def get_portfolio_items(name):

    get_user = User.query.filter_by(name=name).first()

    for item in get_user.portfolio_items:
        print(item)

    return 'see console'
