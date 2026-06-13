from flask import Flask

def create_app():
    app = Flask(
        __name__,
        template_folder="../templates"
    )

    from app.controllers.user_controller import user_bp
    app.register_blueprint(user_bp)

    return app