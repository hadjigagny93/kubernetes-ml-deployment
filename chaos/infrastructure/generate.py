
import pandas as pd

def map_forward_backward_month(s="2020-01-09", method="backward"):
    def f(year_month):
        y, m = year_month.split("-")
        if m == "01":
            m = "12"
            y = str(int(y) - 1)
        else:
            m = str(int(m) - 1).zfill(2)
        return y + "-" + m
    md_dict = {
        "/2": "28",
        "01": "31",
        "02": "28",
        "03": "31",
        "04": "30",
        "05": "31",
        "06": "30",
        "07": "31",
        "08": "31",
        "09": "30",
        "10": "31",
        "11": "30",
        "12": "31"}
    if method == "forward":
        return s[:8] + md_dict[s[5:7]]
    else:
        return f(s[:7]) + "-" + md_dict[f(s[:7])[5:]] 

class GenerateDataSet:

    def __init__(self, marketing=None, socio=None):
        self.marketing = marketing 
        self.socio = socio 
 
    def _normalize_data(self, method="forward"):
        self.marketing["DATE"] = self.marketing["DATE"].apply(lambda date: map_forward_backward_month(date, method=method))
        return self.marketing.join(self.socio.set_index("DATE"), on="DATE")

    def create_data(self, method="forward"):
        return self._normalize_data(method=method).drop(["DATE", "DURATION_CONTACT"] , axis=1)
        

