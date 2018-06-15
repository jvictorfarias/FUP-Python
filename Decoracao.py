string = raw_input()
indA = int(input())
indB = int(input())
if indA < len(string):
    print string[indA:indA + indB]
else:
    pass
