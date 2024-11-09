import logging
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class LoggerConfig:
    name: str
    level: int = logging.INFO
    log_file: Optional[str] = None
    formatter: str = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    console: bool = True
    file_mode: str = 'a'


class AdvancedLogger:
    def __init__(self, config: LoggerConfig):
        self.logger = logging.getLogger(config.name)
        self.logger.setLevel(config.level)
        formatter = logging.Formatter(config.formatter)

        if config.console:
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

        if config.log_file:
            file_handler = logging.FileHandler(config.log_file, mode=config.file_mode)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger 