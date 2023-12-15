import random
import numpy as np
import matplotlib.pyplot as plt


num_throws = 10000

dice_eyes={1:0,2:0,3:0,4:0,5:0,6:0}

dice_eyes.fromkeys

print (dice_eyes.keys())
print (dice_eyes.values())
print(dice_eyes.get(2))

for throw in range(num_throws):
    dice_roll = random.randint(1,6)

    print('the dice rolled:', str(dice_roll))
    dice_eys_retrieved=dice_eyes.get((dice_roll))
    print("dice eyes retrieve::"+str(dice_eys_retrieved))

    #print ('number of same dice-eyes rolled before:', dice_eyes.get(dice_roll))
    dice_eyes[dice_roll]= dice_eys_retrieved+1
    #print ('NEW  NEW NEW number of same dice-eyes rolled before:', dice_eyes.get(dice_roll))
   

print(dice_eyes)

#now plotting the date
n_groups = 6
index = np.arange(n_groups)
bar_width = 0.35

rects1 = plt.bar(dice_eyes.keys(), dice_eyes.values(), bar_width, alpha=0.4, color='b', label='DiceThrows')

plt.xlabel('Dice Eyes')
plt.ylabel('Scores')
plt.title('Dice rolls by number')
plt.legend()

plt.show()