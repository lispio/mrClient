from enum import Enum


class mpConfig(Enum):
    mpHost = "127.0.0.1"
    mpPort = "6668"


class mpGetQuery(Enum):
    mpEcho = f"http://{mpConfig.mpHost.value}:{mpConfig.mpPort.value}/echo"
