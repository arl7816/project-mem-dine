# backend/app.py
from flask import Flask, jsonify, request
from flask_cors import CORS

from dataclasses import dataclass
from typing import Any

app = Flask(__name__)
# Enable CORS so your Vue frontend can securely communicate with Flask
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}})

@dataclass(kw_only=True)
class ResponseObject:
    status: str
    status_code: int
    data: Any

    @staticmethod
    def success(data: Any = None, status_code: int = 200) -> 'ResponseObject':
        """Quickly generate a clean success payload."""
        return ResponseObject(status="success", status_code=status_code, data=data)

    @staticmethod
    def error(message: str, status_code: int = 400) -> 'ResponseObject':
        """Quickly generate a standardized error payload."""
        return ResponseObject(status="error", status_code=status_code, data={"error": message})

from functools import wraps

def validate_response(func):
    @wraps(func)  # Keeps the original function's metadata intact
    def wrapper(*args, **kwargs):
        
        # 2. Execute the original function
        result = func(*args, **kwargs)
        
        if not isinstance(result, ResponseObject):
            raise TypeError("API not returning a ResponseObject")
        
        # 4. Return the result
        return jsonify(result)
    return wrapper

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
    app.run(port=5000, debug=True)
