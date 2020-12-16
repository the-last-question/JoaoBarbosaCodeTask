def checkpswd(pswd):
  Uppercheck = False
  Lowercheck = False
  Digitcheck = False
  if len(pswd) >= 8:
    for c in pswd:
      if c.isupper():
        Uppercheck = True
      elif c.islower():
        Lowercheck = True
      elif c.isdigit():
        Digitcheck = True
    if Uppercheck and Lowercheck and Digitcheck:
      return True
    else:
      return False
  else:
    return False
	
def main():
  pswd = input("What's your password: ")
  check = checkpswd(pswd)
  if check:
    print("Password accepted")
  else:
    print("Password denied")

if __name__ == "__main__":
    main()