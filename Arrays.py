#Write a python program that do the following:

#- display the initial content of the array
#- display a menu of options
#- allow user to select item in the menu (check if valid)
#- perform the selected option (you may prompt additional info to user when need)
#- display the resulting values of the array


#Note: 
#- The program has an array variable containing 10 random numbers
#- You may add other options and features
#- Your program should be uploaded to github before 1:30pm
#- Record a demo presenting your program
#- Send the demo directly to my messenger

#Example Output:

#Array: [1, 4, 3, 4, 4, 5, 6 ,2 ,56, 200]
#Menu:
# 1 -> Add an element
# 2 -> Insert an element
# 3 -> Modify an element
# 4 -> Delete an element
# 5 -> Arrange in ascending order
# 6 -> Arrange in descending order
#What do you want to do? (1-6): 4
#Enter the index you want to delete: 3
#The element has been deleted
#This is the new array: Array: [1, 4, 3, 4, 5, 6 ,2 ,56, 200]


list = [1, 16, 7, 3, 29, 4, 22, 15, 6, 20]

def menuList():
    print("Menu:")
    print(" 1 -> Add an element")
    print(" 2 -> Insert an element")
    print(" 3 -> Modify an element")
    print(" 4 -> Delete an element")
    print(" 5 -> Arrange in ascending order")
    print(" 6 -> Arange in descending order")

    
def menu():
    askInput = int(input("What do you want to do? (1-6): "))
    num = askInput

#add element
    if num == 1:
        askInput = int(input("Insert a number: "))
        list.append(askInput)
        print("The number has been added to the list.")
        print(f'This is the New Array: Array: {list}')


#insert element
    elif num == 2:
        askInput = int(input('Insert the number you want to put: ' ))
        askIndex = int(input('Input the index where you want to add the number (0-9): '))
        numInput = askInput
        index = askIndex
        list.insert(index, numInput)
        print("The number has been inserted to the list.")
        print(f'This is the New Array: Array: {list}')


#modify an element
    elif num == 3:
        askInput = int(input('Insert the number you want to put: ' ))
        askIndex = int(input('Input the index where you want to add the number (0-9): '))
        numInput = askInput
        index = askIndex
        list[index] = numInput
        print("The number has been modified to the list.")
        print(f'This is the New Array: Array: {list}')


#delete an element
    elif num == 4:
        askInput = int(input('Insert the number you want to delete: ' ))
        numInput = askInput
        list.remove(numInput)
        print("The number has been deleted from the list.")
        print(f'This is the New Array: Array: {list}')


#arrange in ascending order
    elif num == 5:
        list.sort()
        print('The numbers in the list are now arranged in ascending order')
        print(f'This is the New Array: Array: {list}')


#arrange in descending order
    elif num == 6:
        list.sort()
        list.reverse()
        print('The numbers in the list are now arranged in descending order')
        print(f'This is the New Array: Array: {list}')

    else:
        print("The number you've entered is out of range. Please run the program again and enter number from 1-6")

    



print(f"Array: {list}")
menuList()
menu()
