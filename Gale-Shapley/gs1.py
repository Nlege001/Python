#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Gale-Shapley Algorithm
#Created by: Naol Legesse
#Date: September 23/2020
#Purpose: To generate a stable matching for given items or people and their preferance
#Input : N number of male and N number of female participants with their respective preferances
#Output : a stable matching that couples the male and female participants based on their preferance
#Examples: This algorithim can be used in various selection processes and one is given below.



import time
import random
import sys


# This class is used to Implement the Gale-shapley Algrothim.
class Stable_Matching:
    def __init__(self):
        self.Temporary_man = dict()  # dictionary that stores men and their preferance list

        self.Temporary_woman = dict()  # dictionary that stores women and their preferance list

        self.Engaged = []  # list that stores engaged couples

        self.Free_men = []  # list for men that have no partners and are single, They need to propose

        self.Married = [self.Engaged]  # final list of couples that are suitable for each other

    def create_match(self, man):
        # This helps to get the woman from the man's preference list and create a match

        for w in self.Temporary_man[man]:
            # iterate through each (man,woman) pair in the engaged lisr and get the pair if the woman exists in it

            self.Married = [pair for pair in self.Engaged if w in pair]
            # if woman is not in the engaged list or if she's free
            if (len(self.Married) == 0):
                # engage m and w temporarily
                self.Engaged.append([man, w])
                self.Free_men.remove(man)
                return
            # if woman is in the engaged list and she already got a man
            elif (len(self.Married) != 0):

                Previous_male_partner = self.Married[0][0]
                # get the current fiance of woman and the new proposing
                # male by their preferance index.
                new_man_index = self.Temporary_woman[w].index(man)
                Current_fiance = self.Temporary_woman[w].index(Previous_male_partner)

                # Compare the indexes of the two and
                # pair up with the smaller index as that man is more preferred more by the female
                if (new_man_index < Current_fiance):
                    # remove the new man from free men list as he is now engaged to w
                    self.Free_men.remove(man)

                    # change the fiance of w in the paired up list
                    self.Married[0][0] = man
                    return

    # main function that takes command line arguments
    def main(self, argv):

        # create a random list of random men by using the range of integer from the command line.

        for i in range(0, int(sys.argv[1])):
            self.Temporary_man[i] = list(range(0, int(sys.argv[1])))
            random.shuffle(self.Temporary_man[i])  # random.shuffle is used

        # create a random list of random women by using the range of integer from the command line
        for j in range(0, int(sys.argv[1])):
            self.Temporary_woman[j] = list(range(0, int(sys.argv[1])))
            random.shuffle(self.Temporary_woman[j])  # random.shuffle is used

        # add the keys i.e the men in the dictionary of man_temp to the list called freeMenArray
        for m in self.Temporary_man.keys():
            self.Free_men.append(m)

        # This loop runs the actual matching
        # we measure the time taken by this algorithm
        t = time.time()
        while (len(self.Free_men) > 0):
            for man in self.Free_men:
                self.create_match(man)

        print('{} {}'.format(argv, time.time() - t))


if __name__ == '__main__':
    Stable_Matching().main(sys.argv[1])


# In[ ]:




