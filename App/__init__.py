from flask import Flask

from App.apis import init_api
from App.ext import init_ext
from App.settings import envs
from App.views import init_blueprint


def create_app():
    app = Flask(__name__)
    # 初始化 Flask  config
    app.config.from_object(envs.get("develop"))
    # 初始化 扩展库
    init_ext(app)

    # 初始化蓝图
    init_blueprint(app)
    # 注册 rest api
    init_api(app)

    return app
