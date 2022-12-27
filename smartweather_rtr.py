import requests, enum, json, re
from info_me import report_logs
from tempfile import TemporaryFile
from smartweather_db import cfgs
import bs4


class http_errors(enum.Enum):
    SUCCESSFULL_CONNECTED = 200
    INTERNAL_ERROR_OCCURED = 404
    REQUEST_FAILED = 404
    NOT_ALLOW_US = 403


class http_err:
    def http_err_status(p_urls):
        try:
            match p_urls:
                case http_errors.SUCCESSFULL_CONNECTED.value:
                    report_logs().ins_logs("c","http connected..!!")
                case http_errors.INTERNAL_ERROR_OCCURED.value:
                    report_logs().ins_logs("c","cant reterive a data.!!")
                case http_errors.REQUEST_FAILED.value:
                    report_logs().ins_logs("w","requests failed..!!")
        except:
            return "something went wrong"


class http_connc(http_err):


    def __init__(self, urls):
        try:
            http_err.__init__(self)
            self.url = requests.get(urls)
            self.check = http_err.http_err_status(self.url.status_code)
        except requests.exceptions.ConnectionError:
            report_logs().ins_logs("c","http connection failed..!!")
        except json.decoder.JSONDecodeError:
            report_logs().ins_logs("c","cant reterive a data.!!")
        except AttributeError:
            report_logs().ins_logs("w","mistyped errors..!!")

    
    def get_data(self):
        z = bs4.BeautifulSoup(self.url.text, "html.parser")
        p = z.text.split("\n")[0]
        zzz = re.findall("\d:\d\d", p)
        start,end = p.index("".join(zzz)) - 15, p.index("".join(zzz))
        w_data = p[start:end].strip(" ").split("C")
        w_data = w_data[0].replace("ther","").replace("°","").replace("er","").replace("h","")
        dt_collects = {
            "cf": w_data
        }
        add_data = cfgs()
        add_data.add_cfg("C","celusis",str(dt_collects["cf"]))
        add_data.io_cfg()
        return None