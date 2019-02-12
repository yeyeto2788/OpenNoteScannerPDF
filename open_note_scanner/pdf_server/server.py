"""

Main server application and logic for the Open Note Scanner pdf generator server,
this has an API which is located in
<ip>:<port>//api/<string:str_size>/<string:qr_data>/<int:int_pages>

"""
import flask
import flask_restful

from open_note_scanner.pdf_server.api import generate_pdf

# noinspection PyTypeChecker
app = flask.Flask(__name__, static_url_path="/static")
API = flask_restful.Api(app)
API.add_resource(generate_pdf.APIGenerator,
                 '/api/<string:str_size>/<string:qr_data>/<int:int_pages>')


@app.route('/')
@app.route('/home')
def home():
    """
    Simple rendering of the `index.html` page.

    Returns:

    """

    template_return = flask.render_template('index.html')

    return template_return


@app.errorhandler(404)
def page_not_found(error):
    """
    Function for handling all bad requests to the application.

    Args:
        error:

    Returns:
        Template for 404 error code.

    """

    return flask.render_template('404.html'), 404
