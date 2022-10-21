''' Construction of symbol table using hash table and linked list in python-v3.8.10
    
    Name: Abdullah Ibn Amin
    ID: 18304015
    Course Name: Compiler Sessional
    Course Code: CSE - 3104
    Semester: Spring-22
'''

class SymbolInfo:
    def __init__(self, symbol, type):
        self.symbol : str = symbol
        self.type : str = type
        self.next = None


class LinkedList:
    
    ''' Implementation of singly linked-list for the hash table '''
    
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, symbol, type: str):
        new_node = SymbolInfo(symbol, type.upper())

        if self.head == None:
            self.head = new_node # if list is empty insert a node at the start
        else:
            temp = self.head
            while temp.next != None:
                if temp.symbol == symbol:
                    print("\nInsertion Failed\nSymbol already exists")
                    break
                else:
                    temp = temp.next

            if temp.symbol == symbol:
                print("\nInsertion Failed\nSymbol already exists.")
            else:
                temp.next = new_node
    
    def delete_by_symbol(self, symbol):
        if self.head != None:
            if self.head.symbol == symbol: # if the node to be deleted is the first node
                self.head = self.head.next
            else:
                temp = self.head
                while temp.next != None:
                    if temp.next.symbol == symbol:
                        temp.next = temp.next.next
                    else:
                        temp = temp.next
    
    def search_by_symbol(self, symbol):
        temp = self.head
        count = 0
        while temp != None:
            if temp.symbol == symbol:
                break
            else:
                temp = temp.next
            count += 1
        return (count, temp.symbol, temp.type)

    def traverse(self):
        temp = self.head
        string = ''
        while temp != None:
            if temp.next != None:
                string += f"{temp.symbol} ( {temp.type} ), "
            else:
                string += f"{temp.symbol} ( {temp.type} )"
            temp = temp.next
        return string


class SymbolTable:

    ''' Implementation of Hash Table '''

    def __init__(self):
        self.ARRAY_SIZE = 20
        self.arr = [LinkedList() for _ in range(self.ARRAY_SIZE)]
    
    def get_hash(self, symbol):

        ''' Implementation of sdbm hashing algorithm.
        reference : https://stackoverflow.com/a/14409947
                    http://www.cse.yorku.ca/~oz/hash.html
        '''

        hash = 0
        for chr in symbol:
            hash = ord(chr) + (hash << 6) + (hash << 16) - hash
        final_hash_value = hash % self.ARRAY_SIZE

        return final_hash_value
    
    def insert(self, symbol, type):
        arr_index_num = self.get_hash(symbol)
        self.arr[arr_index_num].insert_at_end(symbol, type)

    def dump(self):
        for index, value in enumerate(self.arr):
            if value.traverse() == None:
                print(f"{index}: ")
            else:
                print(f"{index}: {value.traverse()}")

    def lookup(self, symbol):
        arr_index_num = self.get_hash(symbol)
        result = self.arr[arr_index_num].search_by_symbol(symbol)

        print(f"Hash index: {arr_index_num}")
        print(f"Chain Index: {result[0]}")
        print(f"Item(symbol, type): {result[1]}, ( {result[2]} )")

    def erase(self, symbol):
        arr_index_num = self.get_hash(symbol)
        self.arr[arr_index_num].delete_by_symbol(symbol)


def menu():
    print("""
        *press 1 to insert a new symbol along with its type into the symbol-table
        *press 2 to lookup whether a given symbol already exists in the symbol-table or not
        *press 3 to dump the contents of the symbol table to the console
        *press 4 to delete a given symbol if it already exists in the symbol-table
        *press 0 to exit
    """)



if __name__ == "__main__":
    x = SymbolTable()

    menu()
    choice = int(input("Choice: "))

    while choice != 0:

        if choice == 1:
            symbol = input("Symbol: ")
            type = input("Type: ")
            x.insert(symbol, type)
        
        if choice == 2:
            symbol = input("Symbol: ")
            x.lookup(symbol)
        
        if choice == 3:
            x.dump()
        
        if choice == 4:
            symbol = input("Symbol: ")
            x.erase(symbol)
        
        menu()
        choice = int(input("Choice: "))







































    
