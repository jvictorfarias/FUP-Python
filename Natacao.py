comp1 = float(input())
comp2 = float(input())
comp3 = float(input())

if(comp1 is comp2 and comp2 is comp3):
    print("comp1comp2comp3")
if(comp1 > comp2 and comp1 > comp3):
    if(comp2 > comp3):
        print("comp1\ncomp2\ncomp3")
    elif(comp3 > comp2):
        print("comp1\ncomp3\ncomp2")
    else:
        print("comp1\ncomp2comp3")
elif(comp1 is comp2 or comp1 is comp3):
    if(comp1 is comp2 and comp1 > comp3):
        print("comp1comp2\ncomp3")
    else:
        print("comp3\ncomp1comp2")




elif(comp2 > comp1 and comp2 > comp3):
    if(comp1 > comp3):
        print("comp2\ncomp1\ncomp3")
    elif(comp3 > comp1):
        print("comp2\ncomp3\ncomp1")
    else:
        print("comp2\ncomp1comp3")
elif(comp2 is comp3 or comp2 is comp1):
    if(comp2 is comp3 and comp2 > comp1):
        print("comp2comp3\ncomp1")
    else:
        print("comp")
