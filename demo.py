from random import randint
num = randint (1,10)
print "GUess what I think?"
bingo = False
while bingo == False:
    answer = input()
    if answer < num:
    	print "%d is too small!"%answer
    if answer > num:
    	print "%d is too big"%answer
    if answer == num:
    	print "BINGO!%d is What I think."%answer
    	bingo = True