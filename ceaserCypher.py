def encryption(str, key):
  encrypted = ""
  for c in str:
    if c.isupper():
      char_numeric = ord(c) - ord('A')
      new_char_numeric = (char_numeric + key) % 26 + ord('A')
      new_char = chr(new_char_numeric)
      encrypted += new_char
    elif c.islower():
      char_numeric = ord(c) - ord('a')
      new_char_numeric = (char_numeric + key) % 26 + ord('a')
      new_char = chr(new_char_numeric)
      encrypted += new_char
    else:
      encrypted += c

  return encrypted
  
def main():
  string = input("String to decypher: ")
  key = int(input("Value to shift: "))
  print(string, " encrypted: ", encryption(string, key))
  
main()