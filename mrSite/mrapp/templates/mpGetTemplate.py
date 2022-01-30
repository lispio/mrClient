from enum import Enum

from .configModule import mpConfig


class mpGetQuery(Enum):
    mpEcho = f"http://{mpConfig.mpHost.value}:{mpConfig.mpPort.value}/echo"