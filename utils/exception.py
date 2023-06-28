import sys

def error_message_detail(error, error_detail:sys):
    _,_,exc_tb=error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    err_msg = "Error oocured in [{0}] : [{1}] : [{2]".format(file_name, exc_tb.tb_lineno, str(error))

class CustomException(Exception):
    def __init__(self, err_msg, error_detail:sys):
        super.__init__(err_msg)
        self.err_msg = error_message_detail(err_msg, error_detail=error_detail)

    def __str__(self):
        return self.err_msg