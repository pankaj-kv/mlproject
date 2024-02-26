import sys

def error_message_detail(error, erorr_detail:sys):
    _,_,exc_tb = erorr_detail.exec_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in python script name {filename} line number {line_number} error message {str(error)}"
    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super.__init__(error_mesage)
        self.error_message = error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message