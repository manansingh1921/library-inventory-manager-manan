import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from library_manager.inventory import LibraryInventory

def main():
    lib = LibraryInventory()
    
    while True:
        print("\n--- Library Manager ---")
        print("1. Add Book")
        print("2. Issue Book") 
        print("3. Return Book")
        print("4. View All")
        print("5. Search")
        print("6. Exit")
        
        choice = input("Choice: ")
        
        if choice == '1':
            t = input("Title: ")
            a = input("Author: ")
            i = input("ISBN: ")
            lib.add_book(t, a, i)
            
        elif choice == '2':
            i = input("ISBN: ")
            print("Done" if lib.issue_book(i) else "Not found")
            
        elif choice == '3':
            i = input("ISBN: ")
            print("Done" if lib.return_book(i) else "Not found")
            
        elif choice == '4':
            for b in lib.display_all():
                print(b)
                
        elif choice == '5':
            t = input("Title: ")
            for b in lib.search_by_title(t):
                print(b)
                
        elif choice == '6':
            break

if __name__ == "__main__":
    main()
