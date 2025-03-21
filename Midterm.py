import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
     import math 

     result = math.pi * radius ** 2

     return round(result, 2)

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    result = ''

    if n < 4:

        return "The triangle height should be at least 4."

    else: 

        for i in range(n):

            for j in range(i + 1):

                if j == 0 or j == i or i == n - 1:

                    result += "*"

                else: 

                    result += " "
   
            result += "\n"

    return result.rstrip()


# Q3: Inverted Pyramid
def inverted_pyramid(n):

    result = ''

    if n < 3:

        return "The pyramid height should be at least 3."

    else: 
    
        for i in range(n - 1, -1, -1):

            result += " " * (n - i - 1)

            result += "*" * (2 * i + 1)

            result += "\n"
   
        return result.strip()

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()