import os

from open_note_scanner.pdf_server.server import app


from waitress import serve

# TODO: Put all application related configuration into a file.
config = {'ip': '0.0.0.0', 'port': 8080}

# Generate a new Key each time the app is run.
app.secret_key = os.urandom(16)


# If you want a debugging server set variable below to True, otherwise leave it as is.
DEBUG = False

# Run the server.
if DEBUG:
    app.run(host=config['ip'], port=config['port'], threaded=True)
else:
    serve(app, listen='{}:{}'.format(config['ip'], config['port']))
