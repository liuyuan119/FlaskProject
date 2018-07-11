from flask import Blueprint

order = Blueprint('order', __name__)


@order.route("/orders/")
def orders():

    return "Hello Order"