import functools
from flask import Blueprint
from flask import g
from flask import request
from flask import session
from flask import jsonify
from .. import getErrorObject
#from ..service.user_service import user_service_create_user,user_service_validate_login
from ..service.user_service import user_service

bp = Blueprint("auth", __name__, url_prefix="/v1/auth")

def validate_session(view):
    """View decorator that validates logged in users."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user_id is None:
            return getErrorObject("User must be logged in"), 401

        return view(**kwargs)

    return wrapped_view

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from the database into ``g.user``."""
    user_id = session.get("user_id")
    g.user_id = user_id
    # if user_id is None:
    #     g.user_id = None
    # else:
    #     g.user_id = user_id

@bp.route("/register", methods=["POST"])
def register():
    content = request.json
    username = content["username"]
    password = content["password"]
    validation = None

    #Basic validations
    if not username or len(username) <= 3:
        validation = "Invalid username."
    elif not password or len(password)  <= 3:
        validation = "Invalid password."

    if validation is not None:
        return getErrorObject(validation), 400
    
    new_user, error = user_service.create_user(username,password)
    if ( error is not None):
        return error, 400

    # store the user id in a new session and return to the index
    session.clear()
    session["user_id"] = new_user["id"]
    
    return jsonify(new_user), 200

@bp.route("/login", methods=["POST"])
def login():
    content = request.json
    username = content["username"]
    password = content["password"]
    validation = None

    #Basic validations
    if not username or len(username) <= 3:
        validation = "Invalid username."
    elif not password or len(password)  <= 3:
        validation = "Invalid password."

    if validation is not None:
        return getErrorObject(validation), 400
    
    user, error = user_service.validate_login(username,password)

    if error is not None:
        return error, 401

    # store the user id in a new session and return to the index
    session.clear()
    session["user_id"] = user["id"]
    return jsonify(user), 200

@bp.route("/logout")
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return '', 200
