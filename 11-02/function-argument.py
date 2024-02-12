
firstname= input("Enter the first name:-")
#   default arguments

"""
def fullname(fname,mname = "kumar", lname = "Sharma"):
    print("Hey!! ",fname,mname,lname)

fullname(firstname)
"""

#   Keyword arguments:

mid_name = input("Enter the middle Name:- ")
last_name = input("Enter the last name:- ")

"""
def KeywordArguments(fname,midname,lastname):
    print("Hey!!",fname,midname,lastname)

KeywordArguments(firstname,mid_name,last_name)
"""


# Variable length arguments

# 1)Arbitrary Arguments:-                   {using tuple}
# 2)keyword Arbitrary Arguments:-           {using dictionary}

# 1)Arbitrary Arguments:-

'''
def name(*name):
    print("Hello,", name[0], name[1], name[2],name[3])

name(firstname,mid_name, last_name, "Or Kya haal")
'''


# 2)keyword Arbitrary Arguments:-           

def names(**name):
    print("Helloo,", name["fname"],name["mname"],name["lname"])

names(lname = last_name,fname = firstname,mname = mid_name)