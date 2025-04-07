import tkinter as tk
from tkinter import ttk

# Clase DoublyNode
class DoublyNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
