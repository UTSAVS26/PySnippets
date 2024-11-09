import time
from dataclasses import dataclass
from typing import Callable, Optional
import logging
from functools import wraps
import threading


@dataclass
class RateLimitConfig:
    calls: int
    period: float


class RateLimiter:
    def __init__(self, config: RateLimitConfig):
        self.calls = config.calls
        self.period = config.period
        self.logger = logging.getLogger(self.__class__.__name__)
        self.call_times = []
        self.lock = threading.Lock()

    def __call__(self, func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            with self.lock:
                current_time = time.time()
                self.call_times = [t for t in self.call_times if t > current_time - self.period]

                if len(self.call_times) >= self.calls:
                    wait_time = self.period - (current_time - self.call_times[0])
                    self.logger.warning(f"Rate limit exceeded. Sleeping for {wait_time:.2f} seconds.")
                    time.sleep(wait_time)
                    self.call_times = [t for t in self.call_times if t > time.time() - self.period]

                self.call_times.append(time.time())
                self.logger.info(f"Executing function '{func.__name__}'. Call count: {len(self.call_times)}")
            return func(*args, **kwargs)
        return wrapper 