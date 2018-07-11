
def get_db_uri(dbinfo):
    # 提供默认值
    DB = dbinfo.get("DB") or "mysql"
    DRIVER = dbinfo.get("DRIVER") or "pymysql"
    USER = dbinfo.get("USER") or "root"
    PASSWORD = dbinfo.get("PASSWORD") or "root"
    HOST = dbinfo.get("HOST") or "localhost"
    PORT = dbinfo.get("PORT") or "3306"
    NAME = dbinfo.get("NAME") or "mysql"

    return "{}+{}://{}:{}@{}:{}/{}".format(DB, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:

    DEBUG = False

    TESTING = False

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "Rock"


class DevelopConfig(Config):

    DEBUG = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)

    SESSION_TYPE = "redis"


class TestingConfig(Config):

    TESTING = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):

    DEBUG = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):

    DEBUG = True

    DATABASE = {
        "USER": "root",
        "PASSWORD": "1190",
        "HOST": "localhost",
        "PORT": "3306",
        "NAME": "flaskproject",
        "DB": "mysql",
        "DRIVER": "pymysql"
    }

    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    "develop": DevelopConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "product": ProductConfig,
    "default": DevelopConfig
}

