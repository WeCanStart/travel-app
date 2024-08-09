import app.db.db_tables as dbt
import app.db.db_connection as conn
import app.db.db_settings as st


def authentication(name: str, password: str) -> bool:
    user_data = dbt.User(nickname=name, user_password=password, email= "")
    session = conn.session_creation(st.settings.engine)
    with session(bind=st.settings.engine) as db:
        checking_user = db.query(dbt.User).filter_by(nickname=user_data.nickname).all()
        if len(checking_user) > 1:
            print("Error more users than expected(1 expected)")
            return False
        elif len(checking_user) == 1:
            return False
        else:
            return True


def registration(name: str, password: str, email: str = "") -> bool:
    if authentication(name, password):
        session = conn.session_creation(st.settings.engine)
        with session(bind=st.settings.engine) as db:
            new_user = dbt.User(nickname=name, user_password=password, email=email)
            db.add(new_user)
            db.commit()
            db.refresh(new_user)
        return True
    print('such user is already exists')
    return False


