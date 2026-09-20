# backend/app.py
from flask import Flask
from flask_cors import CORS

from classes.api_classes import ResponseObject

from helpers.validate_response import validate_response
from settings import settings

app = Flask(__name__)
# Enable CORS so your Vue frontend can securely communicate with Flask
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@app.route('/api/hello')
@validate_response
def helloWorld():
    ro = ResponseObject(
        status="success",
        data="Hello World!",
        status_code=200
    )

    return ro

# to get me started up run 'python app.py'
if __name__ == '__main__':
    app.run(port=settings.port, debug=settings.debug)
