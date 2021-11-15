from random import choice as r

choices = ["A", "B", "C"]
results = []

a = 0
b = 0
c = 0

votes = int(input("How many votes do you want there to be? "))

for i in range(votes):
    vote = r(choices)
    results.append(vote)

for i in range(votes):
    if results[i] == "A":
        a += 1
    elif results[i] == "B":
        b += 1
    elif results[i] == "C":
        c += 1
    else:
        print("Yeah Tom you broke something")


if a == b == c:
    if a == 1:
        votess = "Vote"
    else:
        votess = "Votes"
    print("All the votes are tied with {} {} each".format(a, votess))

if a > b and a > c:
    if b > c:
        print("A had the most votes with {} votes followed by B with {} votes and C at the bottom with {} votes".format(a, b, c))
    elif c > b:
        print("A had the most votes with {} votes followed by C with {} votes and B at the bottom with {} votes".format(a, c, b))
    elif b == c:
        print("A had the most votes with {} votes followed by C and B all tied up with both {} votes each".format(a, b))

if b > a and b > c:
    if a > c:
        print("B had the most votes with {} votes followed by A with {} votes and C at the bottom with {} votes".format(b, a, c))
    elif c > a:
        print("B had the most votes with {} votes followed by C with {} votes and A at the bottom with {} votes".format(b, c, a))
    elif a == c:
        print("B had the most votes with {} votes followed by A and C all tied up with both {} votes each".format(b, a))

if c > a and c > b:
    if b > a:
        print("C had the most votes with {} votes followed by B with {} votes and A at the bottom with {} votes".format(c, b, a))
    elif a > b:
        print("C had the most votes with {} votes followed by A with {} votes and B at the bottom with {} votes".format(c, a, b))
    elif b == c:
        print("C had the most votes with {} votes followed by A and B all tied up with both {} votes each".format(c, a))

if a == b and a > c:
    print("A and B are tied on top with {} votes each and C is on bottom with only {} votes".format(a,c))
if a == c and a > b:
    print("A and C are tied on top with {} votes each and B is on bottom with only {} votes".format(a,b))
if b == c and b > a:
    print("B and C are tied on top with {} votes each and A is on bottom with only {} votes".format(b,a))