import types

def checkType(*t_args, **t_kwargs):
  
  def decorator(function):
    def checker(*args, **kwargs):
      pass
    
    return checker
  return decorator

Function = types.FunctionType