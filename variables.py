import math

num=20
print(num.as_integer_ratio())

num1=15.56
print(num1.as_integer_ratio())

x=4.5
print(x.as_integer_ratio())
# print(dir(num1))

print(num.bit_count())


print(num.bit_length())

# print(num.__dir__())


x=40
y=-50
z=4.14
l=3.5
s="   "
print(abs(y))
print(bin(x))
print(float(x))



print(math.factorial(x))


username="Alan"

print(f"Hello {username}")

unit_price=49.99
quantity=30

print(f"sub total :  ${quantity * unit_price: ,.2f}")

tax=.065
print(f"Tax rate is  {tax:.2%}")

sample1= f'Sales tax rate {tax:.2%}'
sample2= f"Sales tax rate {tax:.2%}"
sample3=f"""Sales tax rate {tax:.2%}"""
sample4=f'''Sales tax rate {tax:.2%}'''

print(sample1)

sub_total= quantity * unit_price
sales_tax=tax * sub_total

total =sub_total + sales_tax
# with triple quotation we can use enter to have a new line instead of \n. For other qutations to have a new line use \n
output= f"""
subtotal = ${sub_total: ,.2f} 
sales tax = ${sales_tax: ,.2f}
total =  ${total: ,.2f}"""

print(output)


x=255

print(hex(x))
print(oct(x))
print(bin(x))

print(0b11111111)
print(0o377)
print(0xff)

#*******************************************************************************************************************************************************************

# String varaibles

name= "Ahmed"
mid="Atef"
last="Abdelghaffar"

full= name+" " + mid + " " + last
print(full)

print(len(name))

s= "Abracadabra Hocus Pocus you're a turtle dove"
print(len(s))
# print("t" in s)
# print("T" in s)
# print("T" not in s)
# print("-" * 15)
# print(s[0])
# print(s[33:39])
# print(s[0:44:3])
# print(min(s))
# print(max(s))
# print(s.index("P"))
# print(s.index("o",22,44))
# print(s.count("a"))
# print(ord("A"))

print(s.capitalize())
print(s.count("o", 3,30))
print(s.find("y", 20,39))
print(s.find("y", 25,39))  # if -1 is returned this means the string is not found
print(s.index("P", 6,30))
# print(s.index("P", 25,39))
age=24
print(s.format(age))

print(s.casefold())
