import configparser
from info_me import report_logs

class cfgs():

    __slots__ = ["cfg"]
    def __init__(self) -> None:
        self.cfg = configparser.RawConfigParser()
        report_logs().ins_logs("i","config successfully created")


    def add_cfg(self, m, x, y):
        self.cfg.add_section(m)
        self.cfg.set(m,x,y)
        report_logs().ins_logs("i","collecting a data from web")
        


    def get_cfg(self, m,x):
        self.cfg.read("weather.cfg")
        report_logs().ins_logs("i","get collected a data")
        return self.cfg.get(m, x)


    def io_cfg(self):
        with open("weather.cfg","w+") as w_data:
            self.cfg.write(w_data)
        report_logs().ins_logs("i","push the data to config")

