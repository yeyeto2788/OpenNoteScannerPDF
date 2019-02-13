## NAME
server

## DESCRIPTION
Main server application and logic for the Open Note Scanner pdf generator server,
this has an API which is located in
`<ip>:<port>//api/<string:str_size>/<string:qr_data>/<int:int_pages>`

## FUNCTIONS

### `home()`
Simple rendering of the `index.html` page.

**Returns:** 

### `page_not_found(error)`
Function for handling all bad requests to the application.

**Args:**

error:

**Returns:** Template for 404 error code.

## DATA
API = <flask_restful.Api object>

app = <Flask 'server'>
