# Hint:  use Google to find python function

####a) 
from datetime import datetime
date_start = '01-02-2013'  
date_stop = '07-28-2015'   
date_format = '%m-%d-%Y'


def delta_calc(date_start, date_stop, date_format):
    a = datetime.strptime(date_start, date_format)
    b = datetime.strptime(date_stop, date_format) 
    delta = b-a 
    return delta


delta = delta_calc('01-02-2013','07-28-2015','%m-%d-%Y')
print("{0} days have passed".format(delta.days))

####b)  
from datetime import datetime
date_start = '12312013'  
date_stop = '05282015'  

def delta_calc(date_start, date_stop, date_format):
    a = datetime.strptime(date_start, date_format)
    b = datetime.strptime(date_stop, date_format) 
    delta = b-a 
    return delta

delta = delta_calc(date_start, date_stop, date_format)
print("{0} days have passed".format(delta.days))



####c)  
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'
date_format = '%d-%b-%Y' 

delta = datetime.strptime(date_stop, date_format) - datetime.strptime(date_start, date_format)
print("{0} days have passed".format(delta.days))
