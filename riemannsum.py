print("Riemann sum for y=x^2 with increments of 0.5")
astr = input("Please enter the value a: ")
bstr = input("please enter the value b: ")

a = int(astr)
b = int(bstr)

def f(x):
    return x*x

i = a
rsum = 0

while i < b:
    rsum = rsum + 0.5*f(i)
    i = i + 0.5

i = a + 0.5
lsum = 0

while i <= b:
    lsum = lsum + 0.5*f(i)
    i = i + 0.5

riem = (rsum + lsum)/2
    
print("The sum is: ", riem)
ex = input("Please enter any key ")
    
    
    
    

