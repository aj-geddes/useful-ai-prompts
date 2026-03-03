# Python WebSocket Server (aiohttp)

## Python WebSocket Server (aiohttp)

```python
from aiohttp import web
import aiohttp
import json
from datetime import datetime
from typing import Set

class WebSocketServer:
    def __init__(self):
        self.app = web.Application()
        self.rooms = {}
        self.users = {}
        self.setup_routes()

    def setup_routes(self):
        self.app.router.add_get('/ws', self.websocket_handler)
        self.app.router.add_post('/api/message', self.send_message_api)

    async def websocket_handler(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)

        user_id = None
        room_id = None

        async for msg in ws.iter_any():
            if isinstance(msg, aiohttp.WSMessage):
                data = json.loads(msg.data)
                event_type = data.get('type')

                try:
                    if event_type == 'auth':
                        user_id = data.get('userId')
                        self.users[user_id] = ws
                        await ws.send_json({
                            'type': 'authenticated',
                            'timestamp': datetime.now().isoformat()
                        })

                    elif event_type == 'join_room':
                        room_id = data.get('roomId')
                        if room_id not in self.rooms:
                            self.rooms[room_id] = set()
                        self.rooms[room_id].add(user_id)

                        # Notify others
                        await self.broadcast_to_room(room_id, {
                            'type': 'user_joined',
                            'userId': user_id,
                            'timestamp': datetime.now().isoformat()
                        }, exclude=user_id)

                    elif event_type == 'message':
                        message = {
                            'id': f'msg_{datetime.now().timestamp()}',
                            'userId': user_id,
                            'text': data.get('text'),
                            'roomId': room_id,
                            'timestamp': datetime.now().isoformat()
                        }

                        # Save to database
                        await self.save_message(message)

                        # Broadcast to room
                        await self.broadcast_to_room(room_id, message)

                    elif event_type == 'leave_room':
                        if room_id in self.rooms:
                            self.rooms[room_id].discard(user_id)

                except Exception as error:
                    await ws.send_json({
                        'type': 'error',
                        'message': str(error)
                    })

        # Cleanup on disconnect
        if user_id:
            del self.users[user_id]
        if room_id and user_id:
            if room_id in self.rooms:
                self.rooms[room_id].discard(user_id)

        return ws

    async def broadcast_to_room(self, room_id, message, exclude=None):
        if room_id not in self.rooms:
            return

        for user_id in self.rooms[room_id]:
            if user_id != exclude and user_id in self.users:
                try:
                    await self.users[user_id].send_json(message)
                except Exception as error:
                    print(f'Error sending message: {error}')

    async def save_message(self, message):
        # Save to database
        pass

    async def send_message_api(self, request):
        data = await request.json()
        room_id = data.get('roomId')

        await self.broadcast_to_room(room_id, {
            'type': 'message',
            'text': data.get('text'),
            'timestamp': datetime.now().isoformat()
        })

        return web.json_response({'sent': True})

def create_app():
    server = WebSocketServer()
    return server.app

if __name__ == '__main__':
    app = create_app()
    web.run_app(app, port=3000)
```
