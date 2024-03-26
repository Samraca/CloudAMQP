import tkinter as tk
from tkinter import messagebox
from connection import publish_message
import json
from datetime import datetime

# Create the main window
window = tk.Tk()

# Change the name of the window to "publisher"
window.title("publisher")

# Change the size of the window to 150x150 pixels
window.geometry("150x150")

# Create three labels
label1 = tk.Label(window, text="Cuenta Inscrita:")
label2 = tk.Label(window, text="Cedula titular cuenta inscrita:")

# Create three textfields
textfield1 = tk.Entry(window)
textfield2 = tk.Entry(window)

# Add labels and textfields to the window
label1.pack()
textfield1.pack()
label2.pack()
textfield2.pack()

# Create a button
def send_message():
    
    message = {
        "cuenta_inscrita" : textfield1.get(),
        "cedula_titular": textfield2.get(),
        "tipo_operacion": "Inscripción",
        "fecha_operacion": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

    }

    message_json = json.dumps(message)
    publish_message("inscripciones", message_json)
    messagebox.showinfo("Message", message_json)

button = tk.Button(window, text="Send", command=send_message, bg="green", fg="white")

# Add the button to the window
button.pack()

# Start the main event loop
window.mainloop()
