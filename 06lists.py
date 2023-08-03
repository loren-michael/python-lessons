users = ["Loren", "Amanda", "Celeste", "Nova"]

data = ["Loren", 42, True]

emptylist = []

print("Loren" in users)
print("Loren" in data)
print("Loren" in emptylist)

print(users[0])
print(users[-1])

print(users.index("Celeste"))
print(users[0:2])
print(users[0:])

print(len(data))

users.append('Dixie')
users += ['Snickers']
print(users)

users.extend(["Tyke"])
print(users)

# users.extend(data)
# print(users)

users.insert(0, 'Beth')
print(users)

users[2:2] = ['Eddie', 'Alex']
print(users)

users[1:3] = ['Rob', 'Justin']
print(users)

users.remove('Rob')
print(users)

print(users.pop())
print(users)

del users[1]
print(users)

del users[1]
print(users)

users[1:1] = ["Loren"]
print(users)

# del data
data.clear()
print(data)

users[1:1] = ['dave']
users.sort(key=str.lower) # include lowercase in correct alphabetical order
print(users)

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

nums.sort(reverse=True)
print(nums)

print(sorted(nums, reverse=True))

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

# Tuples

mytuple = tuple(('Loren', 42, True))

anothertuple = (1, 2, 3, 4, 2, 2)

print(mytuple)
print(anothertuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
newlist.append('Amanda')
newtuple = tuple(newlist)
print(newtuple)

(one, two, *hey) = anothertuple
print(one)
print(two)
print(hey)

print(anothertuple.count(2))

