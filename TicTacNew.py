import tkinter as tk

class DraggableLabel(tk.Label):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        # Binde Mausereignisse an das Label
        self.bind('<Button-1>', self.start_drag)
        self.bind('<B1-Motion>', self.do_drag)
        self.bind('<ButtonRelease-1>', self.stop_drag)
        # Initialisiere Drag-Daten (Startkoordinaten)
        self._drag_data = {"x": 0, "y": 0}

    def start_drag(self, event):
        # Speichere die Startposition der Maus
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def do_drag(self, event):
        # Berechne die neue Position basierend auf der Mausbewegung
        x = self.winfo_x() - self._drag_data["x"] + event.x
        y = self.winfo_y() - self._drag_data["y"] + event.y
        # Aktualisiere die Position des Widgets
        self.place(x=x, y=y)

    def stop_drag(self, event):
        # Setze die Drag-Daten zurück
        self._drag_data = {"x": 0, "y": 0}

# Erstelle das Hauptfenster
root = tk.Tk()
root.geometry("400x400")
root.title("Tic Tac New")

# Erstelle und platziere das erste verschiebbare Label mit dem Text "X"
label = DraggableLabel(root, text="X", bg="red", padx=10, pady=5)
label.place(x=50, y=50)

label1 = DraggableLabel(root, text="X", bg="red", padx=10, pady=5)
label1.place(x=40, y=60)

label2 = DraggableLabel(root, text="X", bg="red", padx=10, pady=5)
label2.place(x=40, y=60)

label3 = DraggableLabel(root, text="X", bg="red", padx=10, pady=5)
label3.place(x=40, y=60)

label4 = DraggableLabel(root, text="X", bg="red", padx=10, pady=5)
label4.place(x=40, y=60)


# Erstelle und platziere das erste verschiebbare Label mit dem Text "O"
label = DraggableLabel(root, text="O", bg="green", padx=10, pady=5)
label.place(x=350, y=50)

label1 = DraggableLabel(root, text="O", bg="green", padx=10, pady=5)
label1.place(x=340, y=60)

label2 = DraggableLabel(root, text="O", bg="green", padx=10, pady=5)
label2.place(x=340, y=60)

label3 = DraggableLabel(root, text="O", bg="green", padx=10, pady=5)
label3.place(x=340, y=60)

label4 = DraggableLabel(root, text="O", bg="green", padx=10, pady=5)
label4.place(x=340, y=60)




root.mainloop()
