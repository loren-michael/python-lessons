# recursion is when a function calls itself

def add_one(num):
    
    if (num >= 9):
        return num +1
    
    total = num + 1
    print(total)

    return add_one(total)

my_new_total = add_one(0)
print(my_new_total)



value = True

while value:
    print(value)
    value = False


value2 = "y"
count = 0

while value2:
    count += 1
    print(count)
    if count == 5:
      break
    else:
        value2 = 0
        continue