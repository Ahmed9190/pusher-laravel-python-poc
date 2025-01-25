# Pusher Laravel Python POC

A proof-of-concept (POC) repository demonstrating bidirectional communication between a Laravel server and a Python client using Pusher. This setup allows Laravel to broadcast events to a Python client and vice versa.

## Project Structure

```

.
├── docker-compose.yml # Docker Compose file for orchestrating services
├── .env.example # Environment variables for the project
├── pusher-client-python # Python client implementation
│ ├── client.py # Python script for Pusher communication
│ ├── Dockerfile # Dockerfile for Python client
│ └── requirements.txt # Python dependencies
└── pusher-server-laravel # Laravel server implementation
├── app/Events/MessageEvent.php # Event class for broadcasting messages
├── app/Http/Controllers/MessageController.php # Controller to handle messages
├── Dockerfile # Dockerfile for Laravel server
├── routes/api.php # API routes for the Laravel server
└── other Laravel files...

```

---

## Prerequisites

1. Docker and Docker Compose installed.
2. Pusher account. Create a new app on the [Pusher dashboard](https://pusher.com/) to get your `APP_ID`, `APP_KEY`, `APP_SECRET`, and `APP_CLUSTER`.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Ahmed9190/pusher-laravel-python-poc.git
cd pusher-laravel-python-poc
```

### 2. Configure Environment Variables

Rename the `.env.example` file to `.env` and replace the placeholders with your Pusher credentials:

```dotenv
PUSHER_APP_ID=your-app-id
PUSHER_APP_KEY=your-app-key
PUSHER_APP_SECRET=your-app-secret
PUSHER_APP_CLUSTER=your-app-cluster
PUSHER_HOST=api-${PUSHER_APP_CLUSTER}.pusher.com
```

### 3. Build and Start the Containers

Use Docker Compose to build and start the services:

```bash
docker-compose up --build
```

---

## Test Bidirectional Communication

### From Python to Laravel

The Python client sends an initial message to the Laravel server via Pusher. Check the logs of the Python container to confirm:

```bash
docker logs pusher-client-python -f
```

You should see:

```
Sent: Initial message from Python
Connected to Pusher WebSocket
```

### From Laravel to Python

Send a message from Laravel to Python using the `/api/send-message` endpoint:

```bash
curl -X POST http://localhost:9000/api/send-message \
    -H "Content-Type: application/json" \
    -d '{"message": "Hello from Laravel!"}'
```

The Python client should display:

```
Received new message: Hello from Laravel!
```

---

## Environment Variables

| Variable             | Description                          | Example                                |
| -------------------- | ------------------------------------ | -------------------------------------- |
| `PUSHER_APP_ID`      | Pusher app ID                        | `123456`                               |
| `PUSHER_APP_KEY`     | Pusher app key                       | `abcd1234`                             |
| `PUSHER_APP_SECRET`  | Pusher app secret                    | `secret1234`                           |
| `PUSHER_APP_CLUSTER` | Pusher cluster                       | `mt1`                                  |
| `PUSHER_HOST`        | Pusher host URL (default for Pusher) | `api-${PUSHER_APP_CLUSTER}.pusher.com` |

---

## Debugging

### Laravel

To view Laravel logs:

```bash
docker exec -it pusher-server-laravel bash
tail -f storage/logs/laravel.log
```

### Python

To view Python client logs:

```bash
docker logs pusher-client-python -f
```

---

## License

This project is licensed under the MIT License.

---

## Notes

Feel free to fork and customize this POC for your specific needs. Contributions and improvements are welcome!

---

### Key Updates:

1. **Single `.env.example` File**:

   - Contains all necessary Pusher configurations used by both services (`laravel` and `python-client`).
   - Referenced directly in the `docker-compose.yml` file.

2. **Instructions**:

   - Simplified environment setup for a single `.env` file.
   - Unified the explanation for Pusher configuration.

3. **Testing**:
   - Includes specific commands to verify bidirectional communication.
