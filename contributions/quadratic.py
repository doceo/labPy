from math import sqrt
print('Solve the quadratic equation: ax**2 + bx + c = 0')
a = float(input('Please enter a : '))
b = float(input('Please enter b : '))
c = float(input('Please enter c : '))
if a==0:
  print("What the what?? This is not a quadratic equation.")
  
delta = (b**2) - (4*a*c)
solution1 = (-b-sqrt(delta))/(2*a)
solution2 = (-b+sqrt(delta))/(2*a)

print('The solutions are {0} and {1}'.format(solution1,solution2))
