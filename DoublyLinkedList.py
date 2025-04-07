# Clase TextEditor para implementar la interfaz gráfica del editor de texto
from TextEditor import DoublyLinkedList
import tkinter as tk
from tkinter import ttk


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Editor de Texto con Historial")
        self.history = DoublyLinkedList()

        # Área de texto
        self.text_area = tk.Text(root, wrap="word", width=50, height=20)
        self.text_area.pack(pady=10)

        # Botones
        self.save_button = ttk.Button(root, text="Guardar Estado", command=self.save_state)
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.undo_button = ttk.Button(root, text="Deshacer", command=self.undo)
        self.undo_button.pack(side=tk.LEFT, padx=5)

        self.redo_button = ttk.Button(root, text="Rehacer", command=self.redo)
        self.redo_button.pack(side=tk.LEFT, padx=5)

    # Método para guardar el estado actual del texto en la lista doblemente enlazada
    def save_state(self):
        current_text = self.text_area.get("1.0", tk.END).strip()
        self.history.append(current_text)

    # Método para deshacer (navegar al estado anterior)
    def undo(self):
        previous_text = self.history.move_backward()
        if previous_text is not None:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", previous_text)

    # Método para rehacer (navegar al estado siguiente)
    def redo(self):
        next_text = self.history.move_forward()
        if next_text is not None:
            self.text_area.delete("1.0", tk.END)
            self.text_area.insert("1.0", next_text)

# Función principal para ejecutar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = TextEditor(root)
    root.mainloop()