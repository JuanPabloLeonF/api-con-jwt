import os
from flask import Flask
from app.configuration.configuration_database import db, init_app
from app.exceptions.exception_handler import responseErrorsHandlersGlobal

app: Flask = Flask(__name__)
init_app(app=app)

responseErrorsHandlersGlobal(app=app)

if __name__ == "__main__":
    from app.controllers.user_entity_controller import user_route
    from app.controllers.login_controller import login_route
    app.register_blueprint(login_route)
    app.register_blueprint(user_route)
    port:int = int(os.environ.get("PORT", 5001))
    app.run(debug=True, host="0.0.0.0", port=port)
    with app.app_context():
        db.create_all()