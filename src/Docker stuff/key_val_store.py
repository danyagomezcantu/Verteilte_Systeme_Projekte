import threading

store = {}
subscriptions = {}
store_lock = threading.Lock()


def notify_subscribers(key, value, operation, excluding_fd):
    if key in subscriptions:
        for client_fd in subscriptions[key]:
            if client_fd != excluding_fd:
                message = f"{operation}:{key}:{value}\n"
                client_fd.sendall(message.encode())


def subscribe(key, connfd):
    with store_lock:
        if key not in subscriptions:
            subscriptions[key] = []
        subscriptions[key].append(connfd)


def put(key, value, connfd):
    with store_lock:
        store[key] = value
        notify_subscribers(key, value, "PUT", connfd)


def get(key, connfd):
    with store_lock:
        if key in store:
            value = store[key]
            connfd.sendall(value.encode())
        else:
            connfd.sendall(b"key_nonexistent\n")


def delete(key, connfd):
    with store_lock:
        if key in store:
            del store[key]
            notify_subscribers(key, "key_deleted", "DEL", connfd)


def process_command(command, connfd):
    parts = command.split()
    if not parts:
        return
    cmd = parts[0].upper()
    if cmd == "PUT" and len(parts) == 3:
        put(parts[1], parts[2], connfd)
    elif cmd == "GET" and len(parts) == 2:
        get(parts[1], connfd)
    elif cmd == "DEL" and len(parts) == 2:
        delete(parts[1], connfd)
    elif cmd == "SUB" and len(parts) == 2:
        subscribe(parts[1], connfd)
    else:
        connfd.sendall(b"Unknown command\n")
