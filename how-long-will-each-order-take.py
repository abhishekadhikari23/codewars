'''
# 2019-08-16

        https://www.codewars.com/kata/how-long-each-order-will-take/

The pizza store wants to know how long each order will take. They know:

Prepping a pizza takes 3 mins
Cook a pizza takes 10 mins
Every salad takes 3 mins to make
Every appetizer takes 5 mins to make
There are 2 pizza ovens
5 pizzas can fit in a oven
Prepping for a pizza must be done before it can be put in the oven
There are two pizza chefs and one chef for appitizers and salads combined
The two pizza chefs can work on the same pizza
Write a function, order, which will tell the company how much time the order will take.

 order(3,1,2)=14.5

'''

def order(pizzas, salads, appetizers):
    pass
    prep = 0
    cook = 0
    salizer = 0
    if(pizzas%10 == 0):
        cook = (pizzas/10)*10
    else:
        cook = (int(pizzas/10)*10) + 10
    if(pizzas == 1):
        prep = 1.5
    elif(pizzas%2 == 0):
        prep = (pizzas/2)*3
    else:
        prep = (((pizzas-1)/2)*3)+1.5
    salizer = (salads*3) + (appetizers*5)
    if(salizer > (prep + cook)):
        return salizer
    else:
        return prep + cook
        
piz = int(input("Enter no. of pizzas     : "))
sal = int(input("Enter no. of salads     : "))
ape = int(input("Enter no. of appetizers : "))
print("Time taken for order = " + str(order(piz,sal,ape)))

'''By Abhishek Adhikari'''
