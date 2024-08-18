# Question 7: Generating Numbers from 1 to 100
# using array
array = [] 
for i in range(1, 101):
    array.append(i) # creating a list that contains integers from 1 to 100.
print(array) # print the array

# using linked list
# python doesn't have built-in functions for linked list.

from collections import deque
linked_list = deque(range(1, 101))
print(linked_list) #print the linked list

#Advantages of using array is most likely fast access to the elements 
# and disadvantages is size is fixed and insertion and deletions is expensive.

#Advantages of using linked list is size is dynamic. It can be resized according to needs
# and disadvantages is slower access time to the elements compared to arrays.