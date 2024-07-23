k = [1, 12, 15, 1]
h = k[2::-1]
print(h)

 
# k = [1, 12, 15, 1] initializes the list k with four elements.
#h = k[2::-1] slices the list k from index 2 down to index 0 in reverse order.
#k[2::-1] means start at index 2 (15), and go backwards one step at a time until you reach index 0 (1).
#The slice k[2::-1] includes the elements at indices 2, 1, and 0, in that order.
#print(h) outputs the resulting list.