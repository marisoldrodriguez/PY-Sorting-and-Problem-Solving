# Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list in descending order (use the sorted() function).
# The sorted() function sorts in ascending order, but it can sort in descending order by adding a reverse parameter with a boolean value of True.

unsorted_lst = [7,5,3,2,6,1,4]
sorted_lst_desc = sorted(unsorted_lst, reverse=True)
print(sorted_lst_desc)