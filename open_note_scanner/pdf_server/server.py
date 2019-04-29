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
        Flask template return.
    """

    template_return = flask.render_template('index.html')

    return template_return


@app.route('/documentation')
def documentation():
    """
    Render the documentation of the API

    Returns:
        Flask template return.
    """
    template_return = flask.render_template('documentation.html')

    return template_return


@app.route('/generate', methods=['POST', 'GET'])
def generate():
    """
    Simple wrapper for the API to generate the pdf with a form on the HTML.

    Returns:
        Template based on the method.
    """

    if flask.request.method == 'POST':
        page_size = flask.request.form.get('page-size')
        qr_data = flask.request.form.get('qr-data')
        int_pages = flask.request.form.get('int-pages')
        template_return = flask.redirect('/api/{}/{}/{}'.format(page_size, qr_data, int_pages))

    else:
        template_return = flask.render_template('generate_pdf.html')

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
