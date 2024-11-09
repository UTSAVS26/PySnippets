import json
import yaml
import logging
from dataclasses import dataclass
from typing import Any, Optional
import os


@dataclass
class AppConfig:
    debug: bool
    database_url: str
    retry_attempts: int


class ConfigLoader:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.logger = logging.getLogger(self.__class__.__name__)
        self.config: Optional[AppConfig] = None

    def load_config(self) -> AppConfig:
        try:
            with open(self.config_path, 'r') as file:
                if self.config_path.endswith('.json'):
                    config_data = json.load(file)
                elif self.config_path.endswith(('.yaml', '.yml')):
                    config_data = yaml.safe_load(file)
                else:
                    raise ValueError("Unsupported configuration file format.")
            # Override with environment variables if available
            config_data['debug'] = os.getenv('DEBUG', config_data.get('debug'))
            config_data['database_url'] = os.getenv('DATABASE_URL', config_data.get('database_url'))
            config_data['retry_attempts'] = int(os.getenv('RETRY_ATTEMPTS', config_data.get('retry_attempts')))
            self.config = AppConfig(**config_data)
            self.logger.info("Configuration loaded successfully.")
            return self.config
        except Exception as e:
            self.logger.error(f"Failed to load configuration: {e}")
            raise 