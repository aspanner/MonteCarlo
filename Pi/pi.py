#circumference circle (Kreisumfang) = 2*pi*r
#circle area = r*r*pi
#we will  be doing a statistical sampling by randomly generating data points on a plane. 
# We will lay down the foundation for that in the next section.

#Consider a circle inscribed in a square. If we consider a side of this square to be 2a, we can find the area of the square by squaring its side length and get the answer 4a2. 
#Since half of the side becomes the radius of the circle, we can get the area of the circle as πa^2.
# radius = a

# Area of square = 4a
# Area of circle = pi *a^2
# Ratio = 4a / pi *a*a


import random

sampleSize=100000
n_inside_circle = 0

for i in range(0,sampleSize):
    x = random.random()*2 - 1
    y = random.random()*2 - 1
    if ((x*x+y*y)<=1):
        n_inside_circle +=1
        #print ("inside circle" + str(x) + str(y))
   # print (x,y)

print(n_inside_circle)

print('Pi approximation = ' + str(4*n_inside_circle/sampleSize))

# We understand that the radius of the circle is 1. Therefore, using the Pythagorean theorem, 
# we can determine if a point is residing inside or outside the circle.
#If we consider the generated point pair and the resulting right triangle, we can get the length of its hypotenuse using sqrt(a2 + b2.) 
# and if this value is less than 1, we can say that the respective value pair is residing inside the circle. In the above, 
# a and b denote the lengths of the sides of the triangle taken as the moduli of the x,y coordinates.
