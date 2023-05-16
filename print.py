# this file shows the different way sto use tyhe print function

a=10
b="ahmed"
c=True
d=20.45


print("Hello world")
#print(b + a) # produces error as b and a are not of the same type

print(b + str(a))

print("Hello world" , "  ",  a) # this one works no need to change a as we use , separator

print("Hello" , "World " , " from" , "Japan")

print("Hello" , "World " , " from" , "Japan", sep='+') # sep specifies the type of seprator used

print("Hello" , "World " , " from" , "Japan", sep=',')

print("Hello" , "World " , " from" , "Japan", sep='\n')
print("{0} is not the same as {1}".format(a,b) )

print("{1} is not the same as {0}".format(a,b) )

print("{} is not the same as {}".format(d,c) )


print("we entered %d , and %d"%(a,d)) # %d for numbers %s for stings %f for floats , %.<number of digits after the dot in a float> , %.2f displays 2 digits after dot
                                    #%x or %X for hex representation , 

print(r"Ahmed is \n not a bad boy ")

print(" We are not qouting \"This is a good thing\" we are not saying so ")

print(r" We are not qouting \"This is a good thing\" we are not saying so ")

print("Hi" + " there")
print(d , a)
print(d , end =", ") 
print(a)

print(d , end ="  ")
print(a)
print(a , d , end=",")
print("{0} is not the same as {1}".format(a,b) )


print("Hello World " , end="\b") #\b acts like a backspace we can add as many \b as we want
print("This is ny rules")


print("Hello World " , end="\r") #\r removes the text of first print
print("This is ny rules")

username='Alan'
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
subtotal = ${sub_total:>9,.2f} 
sales tax = ${sales_tax:<9,.2f}
total =  ${total:^,.2f}"""

print(output)

s_subtotal= "$" + f'{sub_total:,.2f}'
s_salestax="$" + f'{sales_tax:,.2f}'
s_total= "$" + f'{total:,.2f}'

output1= f"""
subtotal = ${s_subtotal:>9} 
sales tax = ${s_salestax:>9}
total =  ${s_total:>9}"""

print(output1)




#**********************************************************************************************

sourcefile= open("print.txt","w")
print("Wellcome from print command to this file directly using file attribute", file=sourcefile) # file attribute in print
sourcefile.close()
#**********************************************************************************************
import time
print("Hello World", end=" ") # hello world is printed then after 5 seconds bye is printed on the same line.
time.sleep(5)
print("Bye")

print("Hello World", end=" ", flush=True) 
time.sleep(5)
print("Bye")

for i in range (10):
    print(i, end= ' ' , flush=True)
    time.sleep(5)

for i in range (10):
    print(i, end= ' ' , flush=False)
    time.sleep(5)
    

