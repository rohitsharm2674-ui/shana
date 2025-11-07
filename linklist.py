class StudentNode
	def __init__(self,rollno,name,marks):
		self.rollno=rollno
		self.name=name
		self.marks=marks
		self.next=None
class studentlinklist
	def __init__(self):
		self.head=None

	def add_students(self,rollno,name,marks):
		new_node=StudentNode(rollno,name,marks)
		if self.head=None:
			self.head=new_node
		else:
			current=self.head
			while current.next:
				current=current.next
			current.next=new_node
		print("===Student Record Added Succesfully===")

	def delet_students(self,rollno):
		current=self.head
		prev=None
		while current:
			if current.rollno=rollno:
				if prev:
					prev.next=current.next
				else:
					self.head=current.next
				print("===Student Record Deleted Succesfully===")
			prev=current
			current=current.next
		print("===Student Not Found===")

	def update_students(self,rollno,new_name,new_marks):
		current=self.head
		while current:
			if current.rollno=rollno
				current.name=new_name
				current.marks=new_marks
				print("===Student Record Updated Succesfully===")
				return
		print("==Student Not Found===")

	def search_students(self,rollno)
		current=self.head
		while current:
			if current.rollno=rollno:
				print(f"Found Roll Number{current.rollno} Name{current.name} Marks{current.marks}")
				return
			current=current.next
		print("Student Record Not Found")

	def display_students(self, sort="rollno", ascending=True):
		students = []
		current = self.head
		while current:
			students.append((current.roll_no, current.name, current.marks))
			current = current.next
		if sort=="roll no"
			students.sort(key=lambda x: x[0], reverse=not ascending)
		else sort=="marks"
			students.sort(key=lambda x: x[2], reverse=not ascending)
		if not students:
			print("===No Record Display===")
			return
		print("===Student Record===")
		for s in students:
			print(f\"Roll No: {s[0]}, Name: {s[1]}, Marks: {s[2]}")
