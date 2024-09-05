import tkinter as tk
from tkinter import ttk
from rules_engine import diagnosticar_problema

# Función para obtener los síntomas ingresados y mostrar el diagnóstico en la interfaz
def mostrar_diagnostico():
    modelo = modelo_var.get()
    sintomas = []
    
    # Recolectar los síntomas seleccionados
    if no_arranca_var.get():
        sintomas.append("no arranca")
    if clic_var.get():
        sintomas.append("clic")
    if tablero_apagado_var.get():
        sintomas.append("tablero apagado")
    if luces_encendidas_var.get():
        sintomas.append("luces encendidas")
    if humo_var.get():
        sintomas.append("humo")
    if ruido_motor_var.get():
        sintomas.append("ruido del motor")
    if frenos_var.get():
        sintomas.append("frenos")
    if ruido_frenar_var.get():
        sintomas.append("ruido al frenar")

    # Verificación de que se seleccionaron síntomas
    if not sintomas:
        diagnostico_texto.config(state=tk.NORMAL)
        diagnostico_texto.delete("1.0", tk.END)
        diagnostico_texto.insert(tk.END, "Debe seleccionar al menos un síntoma para diagnosticar.")
        diagnostico_texto.config(state=tk.DISABLED)
        return
    
    # Llamar a la función para diagnosticar problemas
    problemas = diagnosticar_problema(sintomas, modelo)
    
    # Mostrar los resultados en el widget Text
    diagnostico_texto.config(state=tk.NORMAL)
    diagnostico_texto.delete("1.0", tk.END)
    
    if problemas:
        diagnostico_texto.insert(tk.END, "Posibles problemas:\n" + "\n".join(problemas))
    else:
        diagnostico_texto.insert(tk.END, "No se encontraron problemas coincidentes para los síntomas seleccionados.")
    
    diagnostico_texto.config(state=tk.DISABLED)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Diagnóstico de Vehículos")
root.configure(bg="#f0f4f8")

# Estilos de ttk
style = ttk.Style()
style.configure("TCombobox", foreground="#333", background="#ffffff", fieldbackground="#ffffff")
style.configure("TButton", background="#005f99", foreground="black", font=("Arial", 12))
style.map("TButton", background=[('active', '#007acc')])

# Variables de los síntomas
no_arranca_var = tk.BooleanVar()
clic_var = tk.BooleanVar()
tablero_apagado_var = tk.BooleanVar()
luces_encendidas_var = tk.BooleanVar()
humo_var = tk.BooleanVar()
ruido_motor_var = tk.BooleanVar()
frenos_var = tk.BooleanVar()
ruido_frenar_var = tk.BooleanVar()

# Variable para el modelo de vehículo
modelo_var = tk.StringVar()

# Crear la interfaz gráfica
tk.Label(root, text="Seleccione el modelo del vehículo:", bg="#f0f4f8", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=5)

# Combobox para seleccionar el modelo del vehículo
modelos = ["Sedán", "SUV", "Camión", "Motocicleta", "Furgoneta"]
modelo_combobox = ttk.Combobox(root, textvariable=modelo_var, values=modelos)
modelo_combobox.set("Sedán")  # Valor predeterminado
modelo_combobox.pack(anchor=tk.W, padx=10, pady=5)

# Etiqueta para los síntomas
tk.Label(root, text="Seleccione los síntomas observados:", bg="#f0f4f8", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=5)

# Crear categorías para los síntomas
frame_motor = tk.LabelFrame(root, text="Problemas con el motor", padx=10, pady=10, bg="#ffffff", font=("Arial", 10, "bold"))
frame_motor.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Checkbutton(frame_motor, text="El vehículo no arranca", variable=no_arranca_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)
tk.Checkbutton(frame_motor, text="Ruido de clic al intentar arrancar", variable=clic_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)
tk.Checkbutton(frame_motor, text="Hay humo saliendo del motor", variable=humo_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)
tk.Checkbutton(frame_motor, text="Ruido extraño en el motor", variable=ruido_motor_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)

frame_electrico = tk.LabelFrame(root, text="Problemas eléctricos", padx=10, pady=10, bg="#ffffff", font=("Arial", 10, "bold"))
frame_electrico.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Checkbutton(frame_electrico, text="Las luces del tablero están apagadas", variable=tablero_apagado_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)
tk.Checkbutton(frame_electrico, text="Las luces del tablero están encendidas", variable=luces_encendidas_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)

frame_frenos = tk.LabelFrame(root, text="Problemas con los frenos", padx=10, pady=10, bg="#ffffff", font=("Arial", 10, "bold"))
frame_frenos.pack(fill="both", expand="yes", padx=10, pady=10)

tk.Checkbutton(frame_frenos, text="Frenos haciendo ruido", variable=frenos_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)
tk.Checkbutton(frame_frenos, text="Ruido al frenar", variable=ruido_frenar_var, bg="#ffffff", font=("Arial", 10)).pack(anchor=tk.W)

# Botón para obtener diagnóstico
ttk.Button(root, text="Diagnosticar", command=mostrar_diagnostico).pack(pady=10)

# Widget Text para mostrar el diagnóstico
tk.Label(root, text="Diagnóstico:", bg="#f0f4f8", font=("Arial", 12, "bold")).pack(anchor=tk.W, padx=10, pady=5)
diagnostico_texto = tk.Text(root, height=10, width=50, state=tk.DISABLED, bg="#ffffff", fg="#333", font=("Arial", 10))
diagnostico_texto.pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
