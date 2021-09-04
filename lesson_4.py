def conversion(temperature, scale):
    if scale == "fahrenheit" or scale == "F":
        celsius = (temperature - 32) * 5/9
        print(str(temperature) + "F can be converted to " + str(celsius) + "C")
    elif scale == "celsius" or scale == "C":
        fahrenheit = (temperature * 9/5) + 32
        print(str(temperature) + "C can be converted to " + str(fahrenheit) + "F")

a = "C"
b = "F"
conversion(212, "celsius")
conversion(38, a)
conversion(38, b)

def sphere_volume(radius):
    volume = (4/3) * 3.14 * (radius ** 3)
    return volume

c = sphere_volume(2)
d = sphere_volume(8)
print(c)
print(d)

def factorial(num):
    try:
        float(num)
    except:
        return(print("Error, Use numbers only"))
    if num > 0:
        fact = num
        while num > 1:
            fact *= (num - 1)
            num -= 1    
    elif num == 0:
        fact = num + 1
    else:
        return(print("No negative numbers"))
    print(fact)

factorial(7)