from typing import Any
from dataclasses import dataclass

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