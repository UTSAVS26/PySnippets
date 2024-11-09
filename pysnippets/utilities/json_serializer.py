import json
from dataclasses import is_dataclass, asdict, fields
from typing import Type, TypeVar, Any, Dict
import logging

T = TypeVar('T')


class JSONSerializer:
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)

    def serialize(self, obj: Any) -> str:
        if not is_dataclass(obj):
            self.logger.error("serialize() expects a dataclass instance.")
            raise TypeError("serialize() expects a dataclass instance.")
        try:
            json_str = json.dumps(asdict(obj), default=str)
            self.logger.info("Object serialized successfully.")
            return json_str
        except Exception as e:
            self.logger.error(f"Serialization failed: {e}")
            raise

    def deserialize(self, json_str: str, cls: Type[T]) -> T:
        if not is_dataclass(cls):
            self.logger.error("deserialize() expects a dataclass type.")
            raise TypeError("deserialize() expects a dataclass type.")
        try:
            data = json.loads(json_str)
            field_types: Dict[str, Any] = {f.name: f.type for f in fields(cls)}
            for field_name, field_type in field_types.items():
                if is_dataclass(field_type) and field_name in data:
                    data[field_name] = self.deserialize(json.dumps(data[field_name]), field_type)
            field_names = {f.name for f in fields(cls)}
            filtered_data = {k: v for k, v in data.items() if k in field_names}
            obj = cls(**filtered_data)
            self.logger.info("Object deserialized successfully.")
            return obj
        except Exception as e:
            self.logger.error(f"Deserialization failed: {e}")
            raise 