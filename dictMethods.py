# clear

d1={
    "soap":'dove',
    'color':'white',
    'price':'40'
}
d1.clear()
print(d1)
print()
print('-----')
print()

# Clear : removes all elements from the dictionary.

# copy

d2={
     "pen":'cello',
    'color':'black',
    'price':'20'
}
x=d2.copy()
print(x)
print()
print('-----')
print()

# Copy : returns a copy of the dictionary.

# fromkeys

x=('a','b','c',)
y=10
thisdict=dict.fromkeys(x,y)
print(thisdict)
print()
print('-----')
print()

# Fromkeys : creates a dictionary from the given sequence of keys and a value.

# get

d3={
    'a1': 10,
    'b1': 20,
    'c1': 30
}
x=d3.get('b1')
print(x)
print()
print('-----')
print()

# Get : returns the value of the specified key.

# items

d4={
    'x1': 50,
    'y1': 100,
    'z1': 150
}
x=d4.items()
print(x)
print()
print('-----')
print()

# Items : returns a view object that displays a list of dictionary's key-value tuple pairs.

# keys

d5={
     "fruit":'mangos',
    'color':'yellow',
    'price':'100'
}
x=d5.keys()
print(x)
print()
print('-----')
print()

# Keys : returns a view object that displays a list of all the keys in the dictionary.

# values

d6={
     "vegitable":'potato',
    'shape':'oval',
    'price':'60'
}
x=d6.values()
print(x)
print()
print('-----')
print() 

# Values : returns a view object that displays a list of all the values in the dictionary.

# pop

d7={
    'name':'Sita',
    'add':'add1',
    'mob_no': 123456
}
d7.pop('name')
print(d7)
print()
print('-----')
print()

# Pop : removes the element with the specified key.

# popitem

d7={
    'stu':'Richa',
    'add':'add1',
    'sub':'english'
}
d7.popitem()
print(d7)
print()
print('-----')
print()

# Popitem : removes the last inserted key-value pair.

# setdefault

d8={
     "fruit":'kiwi',
    'color':'brown',
    'price':70
}
x=d8.setdefault('price',150)
print(x)
print()
print('-----')
print()

# Setdefault : returns the value of the specified key. If the key does not exist, inserts the key with the specified value.

# update

d9={
     "hair oil":'almond',
    'color':'light yellow',
    'price':200
}
d9.update({'color':'nutral'})
print(d9)
print()
print('-----')
print()

# Update : updates the dictionary with the specified key-value pairs.

