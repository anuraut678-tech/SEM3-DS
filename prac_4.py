import time
from colorama import init, Fore, Style

init(autoreset=True)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Invalid position entered.")
            temp = temp.next

        if temp is None:
            raise IndexError("Invalid position entered.")

        new_node.next = temp
        new_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = new_node

        temp.prev = new_node

    def delete_node_at_beginning(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_node_at_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next:
                temp = temp.next

            temp.prev.next = None

    def delete_node_at_position(self, position):
        if self.head is None:
            return

        temp = self.head

        for _ in range(position):
            if temp is None:
                raise IndexError("Invalid position entered.")
            temp = temp.next

        if temp is None:
            raise IndexError("Invalid position entered.")

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

    def display_list(self):
        temp = self.head

        if temp is None:
            print(Fore.RED + "No nodes available in the list.")
            return

        print(Fore.GREEN + "\nCurrent Doubly Linked List:")
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def search_node(self, key):
        temp = self.head

        while temp:
            if temp.data == key:
                return True
            temp = temp.next

        return False

    def length_of_list(self):
        temp = self.head
        count = 0

        while temp:
            count += 1
            temp = temp.next

        return count


def display_menu():
    print("\n" + Style.BRIGHT + "===== DOUBLY LINKED LIST MENU =====")
    print("1. " + Fore.CYAN + "Add Node at Beginning")
    print("2. " + Fore.CYAN + "Add Node at End")
    print("3. " + Fore.CYAN + "Add Node at Specific Position")
    print("4. " + Fore.CYAN + "Remove First Node")
    print("5. " + Fore.CYAN + "Remove Last Node")
    print("6. " + Fore.CYAN + "Remove Node by Position")
    print("7. " + Fore.CYAN + "View Doubly Linked List")
    print("8. " + Fore.CYAN + "Find a Node")
    print("9. " + Fore.CYAN + "Count Total Nodes")
    print("10. " + Fore.RED + "Exit Program")


def main():
    linked_list = DoublyLinkedList()

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
                linked_list.delete_node_at_beginning()
                print(Fore.RED + "First node removed successfully.")

            elif choice == 5:
                linked_list.delete_node_at_end()
                print(Fore.RED + "Last node removed successfully.")

            elif choice == 6:
                position = int(input("Enter the node position to remove: "))
                linked_list.delete_node_at_position(position)
                print(Fore.RED + f"Node at position {position} removed successfully.")

            elif choice == 7:
                linked_list.display_list()

            elif choice == 8:
                data = int(input("Enter the value to search: "))
                if linked_list.search_node(data):
                    print(Fore.GREEN + "Value found in the linked list.")
                else:
                    print(Fore.RED + "Value not present in the linked list.")

            elif choice == 9:
                print(
                    Fore.BLUE
                    + f"Total number of nodes: {linked_list.length_of_list()}"
                )

            elif choice == 10:
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
