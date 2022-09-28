# Basic functions
x=2
y="Hello"
u=3.2
z=True

# Operations: exponents, divisions
print(2 ** 3)
print(4/2)

# If statements (and indentation)
x = 9
if x < 10 :
  print("it is lower than 10")
  print("DIJON")
else :
  print("It is higher than 10")
        
pass # only for displaying

# Loop statements
for i in [1,3,5] :
    print(i)
    
pass

# While loops
i=0
while i < 10:
    print(i)
    i+=1
pass

# Difference between Functions and Methods 

## a function is a piece of reusable code that performs a particular task.
round(3.15, 0)

## types and coercions (see https://jakevdp.github.io/PythonDataScienceHandbook/02.01-understanding-data-types.html#A-Python-Integer-Is-More-Than-Just-an-Integer)
type(x)
z=int(u)
type(z)

## sorting
a_unsorted = [88, 5, 7, 45]
a_sorted = sorted(a_unsorted, reverse = True)
print("this is unsorted ", a_unsorted, " and this is sorted ", a_sorted)

## Methods are functuions that apply to specific objects. these are called by object.method()
# useful methods (some)
biglist = ["A","B","C"]
biglist.append("D")
print(biglist)

# insert an object in a list
biglist.insert(0, "Z")
print(biglist)

# remove
biglist.remove("Z")
print(biglist)

# count
biglist.count("K")

# replace
r='SOAP'
r.replace("A", "U")

# Dictionaries

## Dictionaries are used to store data values in key:value pairs.

thisdict = {
  "brand": ["Ford","Citroen"],
  "model": ["Mustang","C3"],
  "year": [1964,2003]
}
print(thisdict)
