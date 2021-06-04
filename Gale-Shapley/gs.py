import random

male = ['Ronaldo', 'Messi', 'Mbappe', 'Firmino', 'Ronaldiniho', 'Mane', 'Neymar', 'Arnold', 'Ribery', 'Pogba']
female = ['Vicki', 'Christen', 'Kate', 'Chloe', 'Brittany', 'Lilly', 'Love', 'Ariana', 'Zoey', 'Selina']
preferred_rankings_men = {}
preferred_rankings_women = {}
c = len(male)

# creating a random preferance list for our male partcipants
for i in range(c):
    for j in male:
        preferred_rankings_men[j] = random.sample(female, c)
print('Preferance rank of the males')
print('  ')  # space prinited to increase readability
for i, j in preferred_rankings_men.items():
    print(i, '----', j)
    print(' ')

# creating a random preferance list for our female participants
for i in range(c):
    for j in female:
        preferred_rankings_women[j] = random.sample(male, c)
print('Preferance rank of the females')
print('  ')  # space printed to increase readability
for i, j in preferred_rankings_women.items():
    print(i, '----', j)
    print(' ')

# Keep track of the people that "may" end up together
temporary_pairings = []

# Men who still need to propose and get accepted successfully
free_men = []


def init_free_men():
    # Initialize the arrays of women and men to represent
    # that they're all initially free and not engaged
    for man in preferred_rankings_men.keys():
        free_men.append(man)


def begin_matching(man):
    # Find the first free woman available to a man at
    # any given time

    # print("DEALING WITH {}".format(man))
    for woman in preferred_rankings_men[man]:

        # Boolean for whether woman is taken or not
        taken_match = [couple for couple in temporary_pairings if woman in couple]

        if (len(taken_match) == 0):
            # Temporarily engage the man and woman
            temporary_pairings.append([man, woman])
            free_men.remove(man)
            print('{} engaged to {}'.format(man, woman))
            break

        elif (len(taken_match) > 0):
            print('{} is taken already..'.format(woman))

            # Check ranking of the current dude and the ranking of the 'to-be' dude
            current_guy = preferred_rankings_women[woman].index(taken_match[0][0])
            potential_guy = preferred_rankings_women[woman].index(man)

            if (current_guy < potential_guy):
                print('She\'s satisfied with {}..'.format(taken_match[0][0]))
            else:
                print('{} is better than {}'.format(man, taken_match[0][0]))
                print('Making {} free again as he was dumped...engaging {} and {}'.format(taken_match[0][0], man, woman))

                # The new guy is engaged
                free_men.remove(man)

                # The old guy is now single
                free_men.append(taken_match[0][0])

                # Update the fiance of the woman (tentatively)
                taken_match[0][0] = man
                break


def stable_matching():
    # Matching algorithm until stable match terminates
    while (len(free_men) > 0):
        for man in free_men:
            begin_matching(man)


def main():
    init_free_men()
    print(free_men)
    stable_matching()
    print(' ') # print space for readability
    print('Final result of Stable Matching')
    print(' ')  # print space for readability
    for j in temporary_pairings:
        print(j[0],'-',j[1])


main()



