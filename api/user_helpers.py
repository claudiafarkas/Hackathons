from db import db
from db import User

def get_user_by_email(email):
    return User.query.filter(User.email == email).first()

def get_user_by_session_token(session_token):
    return User.query.filter(User.session_token == session_token).first()

def get_user_by_update_token(update_token):
    return User.query.filter(User.update_token == update_token).first()

def verify_credentials(email, password):
    user = get_user_by_email(email)

    if user is None:
        return False, None

    return user.verify_password(password), user

def create_user(email, password, user_id, name):
    optional_user = get_user_by_email(email)

    if optional_user is not None:
        return False, optional_user

    user = User(email=email, password=password, user_id=user_id, name=name, rewards=0)

    # Add to database
    db.session.add(user)
    db.session.commit()

    return True, user


def renew_session(update_token):
    user = get_user_by_update_token(update_token)

    if user is None:
        raise Exception("Invalid update token.")

    user.renew_session()
    db.session.commit()
    return user

def update_rewards(email, rewards):
    user = get_user_by_email(email)

    if user is None:
        raise Exception("Invalid user.")

    user.update_rewards(rewards)
    db.session.commit()
    return user