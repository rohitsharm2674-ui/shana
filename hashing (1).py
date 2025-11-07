class LinearProbingHashing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insertion(self, key):
        index = self.hash_function(key)
        start_index = index

        while self.table[index] is not None and self.table[index] != "DELETED":
            if self.table[index] == key:
                print(f"Key {key} already exists in the hash table at index {index}.")
                return
            index = (index + 1) % self.size
            if index == start_index:
                print("Hash table is full, cannot insert key:", key)
                return

        self.table[index] = key
        print(f"Key {key} inserted at index {index}.")

    
                
    def display(self):
        print("\nHash Table:")
        for i, key in enumerate(self.table):
            print(f"Index {i}: {key}")
        print()

    def menudriven(self):
        while True:
            print("########## MENU ###########")
            print("1. Insert a key")
        
            print("2. Display the table")
            print("3. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                try:
                    key = int(input("Enter key to insert: "))
                    self.insertion(key)
                except ValueError:
                    print("Invalid input! Please enter an integer.")
        
                self.display()
            elif choice == '3':
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    obj = LinearProbingHashing()
    obj.menudriven()

