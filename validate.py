import re

txt = "siphe@gmail.com"
import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
def isValidEmail(email:str)->bool: 
    return True if re.search(regex,email) else False
    
print(isValidEmail(txt))
