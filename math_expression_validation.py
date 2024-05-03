#Challenge: check math expression validation

import re
def math_expr(expr: str) -> bool:
  
  valid_expre = re.match(r'^[0-9+\-*/()]+$', expr)
  if valid_expre:
    try:
      result = eval(expr)
      return True
    except:
      return False
  else:
    return False
    
expr = "6-3"
print(math_expr(expr))
