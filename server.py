import asyncio
import websockets
from groq import Groq

# Setup Groq API
client = Groq(api_key="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")

HOST = '0.0.0.0'
PORT = 8080

async def query_groq(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=512,
            top_p=1,
            stream=False,
        )
        return completion.choices[0].message.content.strip()
    except Exception as e:
        return f"[Groq API error] {str(e)}"

async def handler(websocket, path):
    print(f"Client connected: {websocket.remote_address}")
    try:
        async for message in websocket:
            print(f"User: {message}")
            await websocket.send(f"You: {message}")
            
            # Get AI response
            ai_response = await query_groq(message)
            await websocket.send(f"Groq: {ai_response}")
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")

async def main():
    async with websockets.serve(handler, HOST, PORT):
        print(f"WebSocket server running at ws://{HOST}:{PORT}")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

# pip install websockets groq
