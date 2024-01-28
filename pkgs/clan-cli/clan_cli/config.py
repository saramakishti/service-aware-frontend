# CORS configuration
cors_url = [
    "http://localhost",
    "http://127.0.0.1",
    "http://0.0.0.0",
    "http://[::]",
]
cors_ports = ["*", 3000, 2979, 8001, 8002]
cors_whitelist = []
for u in cors_url:
    for p in cors_ports:
        cors_whitelist.append(f"{u}:{p}")

# host for the server, frontend, backend and emulators
host = "127.0.0.1"

# Used for eventmessage number to name mapping
group_type_to_label = {
    1: {
        "name": "Attachement",
        1: "Request Send",
        2: "Request Received",
        3: "Response Send",
        4: "Response Received",
    },
    2: {
        "name": "Connection Setup",
        1: "Request Send",
        2: "Request Received",
        3: "Response Send",
        4: "Response Received",
    },
    3: {
        "name": "Presentation",
        1: "Request Send",
        2: "Request Received",
        3: "Respone Send",
        4: "Respone Received",
        5: "Respone Ack",
    },
    4: {
        "name": "DID Resolution",
        1: "Request Send",
        2: "Request Received",
        3: "Response Send",
        4: "Response Received",
    },
    5: {
        "name": "Service De-registration",
        1: "Send",
        2: "Received",
        3: "Success Send",
        4: "Success Received",
    },
    6: {
        "name": "Service Registration",
        1: "Send",
        2: "Received",
        3: "Success Send",
        4: "Success Received",
    },
    7: {
        "name": "Service Discovery",
        1: "Discovery Send",
        2: "Discovery Received",
        3: "Result Send",
        4: "Result Received",
    },
    8: {
        "name": "Service Operation",
        1: "Request Send",
        2: "Request Received",
        3: "Response Send",
        4: "Response Received",
    },
}


# Used for emulation and population for testing
port_dlg = 7000
port_ap = 7500
_port_client_base = 8000
c1_port = _port_client_base + 1
c2_port = _port_client_base + 2
dlg_url = f"http://{host}:{port_dlg}/docs"
ap_url = f"http://{host}:{port_ap}/docs"
c1_url = f"http://{host}:{c1_port}/docs"
c2_url = f"http://{host}:{c2_port}/docs"
