'''GROUP A - ASSIGNMENT NO-2

Name- Divya Shivaji Bargal   Div-A      Roll No-15
 
 STATEMENT:In an e-commerce system, customer account IDs are stored in a list, and you are tasked with
writing a program that implements the following:
• Linear Search: Check if a particular customer account ID exists in the list.
• Binary Search: Implement Binary search to find if a customer account ID exists,
improving the search efficiency over the basic linear
'''

customer_ID=[]
size = int(input("Enter the size of customer ID:"))
for i in range(0,size):
   customer_ID.append(int(input("customer ID:")))

def Linear_search(customer_ID,target):
  for i in range(0,len(customer_ID)):
     if (target==customer_ID[i]):
       return i
       break
  return -1
      
def binary_search(customer_ID,target):
  low=0;
  high=size-1;
  
  while(low<=high):
        mid=(low+high)//2
        if (customer_ID[mid]==key):
          return mid
        elif (customer_ID[mid]<key):
            low=mid+1
        else:
            low=mid-1
  return -1
   
def menu():
  print("=====Menu=====")
  print("1.linear search")
  print("2.binary search")
  print("3.Exit")
  
while True:
  menu()
  choice=int(input("Ehter the choice (1-3)"))
  
  if (choice==1):
    key=int(input("enter the customer id to be searched"))
    res=Linear_search(customer_ID,key)
    if (res!=-1):
      print(f"customer id {key} found at location {res}")
    else:
      print(f"element not found")
   
  if choice==2:
   sort_ID=sorted(customer_ID)
   key=int(input("Enter the number to be search:"))
   res=binary_search(sort_ID,key)
    
   if res!=-1:
      print(f"customer id {key} found at location {res}")
   else:
      print(f"customer id {key} not found")
      
  if choice==3:
    break
  else:
    print("Exiting the loop")
 
 
''' OUTPUT
gescoe@gescoe-OptiPlex-3020:~/Desktop/SE-A15$ python3 search.py 
Enter the size of customer ID:5
customer ID:123
customer ID:765
customer ID:987
customer ID:546
customer ID:374
=====Menu=====
1.linear search
2.binary search
3.Exit
Ehter the choice (1-3)1
enter the customer id to be searched123
customer id 123 found at location 0
Exiting the loop
=====Menu=====
1.linear search
2.binary search
3.Exit
Ehter the choice (1-3)1
enter the customer id to be searched222
element not found
Exiting the loop
=====Menu=====
1.linear search
2.binary search
3.Exit
Ehter the choice (1-3)2
Enter the number to be search:546
customer id 546 found at location 2
Exiting the loop
=====Menu=====
1.linear search
2.binary search
3.Exit
Ehter the choice (1-3)3
Exit'''