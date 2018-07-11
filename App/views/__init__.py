
# 懒加载， 后初始化的方式
from App.views.OrderView import order
from App.views.UserView import blue


def init_blueprint(app):
    app.register_blueprint(blueprint=blue)
    app.register_blueprint(blueprint=order)





