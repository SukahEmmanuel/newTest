#Write a function common_elements that takes two lists of numbers as input. 
# The function should use a set to efficiently find and return a new list containing all elements that 
# are present in both of the input lists.

def common_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1.intersection(set2)
    return list(common)

userInput1 = input("Enter a list of numbers separated by commas: ")
userInput2 = input("Enter another list of numbers separated by commas: ")
myList1 = list(map(int, userInput1.replace(" ", "").split(",")))
myList2 = list(map(int, userInput2.replace(" ", "").split(",")))
print(f"The common elements in the two lists are: {common_elements(myList1, myList2)}")