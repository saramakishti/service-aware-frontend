from enum import Enum


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    UNKNOWN = "unknown"


class Role(Enum):
    PROSUMER = "service_prosumer"
    AP = "AP"
    DLG = "DLG"
