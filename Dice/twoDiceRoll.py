import random
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


def getHightestValueinDictionary(dict):
    
    maxValue = -1 #initialise max value with -1
    dictMaxValueKey = -1 #initialise  dictionary key associated with the maximum value
    #iterate through dictionary
    for k,v in dict.items():
        if v > maxValue:
            maxValue = v
            dictMaxValueKey = k

    print("max value" + str(maxValue))
    print("max key" + str(dictMaxValueKey))

    return [dictMaxValueKey,maxValue, 'hans']



num_throws = 1000

dice1={1:0,2:0,3:0,4:0,5:0,6:0}
dice2={1:0,2:0,3:0,4:0,5:0,6:0}

print (dice1.keys())
print (dice1.values())
print(dice1.get(2))

for throw in range(num_throws):
    dice1_roll = random.randint(1,6)
    print('the 1st dice rolled:', str(dice1_roll))
    dice2_roll = random.randint(1,6)
    print('the 2nd dice rolled:', str(dice2_roll))
    
    dice1_eys_retrieved=dice1.get((dice1_roll))
    print("dice1 eyes retrieve::"+str(dice1_eys_retrieved))
    dice2_eys_retrieved=dice2.get((dice2_roll))
    print("dice eyes retrieve::"+str(dice2_eys_retrieved))

    #print ('number of same dice-eyes rolled before:', dice_eyes.get(dice_roll))
    dice1[dice1_roll]= dice1_eys_retrieved+1
    dice2[dice2_roll]= dice2_eys_retrieved+1
    #print ('NEW  NEW NEW number of same dice-eyes rolled before:', dice_eyes.get(dice_roll))
   

print(dice1)
print(dice2)

key, value, name = getHightestValueinDictionary(dice1)
print("key1:"+ str(key))
print("value1:"+ str(value))
print("name1:"+name)
getHightestValueinDictionary(dice2)


index = dice1.keys()
bar1 = dice1.values()
bar2 = dice2.values()
df = pd.DataFrame({'Dice1': bar1, 'Dice2':bar2}, index=index)
ax = df.plot.bar(rot=0)

#now plotting the date
# n_groups = 6
# index = np.arange(n_groups)
# bar_width = 0.35

# ax = plt.subplot(111)
# ax.bar(dice1.keys(), dice1.values(), width=0.2, color='g', align='center')
# ax.bar(dice2.keys(), dice2.values(), width=0.2, color='r', align='center')


# plt.show()

# rects1 = plt.bar(dice1.keys(), dice1.values(), bar_width, alpha=0.4, color='b', label='DiceThrows')
# rects2 = plt.bar(dice2.keys(), dice2.values(), bar_width, alpha=0.4, color='b', label='DiceThrows')

# plt.xlabel('Dice Eyes')
# plt.ylabel('Scores')
# plt.title('Dice rolls by number')
# plt.legend()

plt.show()