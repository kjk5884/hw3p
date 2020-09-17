# Author: Kyle Kroboth kjk5884@psu.edu
# Section: 2

def digit_sum(n):
  if n<=0:
    return 0
  else:
    return(n % 10 + digit_sum(n//10))

def run():
  total = int(input("Enter an int: "))
  print("sum of digits of " + str(total) + " is " + str(digit_sum(total))+".")

if __name__ == "__main__":
  run()