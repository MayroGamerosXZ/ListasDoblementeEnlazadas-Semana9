# ListasDoblementeEnlazadas-Semana9
# TextEditor con Historial

Este proyecto implementa un editor de texto simple con funciones de deshacer y rehacer utilizando Python y Tkinter. El editor utiliza una lista enlazada doble para manejar el historial de acciones, permitiendo deshacer y rehacer cambios en el texto.

## Dependencias

- Python (versión 3.x)
- Tkinter (biblioteca estándar de Python para interfaces gráficas)

## Instalación

1. Asegúrate de tener Python instalado en tu sistema.
2. Clona o descarga el repositorio en tu máquina local.
3. Ejecuta el script `text_editor.py` utilizando Python.

## Uso

1. Inicia la aplicación ejecutando el script `text_editor.py`.
2. Escriba texto en el área de texto.
3. Use los botones "Guardar estado", "Deshacer" y "Rehacer" para manejar el historial de acciones.

## Características

- **Guardar estado**: Guarda el texto actual en el área de texto en el historial y lo borra.
- **Deshacer**: Deshace la última acción guardada, si es posible.
- **Rehacer**: Rehace la última acción deshecha, si es posible.

## Estructura del Código

El proyecto está organizado en dos clases principales: `DoublyNode` y `DoublyLinkedList`, que representan los nodos y la lista enlazada doble, respectivamente. La clase `TextEditor` utiliza estas clases para implementar el editor de texto con historial.

### Clases

- **DoublyNode**: Representa un nodo en la lista enlazada doble.
- **DoublyLinkedList**: Representa la lista enlazada doble y proporciona métodos para agregar, eliminar, mover y obtener el nodo actual.
- **TextEditor**: Implementa el editor de texto con Tkinter y utiliza la lista enlazada doble para manejar el historial.

### Funcionalidad

- **save_state**: Guarda el texto actual en el historial y lo borra.
- **undo**: Deshace la última acción guardada.
- **redo**: Rehace la última acción deshecha.

## Contribuir

Puedes contribuir a este proyecto enviando pull requests o abriendo issues para reportar bugs o sugerir nuevas características.
