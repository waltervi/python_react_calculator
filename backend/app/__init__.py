import os

from flask import Flask

def getErrorObject(error):
    errObj = None
    if ( error is not None ):
        errObj = { "errorMessage" : error }
    return errObj

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, "app.sqlite"),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register the database commands
    from app import db
    db.init_app(app)

    # apply the blueprints to the app
    #from app.controller import records_controller_bp 
    from app.controller import auth_controller_bp
    from app.controller import app_controller_bp
    
    
    #app.register_blueprint(records_controller_bp.bp)
    app.register_blueprint(auth_controller_bp.bp)
    app.register_blueprint(app_controller_bp.bp)
    

    # app.add_url_rule("/", endpoint="index")

    return app
