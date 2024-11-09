import asyncio
import logging
from dataclasses import dataclass
from typing import Dict, Set, Callable, Any, Coroutine

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class Event:
    """Class representing an event with name and data"""
    name: str
    data: Any = None

class EventEmitter:
    """Asynchronous event emitter that handles event subscriptions and emissions"""
    
    def __init__(self):
        self._subscribers: Dict[str, Set[Callable]] = {}
        self._lock = asyncio.Lock()
        logging.info("EventEmitter initialized")

    async def subscribe(self, event_name: str, callback: Callable[[Event], Coroutine]):
        """Subscribe to an event with an async callback"""
        async with self._lock:
            if event_name not in self._subscribers:
                self._subscribers[event_name] = set()
            self._subscribers[event_name].add(callback)
            logging.info(f"Subscribed to event: {event_name}")

    async def unsubscribe(self, event_name: str, callback: Callable[[Event], Coroutine]):
        """Unsubscribe from an event"""
        async with self._lock:
            if event_name in self._subscribers and callback in self._subscribers[event_name]:
                self._subscribers[event_name].remove(callback)
                logging.info(f"Unsubscribed from event: {event_name}")

    async def emit(self, event: Event):
        """Emit an event to all subscribers"""
        if event.name not in self._subscribers:
            logging.warning(f"No subscribers for event: {event.name}")
            return

        tasks = []
        async with self._lock:
            subscribers = self._subscribers[event.name].copy()

        for callback in subscribers:
            try:
                task = asyncio.create_task(callback(event))
                tasks.append(task)
            except Exception as e:
                logging.error(f"Error creating task for event {event.name}: {e}")

        if tasks:
            results = await asyncio.gather(*tasks, return_exceptions=True)
            for result in results:
                if isinstance(result, Exception):
                    logging.error(f"Error in event handler: {result}")

# Example usage
async def temperature_handler(event: Event):
    """Handle temperature events"""
    logging.info(f"Temperature changed to: {event.data}°C")
    if event.data > 30:
        logging.warning("High temperature alert!")

async def humidity_handler(event: Event):
    """Handle humidity events"""
    logging.info(f"Humidity changed to: {event.data}%")
    if event.data > 80:
        logging.warning("High humidity alert!")

async def main():
    # Create event emitter
    emitter = EventEmitter()

    # Subscribe to events
    await emitter.subscribe("temperature", temperature_handler)
    await emitter.subscribe("humidity", humidity_handler)

    # Simulate sensor readings
    for _ in range(3):
        # Emit temperature events
        await emitter.emit(Event("temperature", 32))
        await asyncio.sleep(1)

        # Emit humidity events
        await emitter.emit(Event("humidity", 85))
        await asyncio.sleep(1)

    # Unsubscribe from events
    await emitter.unsubscribe("temperature", temperature_handler)
    await emitter.unsubscribe("humidity", humidity_handler)

if __name__ == "__main__":
    asyncio.run(main())