import sys
def error(err_no, err_desc, end):
  import datetime
  error_dec = "Time: "+str(datetime.datetime.now())+" Error no: " + str(err_no) + "  Desc: " + err_desc + " end\n"
  with open('log.txt', 'a') as afile:
    afile.write(error_dec)
  if end:
     sys.exit()
