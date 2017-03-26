
"""
#Lists
#values ALWAYS start with 0
#values always end with -1 and can go backwards from -1
#ex "java" is 2 and -1 or "c" is 1 and -2 or python is 0 or -3
#always make list variables end with "s"
three_giants=['python' , 'c' , 'java']
print(three_giants[0])
print(three_giants[1])
print(three_giants[-1])
state1='A nice programmming language is'
print(state1+' '+three_giants[0]+'.')
print(state1+' '+three_giants[1]+'.')
print(state1+' '+three_giants[-1]+'.')
"""

#random note= \n makes it go down a line in output/console and "\" nullifies anything

"""
#Inside and out side loops
#this is a for loop, it justs prints everythin in the [] 
#you must remove the last letter of the list variable to make temp. placeholder
#for lets python know u will make a ___ loop (for this instance "for")
three_giants=['python' , 'c' , 'java']
for three_giant in three_giants:
	print('I'+' love '+three_giant+'!')
	print('No I absolutely love '+three_giant+'.\n')

print("\nI guess I love \'em all guys.")
"""


"""
#Enumerated Lists
#index numbers the lists by value 
#make index a string so u can print it (add +1 to index to start with one)
#enumerate the variable "programs" so it actually numbers the output
programs=['python' , 'c' , 'java']
print("The best programs in order:\n")
for index, program in enumerate(programs):
	place= str(index+1)
	print(place+"st Place: "+ "Program: "+ program)

print("\nThat was a tough race folks")	
"""

#Note to self I left off at http://introtopython.org/lists_tuples.html#Exercises --3/8/17


"""
#Modifying an element
#just put variable name and value in [] and make it equal something eles
programs=['python' , 'c' , 'java']
programs[1]='c++'
print(programs) 
#Finding Element Position
#(programs.index(list-item)) finds the value of the item
print(programs.index('python'))
#Checking if item is in the list
print('python' in programs) #this is true
print('php' in programs) #this is false
"""


"""
#Appending, Inserting, and Removing
programs=['python' , 'c' , 'java']
programs.append('php')# adds to the end
print(programs)
programs.insert(0,'c++')#adds to specified value area 
programs.remove('php')#removes items from list
print(programs)
"""


"""
I know I didn't do alot to day but i want to complete some more IXL's
So below is where i left off
http://introtopython.org/lists_tuples.html#Creating-an-empty-list 
--3/9/17
"""


"""
#Creating Empty List and adding items to the list
humans=[]
humans.append('Danielle')
humans.append('Michelle')
humans.append('Kofi')
for human in humans:
	print('Welcome to python '+human+'.')

print('Welcome to the Google Pittsburgh Office '+ humans[-1]+'!\n')
print('Ya know what... leave '+humans[0]+' and '+humans[1]+'.')
"""
#Left off at same place 


"""
#Sorting
humans=['Danielle', 'Michelle','Kofi']
humans.sort() # it has to be before the for loop
for human in humans:
	print(human)

humans.sort(reverse=True)
for human in humans:
	print(human)
	humans.reverse()
	print(human)
human_count=len(humans) #len() counts how many items are in a list
print(human_count)
#you could also do >>>for human in sorted(humans): for a sorted list
#as well as >>>for human in reversed(humans): for a reversed list
"""


"""
#Sorting Numerical Lists
numbers=[8,2,4,9,6]
for number in sorted(numbers):#Numbers that are increasing
	print(number)

print('')#empty line

for number in sorted(numbers, reverse=True):#decreasing
	print(number)

print('')

for number in reversed(numbers):# reversed original
	print(number)

print('')

numbers.sort()#permanently sorted
print(numbers)

print('')

numbers.reverse()#permanently reversed(in this case reversed increasing or decreasing) 
print(numbers)
"""

"""
Exercise Instructions
Working List 

Make a list that includes four careers, such as 'programmer' and 'truck driver'.
Use the list.index() function to find the index of one career in your list.
Use the in function to show that this career is in your list.
Use the append() function to add a new career to your list.
Use the insert() function to add a new career at the beginning of the list.
Use a loop to show all the careers in your list.

Starting From Empty

Create the list you ended up with in Working List, but this time start your file with an empty list  
and fill it up using append() statements.
Print a statement that tells us what the first career you thought of was.
Print a statement that tells us what the last career you thought of was.

Ordered Working List

Start with the list you created in Working List.
You are going to print out the list in a number of different orders.
Each time you print the list, use a for loop rather than printing the raw list.
Print a message each time telling us what order we should see the list in.
Print the list in its original order.
Print the list in alphabetical order.
Print the list in its original order.
Print the list in reverse alphabetical order.
Print the list in its original order.
Print the list in the reverse order from what it started.
Print the list in its original order
Permanently sort the list in alphabetical order, and then print it out.
Permanently sort the list in reverse alphabetical order, and then print it out.

Ordered Numbers

Make a list of 5 numbers, in a random order.
You are going to print out the list in a number of different orders.
Each time you print the list, use a for loop rather than printing the raw list.
Print a message each time telling us what order we should see the list in.
Print the numbers in the original order.
Print the numbers in increasing order.
Print the numbers in the original order.
Print the numbers in decreasing order.
Print the numbers in their original order.
Print the numbers in the reverse order from how they started.
Print the numbers in the original order.
Permanently sort the numbers in increasing order, and then print them out.
Permanently sort the numbers in descreasing order, and then print them out.

List Lengths

Copy two or three of the lists you made from the previous exercises, or make up two or three new lists.
Print out a series of statements that tell us how long each list is
"""
"""
#Working List Exercise
careers=['programmer','fast food worker','teacher','factory worker']
print(careers.index('fast food worker'))
print(careers[1])
careers.append('truck driver')
careers.insert(0,'information tech')
for career in careers:
	print(career)
"""
"""
#Starting From Empty Exercise
careers=[]
careers.insert(0,'information tech')
careers.append('programmer')
careers.append('fast food worker')
careers.append('teacher')
careers.append('factory worker')
careers.append('truck driver')
print('My first career choice was'+' '+careers[0]+'.')
print('My final career choice was '+careers[1]+'.')
"""
"""
#Ordered Working List Exercise
careers=['information tech','programmer','fast food worker','teacher','factory worker','truck driver']
for career in careers:#original
	print(career)
print("This is an original list.")

print('')#empty line

for career in sorted(career=s):#alphabetical/sorted
	print(career)
print("This is an alphabetical/sorted list.")

print('')

for career in careers:#original again
	print(career)
print("This is another original list.")

print('')

for career in sorted(careers,reverse=True):#reversed alphabetical
	print(career)
print("This is a reversed alphabetical list.")

print('')

for career in careers:#original again
	print(career)
print("This another original list.")

print('')

for career in reversed(careers):#reversed original
	print(career)
print("This is a reversed original list.")

print('')

careers.sort()#Permanent Alphabetical List
for career in careers:
	print(career)
print("This is a permanentaly alphabetical list.")
careers=['information tech','programmer','fast food worker','teacher','factory worker','truck driver']
print('')

careers.reverse()# this changes the previous permanent alphabetical status into Reversed Alphabetical Order
for career in careers:
	print(career)
print("This is a permanent reversed alphabetical list.")
"""
"""
#Ordered Numbers Exercise
numbers=[8,2,4,9,6]

for number in numbers:
	print(number)
print('This is an original numerical list.')

print('')

for number in sorted(numbers):
	print(number)
print('This is an increasing numerical list.')

print('')

for number in numbers:
	print(number)
print('This is another original numerical list.')

print('')

for number in sorted(numbers, reverse=True):
	print(number)
print('This is a decreasing numerical list.')

print('')

for number in numbers:
	print(number)
print('This is the final original numerical list.')

print('')

numbers.sort()
for number in numbers:
	print(number)
print('This is a permanent increasing numerical list.')

print('')

numbers.reverse()
for number in numbers:
	print(number)
print('This is a permanent decreasing list')
"""
"""
#List Lengths
careers=['information tech','programmer','fast food worker','teacher','factory worker','truck driver']
numbers=[8,2,4,9,6]
humans=['Danielle','Michelle','Kofi']

career_coun=len(careers)
career_count=str(career_coun)
number_coun=len(numbers)
number_count=str(number_coun)
human_coun=len(humans)
human_count=str(human_coun)

print('The list "careers" is '+ career_count +' words long.')

print('')

print('The list "numbers" is '+ number_count +' numbers long.')

print('')

print('The list "humans" is '+ human_count +' words long.')
"""
#What to do after Exercises http://introtopython.org/lists_tuples.html#Removing-Items-from-a-List


"""
#Removing Items
humans=['Kofi','Danielle','Michelle']

del humans[-1]#del deletes the item of that position
print(humans)

more_humans=['Edenilson','Soje','Tim']

more_humans.remove('Edenilson')#.remove() deletes the value
print(more_humans)

letters=['a','b','a','c','d']

letters.remove('a')#if there are more than one of the same value, it deletes the first one
print(letters)
"""
#Left off at http://introtopython.org/lists_tuples.html#Popping-items-from-a-list