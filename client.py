import asyncio
import websockets

async def client():
    uri = "ws://127.0.0.1:8080"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hello Server!")
        response = await websocket.recv()
        print("Server says:", response)

if __name__ == "__main__":
    asyncio.run(client())
