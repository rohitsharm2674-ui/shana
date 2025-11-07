'''GROUP B- ASSIGNMENT NO 1

Name- Divya Shivaji Bargal    Div-A    Rollno- 15

STATEMENT:Implementing a real-time undo/redo system for a text editing application using a Stack data
structure. The system should support the following operations:
• Make a Change: A new change to the document is made.
• Undo Action: Revert the most recent change and store it for potential redo.
• Redo Action: Reapply the most recently undone action.
• Display Document State: Show the current state of the document after undoing or
redoing an action
'''


class Texteditor:
  def  __init__(self):
    self.document =""
    self.Undo_stack=[]
    self.Redo_stack=[]
    
  def make_change(self, change):
    self.Undo_stack.append(self.document)
    self.document += change
    print("\n change made.")
    self.display_content()
    
  def Undo_action(self):
    if self.Undo_stack:
     self.Redo_stack.append(self.document)
     self.document=self.Undo_stack.pop()
     print(self.document)
    else:
     print("\n No more action to Undo")
     
  def Redo_action(self):
    if self.Redo_stack:
     self.Redo_stack.append(self.document)
     self.document=self.Redo_stack.pop()
     print(self.document)
    else:
     print("\n No more action to Redo")
     
  def display_content(self):
    print("The original document is:",self.document)
    
  def menu(self):
    while True:
     print("=====Menu=====")
     print("1.make a change")
     print("2.Undo")
     print("3.Redo")
     print("4.display")
     print("5.Exit")
     choice=int(input("Enter your choice:"))
     
     if choice==1:
      change=input("Text to be added:")
      self.make_change(change)
     elif choice==2:
      self.Undo_action()
     elif choice==3:
      self.Redo_action()
     elif choice==4:
      self.display_content()
     elif choice==5:
      print("Exit")
      
Editor=Texteditor()
Editor.menu()

'''OUTPUT
gescoe@gescoe-OptiPlex-3020:~/Desktop/SE-A15$ python3 stack.py 
=====Menu=====
1.make a change
2.Undo
3.Redo
4.display
5.Exit
Enter your choice:1
Text to be added:Happy

 change made.
The original document is: Happy
=====Menu=====
1.make a change
2.Undo
3.Redo
4.display
5.Exit
Enter your choice:1
Text to be added:Life

 change made.
The original document is: HappyLife
=====Menu=====
1.make a change
2.Undo
3.Redo
4.display
5.Exit
Enter your choice:2
Happy
=====Menu=====
1.make a change
2.Undo
3.Redo
4.display
5.Exit
Enter your choice:3
Happy
=====Menu=====
1.make a change
2.Undo
3.Redo
4.display
5.Exit
Enter your choice:4
The original document is: Happy
=====Menu=====
1.make a change
2.Undo
3.Redo
4.display
5.Exit
Enter your choice:5
Exit
'''