# Definimos una clase para los nodos de la lista enlazada doble
class DoublyNode:
    def __init__(self, value):
        self.value = value  # Valor almacenado en el nodo
        self.prev = None    # Referencia al nodo anterior
        self.next = None    # Referencia al nodo siguiente

# Definimos una clase para la lista enlazada doble
class DoublyLinkedList:
    def __init__(self):
        self.head = None   # Referencia al primer nodo de la lista
        self.tail = None   # Referencia al último nodo de la lista
        self.current_node = None  # Referencia al nodo actual

    # Método para agregar un nuevo nodo al final de la lista
    def append(self, value):
        new_node = DoublyNode(value)
        if not self.head:  # Si la lista está vacía
            self.head = new_node
            self.tail = new_node
            self.current_node = new_node
        else:
            self.tail.next = new_node  # Enlazar el nuevo nodo al último nodo
            new_node.prev = self.tail  # Enlazar el último nodo al nuevo nodo
            self.tail = new_node  # Actualizar el último nodo
            self.current_node = new_node  # Actualizar el nodo actual

    # Método para eliminar un nodo por su valor
    def delete(self, value):
        node = self.head
        while node:
            if node.value == value:
                if node.prev:
                    node.prev.next = node.next  # Enlazar el nodo anterior al siguiente
                if node.next:
                    node.next.prev = node.prev  # Enlazar el nodo siguiente al anterior
                if node == self.head:  # Si el nodo a eliminar es el primero
                    self.head = node.next  # Actualizar el primer nodo
                if node == self.tail:  # Si el nodo a eliminar es el último
                    self.tail = node.prev  # Actualizar el último nodo
                if node == self.current_node:  # Si el nodo a eliminar es el actual
                    self.current_node = node.prev if node.prev else node.next  # Actualizar el nodo actual
                return
            node = node.next  # Mover al siguiente nodo

    # Método para mover el nodo actual una posición adelante
    def move_forward(self):
        if self.current_node and self.current_node.next:
            self.current_node = self.current_node.next

    # Método para mover el nodo actual una posición atrás
    def move_backward(self):
        if self.current_node and self.current_node.prev:
            self.current_node = self.current_node.prev

    # Método para obtener el valor del nodo actual
    def current(self):
        return self.current_node.value if self.current_node else None


# Importamos la biblioteca Tkinter para la GUI
import tkinter as tk

# Definimos una clase para el editor de texto
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto")

        # Creamos el área de texto y la mostramos en la ventana
        self.text_area = tk.Text(root, wrap='word', height=20, width=50)
        self.text_area.pack(pady=10)

        # Creamos un botón para guardar el estado actual del texto
        self.save_button = tk.Button(root, text="Guardar estado", command=self.save_state)
        self.save_button.pack(side='left', padx=5)

        # Creamos un botón para deshacer la última acción
        self.undo_button = tk.Button(root, text="Deshacer", command=self.undo)
        self.undo_button.pack(side='left', padx=5)

        # Creamos un botón para rehacer la última acción deshecha
        self.redo_button = tk.Button(root, text="Rehacer", command=self.redo)
        self.redo_button.pack(side='left', padx=5)

        # Inicializamos la lista enlazada doble para el historial
        self.history = DoublyLinkedList()

    # Método para guardar el estado actual del texto en el historial
    def save_state(self):
        current_text = self.text_area.get("1.0", tk.END).strip()
        if current_text:
            self.history.append(current_text)
            self.text_area.delete("1.0", tk.END)

    # Método para deshacer la última acción
    def undo(self):
        if self.history.current_node:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, self.history.current())
            self.history.move_backward()

    # Método para rehacer la última acción deshecha
    def redo(self):
        self.history.move_forward()
        if self.history.current_node:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert(tk.END, self.history.current())

# Inicializamos la aplicación y mostramos la ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()