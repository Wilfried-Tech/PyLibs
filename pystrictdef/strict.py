import types

def checkType(*t_args, **t_kwargs):
  def decorator(function):
    def checker(*args, **kwargs):
      if len(args) != len(t_args):
        raise TypeError("{0.__name__}() missing {diff} required positional argument".format(function, diff=len(t_args)-len(args)))
      for i,_type in enumerate(t_args):
        if type(args[i]) is not _type:
          raise TypeError("the argument {index} must be {type} type".format(index=i, type= _type.__name__))
      return function(*args, **kwargs)
    return checker
  return decorator

Function = types.FunctionType
