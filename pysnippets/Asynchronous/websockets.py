import asyncio
import websockets
import logging

async def websocket_echo(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello Server!")
        logging.info("Message sent to server")
        response = await websocket.recv()
        logging.info(f"Received from server: {response}")

async def main():
    await websocket_echo('ws://localhost:8765')

if __name__ == "__main__":
    asyncio.run(main()) 