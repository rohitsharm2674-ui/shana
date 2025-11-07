'''GROUP A : ASSIGNMENT 3

Name - Divya Shivaji Bargal     Div-A      Roll No- 15

PROBLEM STATEMENAT :In a company, employee salaries are stored in a list as floating-point numbers. Write a
Python program that sorts the employee salaries in ascending order using the following two
algorithms:
• Selection Sort: Sort the salaries using the selection sort algorithm.
• Bubble Sort: Sort the salaries using the bubble sort algorithm.
After sorting the salaries, the program should display top five highest salaries in the company
'''


salary=[]
size=int(input("Enter the array size:"));
for i in range(0,size):
  ele=float(input("Enter the element:"));
  salary.append(ele)
  
def bubble_sort(salary):
 salary_sort=salary.copy()
 n=len(salary_sort)
 for i in range(0,n):
  for j in range(0,n-i-1):
   if(salary_sort[j] > salary_sort[j+1]):
    temp1 = salary_sort[j]
    salary_sort[j] = salary_sort[j+1]
    salary_sort[j+1] = temp1
 
 print("sorted salary:",salary_sort)
 print("top 5 salaries are :",salary_sort[-1:-6:-1])
 
def selection_sort(salary):
  salary_sort=salary.copy()
  n=len(salary_sort)
  for i in range(0,n-1):
    for j in range(i+1,n):
     if(salary_sort[i] > salary_sort[j]):
      temp = salary_sort[i]
      salary_sort[i] = salary_sort[j]
      salary_sort[j] = temp
    
  print("sorted salary:",salary_sort)
  print("top 5 salaries are :",salary_sort[-1:-6:-1])   
 
  
def menu():
   print("=====menu====")
   print("1. Bubble sort")
   print("2. selection sort")
   print("3. Exit")
while True:
   menu()
   choice=int(input("Enter your choice(1-3)"))
   if choice == 1 :
     sorted_bubblesort=bubble_sort(salary)
     print("sorted bubble sort is",sorted_bubblesort)
   elif choice == 2 :
     sorted_selectionsort=selection_sort(salary)
     print("sorted selection sort is",sorted_selectionsort)
   elif choice == 3 :
     print("Exit")
     break;
   else:
     print("Invalid choice")
     
 
 ''' OUTPUT
 gescoe@gescoe-OptiPlex-3020:~/Desktop/SE-A15$ python3 sort.py
Enter the array size:5
Enter the element:23
Enter the element:65
Enter the element:87
Enter the element:56
Enter the element:12
=====menu====
1. Bubble sort
2. selection sort
3. Exit
Enter your choice(1-3)1 
sorted salary: [12.0, 23.0, 56.0, 65.0, 87.0]
top 5 salaries are : [87.0, 65.0, 56.0, 23.0, 12.0]
sorted bubble sort is None
=====menu====
1. Bubble sort
2. selection sort
3. Exit
Enter your choice(1-3)2
sorted salary: [12.0, 23.0, 56.0, 65.0, 87.0]
top 5 salaries are : [87.0, 65.0, 56.0, 23.0, 12.0]
sorted selection sort is None
=====menu====
1. Bubble sort
2. selection sort
3. Exit
Enter your choice(1-3)3
Exit '''