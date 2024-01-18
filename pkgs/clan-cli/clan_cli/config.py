# CORS configuration
cors_url = [
    "http://localhost",
    "http://127.0.0.1",
    "http://0.0.0.0",
    "http://[::]",
]
cors_ports = [2979, 3000]

# host for the server, frontend, backend and emulators
host = "127.0.0.1"
# used for emmulation and population for testing
port_dlg = 7000
port_ap = 7500
_port_client_base = 8000
c1_port = _port_client_base + 1
c2_port = _port_client_base + 2
dlg_url = f"http://{host}:{port_dlg}/docs"
ap_url = f"http://{host}:{port_ap}/docs"
c1_url = f"http://{host}:{c1_port}/docs"
c2_url = f"http://{host}:{c2_port}/docs"


msg_type_to_label = {
    1: "Attachement",
    2: "Connection Setup",
    3: "Presentation",
    4: "DID Resolution",
    5: "Service De-registration",
    6: "Service Registration",
    7: "Service Discovery",
    8: "Service Operation",
}
