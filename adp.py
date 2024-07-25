def power(n,bp):
    #bp="093212"
    bp=[int(char) for char in bp]
    bp.sort(reverse=True)
    #print(bp)
    total=sum(bp)
    #print(total)
    d=0
    c=total 
    for power in bp:
        d=d+power 
        c=total-power 
        if d>c:
            break 
    return d 
n = int(input("Enter the number of people in the town: "))
blood_powers = input("Enter the blood powers as a string: ")
print(power(n,blood_powers))

'''
Stephan is a vampire. And he is fighting with his brother Damon. Vampires get energy from human bloods, so they need to feed on human blood, killing the human beings. Stephan is also less inhuman, so he will like to take less life in his hand. Now all the people’s blood has some power, which increases the powers of the Vampire. Stephan just needs to be more powerful than Damon, killing the least human possible. Tell the total power Steohan will have after drinking the bloods before the battle.
Note that: Damon is a beast, so no human being will be left after Damon drinks everyone’s blood. But Stephan always comes early in the town.

Input Format :
First line with the number of people in the town, n.
Second line with a string with n characters, denoting the one digit power in every blood.
adp company
'''
