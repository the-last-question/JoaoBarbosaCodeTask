def checkPerfection(num):
  sum = 0
  for i in range(1,num):
     if num % i == 0:
        sum += i
  if sum == num:
    return True
  else:
    return False
	
def Perfection10k():
  for i in range(1,10000):
    if checkPerfection(i):
      print(i)

def main():
  print("Perfect numbers: ")
  Perfection10k()
  
main()