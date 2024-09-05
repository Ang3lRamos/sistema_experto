import tkinter as tk
from tkinter import messagebox
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definir las variables difusas
ruido_motor = ctrl.Antecedent(np.arange(0, 11, 1), 'ruido_motor')
bateria = ctrl.Antecedent(np.arange(0, 11, 1), 'bateria')
diagnostico = ctrl.Consequent(np.arange(0, 26, 1), 'diagnostico')

# Definir las funciones de pertenencia para ruido del motor
ruido_motor['leve'] = fuzz.trimf(ruido_motor.universe, [0, 0, 3])
ruido_motor['moderado'] = fuzz.trimf(ruido_motor.universe, [2, 5, 8])
ruido_motor['grave'] = fuzz.trimf(ruido_motor.universe, [7, 10, 10])

# Definir las funciones de pertenencia para batería
bateria['buena'] = fuzz.trimf(bateria.universe, [8, 10, 10])
bateria['media'] = fuzz.trimf(bateria.universe, [3, 5, 7])
bateria['baja'] = fuzz.trimf(bateria.universe, [0, 0, 3])

# Definir las funciones de pertenencia para diagnóstico
diagnostico['sin_problemas'] = fuzz.trimf(diagnostico.universe, [0, 0, 10])
diagnostico['problema_moderado'] = fuzz.trimf(diagnostico.universe, [5, 10, 15])
diagnostico['problema_grave'] = fuzz.trimf(diagnostico.universe, [15, 25, 25])

# Reglas difusas ajustadas
rule1 = ctrl.Rule(ruido_motor['leve'] & bateria['buena'], diagnostico['sin_problemas'])
rule2 = ctrl.Rule(ruido_motor['leve'] & bateria['media'], diagnostico['sin_problemas'])
rule3 = ctrl.Rule(ruido_motor['leve'] & bateria['baja'], diagnostico['problema_moderado'])
rule4 = ctrl.Rule(ruido_motor['moderado'] & bateria['buena'], diagnostico['problema_moderado'])
rule5 = ctrl.Rule(ruido_motor['moderado'] & bateria['media'], diagnostico['problema_grave'])
rule6 = ctrl.Rule(ruido_motor['moderado'] & bateria['baja'], diagnostico['problema_grave'])
rule7 = ctrl.Rule(ruido_motor['grave'] & bateria['buena'], diagnostico['problema_grave'])
rule8 = ctrl.Rule(ruido_motor['grave'] & bateria['media'], diagnostico['problema_grave'])
rule9 = ctrl.Rule(ruido_motor['grave'] & bateria['baja'], diagnostico['problema_grave'])

# Crear el sistema de control difuso
diagnostico_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9])
diagnostico_simulador = ctrl.ControlSystemSimulation(diagnostico_ctrl)

# Función para realizar el diagnóstico difuso
def realizar_diagnostico(ruido_motor_val, bateria_val):
    diagnostico_simulador.input['ruido_motor'] = ruido_motor_val
    diagnostico_simulador.input['bateria'] = bateria_val
    diagnostico_simulador.compute()
    return diagnostico_simulador.output['diagnostico']

# Función para mostrar el diagnóstico difuso
def mostrar_diagnostico():
    ruido_val = ruido_motor_scale.get()
    bateria_val = bateria_scale.get()

    resultado = realizar_diagnostico(ruido_val, bateria_val)

    if resultado is not None:
        if bateria_val == 0:
            diagnostico = "Problema crítico: La batería está completamente descargada."
        elif resultado < 10:
            diagnostico = "Sin problemas significativos."
        elif 10 <= resultado < 15:
            diagnostico = "Problema moderado, es recomendable una revisión."
        else:
            diagnostico = "Problema grave, revisa el vehículo inmediatamente."
        
        messagebox.showinfo("Diagnóstico Difuso", f"Resultado del diagnóstico: {diagnostico}\nGravedad: {resultado:.2f}")
    else:
        messagebox.showwarning("Error", "No se pudo obtener el diagnóstico.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Diagnóstico Difuso de Vehículos")

# Etiqueta para el ruido del motor
tk.Label(root, text="Ruido del motor (0 = Sin ruido, 10 = Muy fuerte)").pack(anchor=tk.W)
ruido_motor_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
ruido_motor_scale.pack(anchor=tk.W)

# Etiqueta para el nivel de batería
tk.Label(root, text="Nivel de batería (0 = Sin carga, 10 = Buena)").pack(anchor=tk.W)
bateria_scale = tk.Scale(root, from_=0, to=10, orient=tk.HORIZONTAL)
bateria_scale.pack(anchor=tk.W)

# Botón para obtener diagnóstico
tk.Button(root, text="Obtener diagnóstico", command=mostrar_diagnostico).pack(pady=10)

# Ejecutar la aplicación
root.mainloop()
