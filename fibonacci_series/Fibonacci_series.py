#initialize the fibonacci function
def fibonnaci_series(number):
    a, b = 0, 1
    while a <= number:
        yield a
        a,b = b, a+b

for data in fibonnaci_series(50):
    #print the result
    print(data)