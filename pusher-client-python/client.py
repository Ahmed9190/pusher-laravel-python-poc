import os
import pusher
import json
from websocket import create_connection


# Initialize Pusher client for triggering events
pusher_client = pusher.Pusher(
    app_id=os.getenv("PUSHER_APP_ID"),
    key=os.getenv("PUSHER_KEY"),
    secret=os.getenv("PUSHER_SECRET"),
    cluster=os.getenv("PUSHER_CLUSTER"),
    ssl=True,
)


def send_message(message):
    """Send message to Laravel via Pusher"""
    pusher_client.trigger(
        "python-laravel",
        "MessageEvent",
        {"message": message, "sender": "python-client"},
    )
    print(f"Sent: {message}")


def listen_for_messages():
    """Listen for messages from Laravel via WebSocket"""
    ws_url = f"wss://ws-{os.getenv('PUSHER_CLUSTER')}.pusher.com:443/app/{os.getenv('PUSHER_KEY')}?protocol=7"

    try:
        ws = create_connection(ws_url)
        print("Connected to Pusher WebSocket")

        # Subscribe to channel
        subscribe_msg = {
            "event": "pusher:subscribe",
            "data": {"channel": "python-laravel"},
        }
        ws.send(json.dumps(subscribe_msg))

        while True:
            response = json.loads(ws.recv())
            if response["event"] == "MessageEvent":
                data = json.loads(response["data"])
                if data.get("sender") != "python-client":  # Avoid echo
                    print(f"\nReceived new message: {data['message']}")

    except Exception as e:
        print(f"WebSocket Error: {str(e)}")
    finally:
        ws.close()


send_message("Initial message from Python")
listen_for_messages()
