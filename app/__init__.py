from flask import Flask, g
from app.blueprints.user import user


class App(Flask):
    def process_response(self, response):
        super(App, self).process_response(response)
        return response


app = App(__name__)
app.config.from_object('app.config.Config')

app.register_blueprint(user, url_prefix='/user')


@app.errorhandler(Exception)
def handle_error(error):
    message = error.description if hasattr(error, 'description') else [
        str(x) for x in error.args]
    response = {
        'error': {
            'type': error.__class__.__name__,
            'message': message
        }
    }

    return response, error.code if hasattr(error, 'code') else 500
