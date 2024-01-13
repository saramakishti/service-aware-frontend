import dataclasses


@dataclasses.dataclass
class Config:
    host: str
    port_dlg: int
    port_ap: int
    port_client_base: int


config = Config(host="127.0.0.1", port_dlg=6000, port_ap=6600, port_client_base=7000)
