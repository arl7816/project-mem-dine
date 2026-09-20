from functools import wraps

from flask import jsonify

from classes.api_classes import ResponseObject

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