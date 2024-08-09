import app.db.db_connection as conn


def singleton(class_):
    instances = {}

    def getinstance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        else:
            print("it's a singleton class, there is can be only one object!")
        return instances[class_]
    return getinstance


@singleton
class EngineSettings:

    def __init__(self, engine):
        self.engine = engine


settings = EngineSettings(conn.engine_creation(conn.conn_str))

