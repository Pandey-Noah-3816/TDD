
def leapyear(x):
  leap = False
  if x % 4 == 0:
    leap = True
    if x % 100 == 0:
      leap = False
      if x % 400 == 0:
        leap = True
    return (leap)

  else:
    return(leap)
