def find_duplicates(sampleList):
    seen = set()
    duplicates = set()
    for item in sampleList:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

userInput = input("Enter a list of numbers separated by commas: ")
# Convert the input string into a list of integers and then into a list
myList = list(map(int, userInput.replace(" ", "").split(",")))
print(f"The duplicates in the list are: {find_duplicates(myList)}")
