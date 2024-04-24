# A handful of sorting algorithms I made for practice with things

# Insertion sort
'''
An insertion sort builds a sorted list to the left of the unsorted part.
It works by taking the first unsorted element, and iterating through the
sorted portion until it finds the right place in the list. It then
places it there in the sorted list and moves on to the next item.
'''
def insertion(list):
    # Go through each item in the list, except the first
    for i in range(1,len(list)):
        # Go through all the items up until the one we're looking at
        for j in range(i-1):
            # Find the point where it fits in
            if list[i] < list[j]:
                # Insert it there, removing the original, and break the `for j` loop
                list.insert(j, list.pop(i))
                break
    return list

# Bubble sort
'''
A bubble sort involves taking each item and comparing it with the next
item in the list. If the item on the left of the two is bigger, it swaps
them. It repeats through the list many times until no swaps are made, in
which case it is sorted.
'''
def bubble(list):
    # Needs multiple passes, so we use this to keep track on whether a pass does something
    sorted = False
    # Repeat until a pass does nothing
    while not sorted:
        # Assume a pass does nothing
        sorted = True
        # Go through all items in the list, except the last
        for i in range(len(list)-1):
            # Check if it's bigger than the one after it
            if list[i] > list[i+1]:
                # If it is, the list hasn't finished sorting after this pass
                sorted = False
                # Swap the two items
                list.insert(i, list.pop(i+1))
    return list

# Selection sort
'''
A selection sort involves finding the largest element in the unsorted
list, and moving it to the start of the list. Then, the next time it
looks for the largest item, it finds the 2nd largest as the largest has
already been moved out of the unsorted list. It then puts this at the
start, which is just before the item bigger than it. It does this for
each item in the list, and at the end, the unsorted list is empty.
'''
def selection(list):
    # Go through all of the items in the list
    for i in range(len(list)):
        # We'll be keeping track of the biggest item in the list
        # here. This sets it (back) to a null state
        biggest = -1
        # Go through all the items, starting from the first that isn't sorted
        for j in range(i,len(list)):
            # Check that `biggest` isn't null
            if biggest != -1:
                # Compare with the biggest
                if list[j] > list[biggest]:
                    # If it's bigger, make it the new biggest
                    biggest = j
            else:
                # Currently, nothing's the biggest, so let's use the first item to set a starting point
                biggest = j
        # Put the biggest unsorted item at the start
        list.insert(0,list.pop(biggest))
    return list

# Fake python shell if ran directly
if __name__ == "__main__":
    while True:
        print("Sorting ready")
        print(eval(input(">>> ")))