import importlib
import inspect
import logging
from logging.handlers import RotatingFileHandler

import flask
from flask import Flask

from config import configDict
from util.my_class import get_modules


def logger_init(file_name='notice.log', file_path='/usr/local/services/app-log/',
                level=logging.INFO,
                max_bytes=100 * 1024 * 1024, backup_count=5):
    """
    定义一个RotatingFileHandler，最多备份5个日志文件，每个日志文件最大100M
    """

    slash = '/' if file_path[:-1] == '/' else ''
    f = file_path + slash + file_name
    logger = logging.getLogger(f)
    logger.setLevel(level)
    handler = RotatingFileHandler(f, maxBytes=max_bytes, backupCount=backup_count)
    formatter = logging.Formatter('%(asctime)s|%(process)d|%(thread)d|'
                                  '|%(levelname)s|%(filename)s:'
                                  '%(lineno)d| %(message)s')
    handler.setFormatter(formatter)

    return handler


def create_app():
    app = Flask('notice', template_folder='templates')
    handler = logger_init()
    app.logger.addHandler(handler)
    app.config.from_object(configDict['prod'])

    # 注册蓝图
    for module in get_modules('app'):
        module_ = importlib.import_module('app' + module)
        for name, obj in inspect.getmembers(module_):
            if isinstance(obj, flask.blueprints.Blueprint):
                app.register_blueprint(obj)

    return app


logging.basicConfig(level=logging.DEBUG)

app = create_app()
