def palindrome(string):
  if not string:
    return True
  elif len(string) == 1:
    return True

  if string[0] == string[-1]:
    mid_string = string.replace(string[0], "")
    new_string = mid_string.replace(string[-1], "")
    if palindrome(new_string):
      return True
    else: return False

  return False
  
def main():
  string = input("String to check: ")
  if palindrome(string):
    print("Palindrome!!")
  else:
    print("Not a Palindrome...")
	
main()