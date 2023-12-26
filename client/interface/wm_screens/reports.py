# --------------------------------------------------------------------------------------- #
# 
#   This is the REPORTS page window manager screen module.
#   Any functions related to this particular interface should
#   specifically be programmed in this environment.
# 
# --------------------------------------------------------------------------------------- #


class Report(object):
    def __init__(self):
        pass
    
    def display_report(self):
        return
    
    def get_report_data(self, report_duration:str) -> dict:
        return
    
    def download_report(self):
        return
    
    def email_report(self):
        return
    
    def print_report(self):
        return
    
    def _create_report(self, branches:list, report_duration:str, report_heading:str):
        return
    
class ManagerReport(Report):
    def get_branch_id(self):
        return
    
    def get_expenditure(self):
        return
    
    def get_profits(self):
        return
    
    def get_inventory(self):
        return
    
    def get_sales(self):
        return
    
    def get_performance(self):
        return
    
    def get_average_serving_time(self):
        return

class HRReport(Report):
    def __init__(self, report:Report):
        self.report = report
        
    def get_branch_performance(self, report_heading: str):
        return