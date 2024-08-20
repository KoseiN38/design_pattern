from abc import ABC, abstractmethod

from src.structure.flyweight.core.memory_usage import add_memory_usage


@add_memory_usage
class BaseModel(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @classmethod
    def _validate_string(cls, value: str, field_name: str):
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value:
            raise ValueError(f"{field_name} cannot be empty")

    @classmethod
    def _validate_positive_number(cls, value: float, field_name: str):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field_name} must be a number (int or float)")
        if value <= 0:
            raise ValueError(f"{field_name} must be a positive number")

    @classmethod
    def _validate_instance(cls, value, expected_type, field_name: str):
        if not isinstance(value, expected_type):
            raise TypeError(
                f"{field_name} must be an instance of {expected_type.__name__}"
            )
