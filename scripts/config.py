from pydantic import BaseSettings
from enum import Enum
from typing import Optional


class LogLevelEnum(Enum):
    debug = "debug"
    info = "info"
    warning = "warning"
    error = "error"
    critical = "critical"


class GunicornConfig(BaseSettings):
    loglevel: str = LogLevelEnum.info.value
    workers: int = 2
    worker_tmp_dir: str = "/dev/shm"
    graceful_timeout: int = 120
    timeout: int = 120
    keepalive: int = 60

    # error log file
    errorlog: Optional[str] = "-"
    accesslog: Optional[str] = "-"


g_config = GunicornConfig()

# gunicorn variables
loglevel = g_config.loglevel
workers = g_config.workers
errorlog = g_config.errorlog
worker_tmp_dir = g_config.worker_tmp_dir
accesslog = g_config.accesslog
graceful_timeout = g_config.graceful_timeout
timeout = g_config.timeout
keepalive = g_config.keepalive
