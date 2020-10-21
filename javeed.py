

# def code():
#     print("we are coding python")
#     add()
# code()


# def cook(x,y):
#     print("cooking "+x+" & "+y+" Biryani")
#
# #cook("chicken")
# cook("chicken","mutton")

# def cook(type,cost):
#     print("cooking "+type+" Biryani")
#     print(cost,"rs")
# cook("chicken",180)
# cook("mutton",250)
#
# def add(x,y):
#     print(x+y)
# add(5,4)
#
#
# def cook(type,cost):
#     print("cooking"+type+"biryani")
#     print(cost,"rs")
#     return cost
# cost=cook("chicken",180)
# print("accessing cost outside",cost)
#
#
# def add(x,y):
#     print(x+y)
#     return x+y
# add(5,6)
# def sub(x,y):
#     print(x-y)
#     return x-y
# sub(6,7)
# def mul(x,y):
#     print(x*y)
#     return x*y
# mul(6,8)


# def coffee(*ingredients):
#     print(ingredients)
#     return "coffee"
# take=coffee("milk","sugar","powder","water","bowl")
# print(take)


# def areaOfTriangle(b,h):
#     res=(b*h)/2
#     return res
# area=areaOfTriangle(7,6)
# print("area of the triangle is",area)


def calculations(x, y, type):
     if type == "square":
        area = x * y
        print("area of the square",area)
        return area
     elif type == "rectangle":
        area = x * y
        print("area of the rectangle",area)
        return area
     elif type == "triangle":
         area =  (x*y)/2
         print("area of the taiangle" ,area)
         return area
     else:
         print("please give appropriate type")

calculations(4,5,"square")
calculations(4,5,"rectangle")
calculations(4,5,"triangle")


def calculations(x, y, type):
    if type == "noddels":
        price = x * y
        print("price of the noddels", price)
        return price
    elif type == "maggie":
        price = x//y
        print("price of the maggie", price)
        return price
    elif type == "egg rice":
        price = x + y
        print("price of the egg rice", price)
        return price
    else:
        print("please give appropriate type")
calculations(10,20,"maggie")
calculations(10,20,"egg rice")
calculations(10,20,"noddels")










