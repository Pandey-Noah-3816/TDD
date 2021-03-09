
def leapyear(x):
  leap = False
  if x % 4 == 0:
    leap = True
    if x % 100 == 0:
      leap = False
    return (leap)

  else:
    return(leap)
