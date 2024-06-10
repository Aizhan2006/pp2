#1
txt="Hello World"
x=txt[0]

#2
txt="Hello World"
x=txt[2:5]

#3
txt=" Hello World "
txt=txt.strip()

#4
txt="Hello World"
txt=txt.upper()

#5
txt="Hello World"
txt=txt.lower()

#6
txt="Hello World"
txt=txt.replace("H","J")

#7
age=36
txt="My name is John, and I am {}"
print(txt.format(age))
