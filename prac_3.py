import time
from colorama import init, Fore, Style

init(autoreset=True)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(position - 1):
            if temp is None:
                raise IndexError("Invalid position entered.")
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    def delete_node_by_value(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return

        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            return

        prev.next = temp.next
        temp = None

    def delete_node_by_index(self, position):
        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            return

        for _ in range(position - 1):
            temp = temp.next
            if temp is None or temp.next is None:
                raise IndexError("Invalid position entered.")

        next_node = temp.next.next
        temp.next = None
        temp.next = next_node

    def display_list(self):
        temp = self.head

        if temp is None:
            print(Fore.RED + "No elements present in the linked list.")
            return

        print(Fore.GREEN + "\nCurrent Linked List:")
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def display_menu():
    print("\n" + Style.BRIGHT + "===== LINKED LIST MENU =====")
    print("1. " + Fore.YELLOW + "Add Node at Beginning")
    print("2. " + Fore.YELLOW + "Add Node at End")
    print("3. " + Fore.YELLOW + "Add Node at Specific Position")
    print("4. " + Fore.YELLOW + "Remove Node by Value")
    print("5. " + Fore.YELLOW + "Remove Node by Position")
    print("6. " + Fore.YELLOW + "View Linked List")
    print("7. " + Fore.RED + "Quit Program")


def main():
    linked_list = LinkedList()

    while True:
        display_menu()

        try:
            choice = int(input(Style.RESET_ALL + "\nSelect an option: "))

            if choice == 1:
                data = int(input("Enter the value to add: "))
                linked_list.insert_at_beginning(data)
                print(Fore.GREEN + "Node added successfully at the beginning.")

            elif choice == 2:
                data = int(input("Enter the value to add: "))
                linked_list.insert_at_end(data)
                print(Fore.GREEN + "Node added successfully at the end.")

            elif choice == 3:
                data = int(input("Enter the value to add: "))
                position = int(input("Enter the position (starting from 0): "))
                linked_list.insert_at_position(data, position)
                print(Fore.GREEN + f"Node inserted successfully at position {position}.")

            elif choice == 4:
                data = int(input("Enter the value to remove: "))
                linked_list.delete_node_by_value(data)
                print(Fore.RED + "Deletion operation completed.")

            elif choice == 5:
                position = int(input("Enter the node position to remove: "))
                linked_list.delete_node_by_index(position)
                print(Fore.RED + f"Node at position {position} removed successfully.")

            elif choice == 6:
                linked_list.display_list()

            elif choice == 7:
                print(Style.RESET_ALL + "Program terminated successfully.")
                break

            else:
                print(Fore.YELLOW + "Please select a valid menu option.")

        except ValueError:
            print(Fore.YELLOW + "Invalid input! Please enter numeric values only.")

        except IndexError as e:
            print(Fore.RED + f"Error: {str(e)}")

        except Exception as e:
            print(Fore.RED + f"Unexpected Error: {str(e)}")

        time.sleep(1)


if __name__ == "__main__":
    main()
