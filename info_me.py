# create  useful logger
import logging, sys
from types import MappingProxyType

class report_logs():

    __slots__ = ["print_loggy","set_logs"]

    def __init__(self) -> None:
            self.print_loggy = logging.StreamHandler(sys.stdout)
        
            self.print_loggy.setFormatter(
                logging.Formatter(
                    "{asctime} {levelname}: {message}",
                    "%d.%m.%y %I:%M:%S", style="{"    
                )
            )
            self.set_logs = logging.getLogger()
            self.set_logs.addHandler(self.print_loggy)
            self.set_logs.setLevel(logging.DEBUG)

    def ins_logs(self, a, b):

        logs = MappingProxyType({
            "e": logging.error,
            "w": logging.warning,
            "c": logging.critical,
            "i": logging.info
        })
        return logs[a]("\t" + b)

