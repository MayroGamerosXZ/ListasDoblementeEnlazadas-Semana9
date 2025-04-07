# Clase DoublyLinkedList para implementar la lista doblemente enlazada
from DoublyNode import DoublyNode

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    # Método para agregar un nuevo nodo al final de la lista
    def append(self, value):
        new_node = DoublyNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.current = new_node  # Establecer el nodo actual como el nuevo nodo

    # Método para eliminar un nodo con un valor específico
    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                if self.current == current:
                    self.current = current.prev
                return
            current = current.next

    # Método para mover el puntero al siguiente nodo (Rehacer)
    def move_forward(self):
        if self.current and self.current.next:
            self.current = self.current.next
            return self.current.value
        return None

    # Método para mover el puntero al nodo anterior (Deshacer)
    def move_backward(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            return self.current.value
        return None

    # Método para obtener el valor del nodo actual
    def current(self):
        return self.current.value if self.current else None
