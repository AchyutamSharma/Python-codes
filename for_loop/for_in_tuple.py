# 1 - for loop in one line

[(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# output :- [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


# 1st and 2nd are same code but it use one line of code 
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            combs.append((x,y))
 combs
# output:- [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]


# --------- New program --------
vec = [-4,-2,0,2,4]
# create a new list with the value double
[x*2 for x in vec] # output:-  [-8,-4,0,4,8]

#               -------new for-------
#filter the list to exclude negative numbers
[x for x in vec if x>=0] # output:- [0,2,4]

#if apply a func (e.g. abs()) to all the elements
[abs(x) for x in vec] # output :- [4, 2, 0, 2, 4]

#           ---------- New -------

#call a method(e.g. strip()) on elements

freshfruit = ['banana','loganberry','passion fruit']
[weapon.strip() for weapon in freshfruit]

#           ---------- New -------

freshfruit = ['xbanana_','xyz_loganberry','10passion fruits']
[weapon.strip('_ . 5 10 x xyz') for weapon in freshfruit]
# output :- ['banana', 'loganberr', 'passion fruits']

# -----     new ------

# Till 5 create a list of 2-tuples like (number,square)
[(x,x**2) for x in range(6)]
#[(0,0),(1,1),(2,4),(3,9),(4,16),(5,25)]


# [x,x**2 for x in range(6)] # without parenthesized it through error

# output :- [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]

