# generate_pdf.py

## NAME
generate_pdf - Simple API for generating the `.pdf` file within the server and return it already generated.

## CLASSES

### `flask_restful.Resource(flask.views.MethodView)`
APIGenerator


### `class APIGenerator(flask_restful.Resource)`
`.pdf` file server API to send the pdf files to the clients doing a get request.

Method resolution order:
APIGenerator
flask_restful.Resource
flask.views.MethodView
flask.views.View
builtins.object

Static methods defined here:


### `get(str_size, qr_data, int_pages)`
Return the File from server if exists on the filesystem.

This will do a check whether the size is either `A4` or `letter`, then it checks
for the length of the `qr_data` argument and finally if will generate the `.pdf`
file returning it to the client.


Data and other attributes defined here:

methods = {'GET'}


Methods inherited from flask_restful.Resource:


### `dispatch_request(self, *args, **kwargs)`
Subclasses have to override this method to implement the
actual view function code.  This method is called with all
the arguments from the URL rule.


Data and other attributes inherited from flask_restful.Resource:

method_decorators = []

representations = None


Class methods inherited from flask.views.View:


### `as_view(name, *class_args, **class_kwargs) from flask.views.MethodViewType`
Converts the class into an actual view function that can be used
with the routing system.  Internally this generates a function on the
fly which will instantiate the :class:`View` on each request and call
the :meth:`dispatch_request` method on it.

The arguments passed to :meth:`as_view` are forwarded to the
constructor of the class.


Data descriptors inherited from flask.views.View:

__dict__
dictionary for instance variables (if defined)

__weakref__
list of weak references to the object (if defined)


Data and other attributes inherited from flask.views.View:

decorators = ()

provide_automatic_options = None
