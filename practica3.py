import tkinter as tk  
from tkinter import messagebox  

# Clase Paciente
class Paciente:
    def __init__(self, nombre, edad, motivo, gravedad):  # constructor de la clase paciente
        self.nombre = nombre  # asignar nombre
        self.edad = edad  # asignar edad
        self.motivo = motivo  # asignar motivo
        self.gravedad = gravedad  # asignar gravedad

# Clase Cola (para manejar la fila de pacientes)
class Cola:
    def __init__(self):
        self.cola = []  # inicializar lista vacia de pacientes

    def vacia(self):
        return len(self.cola) == 0  # retorna True si la cola esta vacia
    
    def insertar(self, paciente):
        # Inserta segun prioridad de gravedad (Muy alta -> mayor prioridad)
        prioridad = {"Muy alta": 1, "Alta": 2, "Media": 3, "Baja": 4}  # diccionario de prioridad
        i = 0  # indice inicial
        for p in self.cola:  # recorrer la cola
            if prioridad[paciente.gravedad] < prioridad[p.gravedad]:  # comparar prioridades
                break  # salir del ciclo si se encuentra posicion
            i += 1  # incrementar indice
        self.cola.insert(i, paciente)  # insertar paciente en la posicion correcta
    
    def atender(self):
        if self.vacia():  # si la cola esta vacia
            return None  # retornar None
        return self.cola.pop(0)  # sacar el primer paciente
    
    def mostrar(self):
        return self.cola  # retornar toda la cola

    def proximo(self):
        if self.vacia():  # si la cola esta vacia
            return None  # retornar None
        return self.cola[0]  # retornar el primer paciente

# Clase Departamento
class Departamento:
    def __init__(self, nombre):  # constructor del departamento
        self.nombre = nombre  # asignar nombre del departamento
        self.cola = Cola()  # inicializar cola de pacientes

# Clase Sistema
class Sistema:
    def __init__(self):
        self.departamentos = {"General": Departamento("General")}  # iniciar con departamento General

    def agregar_departamento(self, nombre):  # agregar nuevo departamento
        nombre = nombre.strip()  # eliminar espacios
        if not nombre:  # validar nombre vacio
            return False  # no agregar
        if nombre in self.departamentos:  # verificar duplicado
            return False  # no agregar
        self.departamentos[nombre] = Departamento(nombre)  # agregar departamento
        return True  # retorno exito

    def agregar_paciente(self, nombre, edad, motivo, gravedad, departamento):  # agregar paciente
        if departamento not in self.departamentos:  # verificar departamento existente
            return None  # no se puede agregar
        paciente = Paciente(nombre, edad, motivo, gravedad)  # crear paciente
        self.departamentos[departamento].cola.insertar(paciente)  # insertar en la cola
        return paciente  # retornar paciente agregado

    def atender_paciente(self, departamento):  # atender paciente
        if departamento not in self.departamentos:  # verificar departamento
            return None  # retornar None
        return self.departamentos[departamento].cola.atender()  # atender paciente

# Interfaz grafica con Tkinter
class Interfaz:
    def __init__(self, ventana):  # constructor de la interfaz
        self.ventana = ventana  # asignar ventana principal
        self.ventana.title("Sistema de Atencion Medica")  # titulo ventana
        self.ventana.geometry("520x430")  # tamaño de ventana
        self.ventana.configure(bg="#f0f8ff")  # color de fondo
        self.sistema = Sistema()  # crear sistema
        self.ventana.iconbitmap("estructura.py\cadu.ico")  # icono ventana

        # Titulo principal
        tk.Label(
            ventana, 
            text="SISTEMA DE ATENCION MEDICA",  # texto titulo
            font=("Arial", 18, "bold"),  # fuente y tamaño
            fg="navy",  # color de letra
            bg="#f0f8ff"  # fondo
        ).pack(pady=12)  # empaquetar con margen vertical

        # Botones principales
        boton_frame = tk.Frame(ventana, bg="#f0f8ff")  # frame para botones
        boton_frame.pack(pady=12)  # empaquetar frame

        tk.Button(boton_frame, text=" +    Agregar paciente", width=25, bg="#d1e7dd", command=self.form_agregar).pack(pady=6)  # boton agregar paciente
        tk.Button(boton_frame, text=" -    Atender paciente", width=25, bg="#ffe5b4", command=self.form_atender).pack(pady=6)  # boton atender paciente
        tk.Button(boton_frame, text=" ?    Mostrar cola", width=25, bg="#cfe2ff", command=self.mostrar_cola).pack(pady=6)  # boton mostrar cola
        tk.Button(boton_frame, text=" !    Ver proximos", width=25, bg="#e6e6fa", command=self.mostrar_proximos).pack(pady=6)  # boton ver proximos
        tk.Button(boton_frame, text=" +    Agregar departamento", width=25, bg="#f8d7da", command=self.form_departamento).pack(pady=6)  # boton agregar departamento

       
    
    # Formulario para agregar paciente
    def form_agregar(self):
        win = tk.Toplevel(self.ventana)  # crear ventana secundaria
        win.title("Agregar paciente")  # titulo ventana
        win.geometry("420x320")  # tamaño ventana
        win.configure(bg="#fefefe")  # color fondo

        tk.Label(win, text="Formulario de Paciente", font=("Arial", 14, "bold"), fg="green", bg="#fefefe").pack(pady=10)  # titulo form

        frame = tk.Frame(win, bg="#fefefe")  # frame interno
        frame.pack(pady=6)  # empaquetar frame

        # Etiquetas de entradas
        tk.Label(frame, text="Nombre:", bg="#fefefe").grid(row=0, column=0, padx=5, pady=6, sticky="e")
        tk.Label(frame, text="Edad:", bg="#fefefe").grid(row=1, column=0, padx=5, pady=6, sticky="e")
        tk.Label(frame, text="Motivo:", bg="#fefefe").grid(row=2, column=0, padx=5, pady=6, sticky="e")
        tk.Label(frame, text="Gravedad:", bg="#fefefe").grid(row=3, column=0, padx=5, pady=6, sticky="e")
        tk.Label(frame, text="Departamento:", bg="#fefefe").grid(row=4, column=0, padx=5, pady=6, sticky="e")

        # Entradas
        e_nombre = tk.Entry(frame, width=28)  # entrada nombre
        e_edad = tk.Entry(frame, width=10)  # entrada edad
        e_motivo = tk.Entry(frame, width=28)  # entrada motivo
        e_nombre.grid(row=0, column=1, pady=6, sticky="w")  # posicion nombre
        e_edad.grid(row=1, column=1, pady=6, sticky="w")  # posicion edad
        e_motivo.grid(row=2, column=1, pady=6, sticky="w")  # posicion motivo

        gravedad = tk.StringVar(value="Media")  # variable gravedad
        tk.OptionMenu(frame, gravedad, "Muy alta", "Alta", "Media", "Baja").grid(row=3, column=1, pady=6, sticky="w")  # menu gravedad

        departamentos = list(self.sistema.departamentos.keys())  # lista de departamentos
        if not departamentos:  # si vacio
            departamentos = ["General"]  # asignar General
        dep = tk.StringVar(value=departamentos[0])  # variable departamento
        tk.OptionMenu(frame, dep, *departamentos).grid(row=4, column=1, pady=6, sticky="w")  # menu departamento

        # Boton guardar
        def agregar():  # funcion agregar paciente
            nombre = e_nombre.get().strip()  # obtener nombre
            edad = e_edad.get().strip()  # obtener edad
            motivo = e_motivo.get().strip()  # obtener motivo
            gravedad_val = gravedad.get()  # obtener gravedad
            depto_val = dep.get()  # obtener departamento

            if not nombre or not edad or not motivo:  # validar campos vacios
                messagebox.showwarning("Aviso", "Todos los campos son obligatorios")  # mensaje
                return  # salir

            # validar edad simple
            try:
                edad_int = int(edad)  # convertir a entero
                if edad_int < 0 or edad_int > 120:  # rango valido
                    raise ValueError  # error si no valido
            except:
                messagebox.showerror("Error", "Edad invalida. Debe ser un numero entre 0 y 120.")  # mensaje error
                return  # salir

            paciente = self.sistema.agregar_paciente(nombre, edad_int, motivo, gravedad_val, depto_val)  # agregar paciente
            if paciente:  # si exito
                messagebox.showinfo("Exito", f"Paciente '{paciente.nombre}' agregado en {depto_val}.")  # mensaje exito
            else:
                messagebox.showerror("Error", "No se pudo agregar el paciente (departamento invalido).")  # mensaje error
            win.destroy()  # cerrar ventana

        tk.Button(win, text="Guardar", bg="#d1e7dd", width=14, command=agregar).pack(pady=12)  # boton guardar

    # Atender paciente
    def form_atender(self):
        win = tk.Toplevel(self.ventana)  # ventana secundaria
        win.title("Atender paciente")  # titulo
        win.geometry("360x150")  # tamaño
        win.configure(bg="#fefefe")  # fondo

        tk.Label(win, text="Seleccione departamento:", bg="#fefefe").pack(pady=(12,4))  # instruccion

        departamentos = list(self.sistema.departamentos.keys())  # lista departamentos
        if not departamentos:  # si vacio
            departamentos = ["General"]  # asignar General
        dep_sel = tk.StringVar(value=departamentos[0])  # variable seleccion
        tk.OptionMenu(win, dep_sel, *departamentos).pack()  # menu opciones

        def atender():  # funcion atender
            depto = dep_sel.get()  # obtener departamento
            paciente = self.sistema.atender_paciente(depto)  # atender paciente
            if paciente:  # si hay paciente
                messagebox.showinfo("Atendido", f"Se atendio a {paciente.nombre} ({paciente.gravedad})")  # mensaje
            else:
                messagebox.showwarning("Cola vacia", "No hay pacientes en espera en ese departamento")  # mensaje vacio
            win.destroy()  # cerrar ventana

        tk.Button(win, text="Atender", bg="#ffe5b4", command=atender).pack(pady=10)  # boton atender

    # Mostrar cola completa
    def mostrar_cola(self):
        win = tk.Toplevel(self.ventana)  # ventana secundaria
        win.title("Cola de pacientes")  # titulo
        win.geometry("420x360")  # tamaño
        win.configure(bg="#fefefe")  # fondo

        tk.Label(win, text="Mostrar cola por departamento", font=("Arial", 12, "bold"), fg="blue", bg="#fefefe").pack(pady=8)  # titulo

        top_frame = tk.Frame(win, bg="#fefefe")  # frame superior
        top_frame.pack(pady=6)  # empaquetar

        departamentos = list(self.sistema.departamentos.keys())  # lista departamentos
        if not departamentos:  # si vacio
            departamentos = ["General"]  # asignar General
        dep_sel = tk.StringVar(value=departamentos[0])  # variable seleccion
        tk.OptionMenu(top_frame, dep_sel, *departamentos).pack()  # menu opciones

        list_frame = tk.Frame(win, bg="#fefefe")  # frame para lista
        list_frame.pack(fill="both", expand=True, padx=10, pady=8)  # empaquetar

        def cargar():  # funcion cargar lista
            for w in list_frame.winfo_children():  # limpiar lista
                w.destroy()  # destruir widgets
            depto = dep_sel.get()  # obtener departamento
            if depto not in self.sistema.departamentos:  # validar
                tk.Label(list_frame, text="Departamento invalido", bg="#fefefe", fg="red").pack()  # mensaje error
                return  # salir
            pacientes = self.sistema.departamentos[depto].cola.mostrar()  # obtener pacientes
            if not pacientes:  # si vacio
                tk.Label(list_frame, text="No hay pacientes en espera", bg="#fefefe", fg="red").pack()  # mensaje vacio
                return  # salir
            for i, p in enumerate(pacientes):  # recorrer pacientes
                tk.Label(list_frame, text=f"{i+1}. {p.nombre} ({p.gravedad}) - {p.edad} anos", bg="#fefefe").pack(anchor="w", pady=3)  # mostrar paciente

        tk.Button(win, text="Cargar cola", bg="#cfe2ff", command=cargar).pack(pady=6)  # boton cargar


    # Mostrar proximos N en la fila
    def mostrar_proximos(self):
        win = tk.Toplevel(self.ventana)  # ventana secundaria
        win.title("Proximos en la fila")  # titulo
        win.geometry("380x260")  # tamaño
        win.configure(bg="#fefefe")  # fondo

        tk.Label(win, text="Ver proximos N en la fila", font=("Arial", 12, "bold"), fg="purple", bg="#fefefe").pack(pady=8)  # titulo

        frame = tk.Frame(win, bg="#fefefe")  # frame
        frame.pack(pady=6)  # empaquetar

        tk.Label(frame, text="Departamento:", bg="#fefefe").grid(row=0, column=0, padx=6, pady=6, sticky="e")  # etiqueta
        departamentos = list(self.sistema.departamentos.keys())  # lista departamentos
        if not departamentos:  # si vacio
            departamentos = ["General"]  # asignar General
        dep_sel = tk.StringVar(value=departamentos[0])  # variable seleccion
        tk.OptionMenu(frame, dep_sel, *departamentos).grid(row=0, column=1, padx=6, pady=6, sticky="w")  # menu opciones

        tk.Label(frame, text="Mostrar cuantos:", bg="#fefefe").grid(row=1, column=0, padx=6, pady=6, sticky="e")  # etiqueta cantidad
        n_entry = tk.Entry(frame, width=6)  # entrada numero
        n_entry.insert(0, "3")  # valor inicial
        n_entry.grid(row=1, column=1, padx=6, pady=6, sticky="w")  # posicion

        list_frame = tk.Frame(win, bg="#fefefe")  # frame lista
        list_frame.pack(fill="both", expand=True, padx=10, pady=8)  # empaquetar

        def cargar_proximos():  # funcion mostrar proximos
            for w in list_frame.winfo_children():  # limpiar
                w.destroy()  # destruir widgets

            depto = dep_sel.get()  # obtener departamento
            if depto not in self.sistema.departamentos:  # validar
                tk.Label(list_frame, text="Departamento invalido", bg="#fefefe", fg="red").pack()  # mensaje error
                return  # salir

            try:
                n = int(n_entry.get())  # obtener numero
                if n <= 0:  # validar positivo
                    raise ValueError  # error si no
            except:
                messagebox.showerror("Error", "Ingrese un numero valido para cuantos mostrar")  # mensaje error
                return  # salir

            cola = self.sistema.departamentos[depto].cola.mostrar()  # obtener cola
            if not cola:  # si vacio
                tk.Label(list_frame, text="La cola esta vacia", bg="#fefefe", fg="red").pack()  # mensaje vacio
                return  # salir

            tk.Label(list_frame, text=f"Proximos {n} en {depto}:", bg="#fefefe", font=("Arial", 10, "bold")).pack(anchor="w", pady=4)  # titulo lista
            mostrados = 0  # contador
            for i, p in enumerate(cola):  # recorrer cola
                if mostrados >= n:  # si ya mostro N
                    break  # salir
                tk.Label(list_frame, text=f"{i+1}. {p.nombre} ({p.gravedad}) - {p.edad} anos", bg="#fefefe").pack(anchor="w", padx=6)  # mostrar paciente
                mostrados += 1  # incrementar

            if mostrados == 0:  # si no hay pacientes
                tk.Label(list_frame, text="No hay suficientes pacientes para mostrar.", bg="#fefefe").pack()  # mensaje

        tk.Button(win, text="Mostrar proximos", bg="#e6e6fa", command=cargar_proximos).pack(pady=6)  # boton mostrar


    # Agregar departamento
    def form_departamento(self):
        win = tk.Toplevel(self.ventana)  # ventana secundaria
        win.title("Nuevo departamento")  # titulo
        win.geometry("320x160")  # tamaño
        win.configure(bg="#fefefe")  # fondo

        tk.Label(win, text="Nombre del departamento:", bg="#fefefe").pack(pady=6)  # etiqueta
        e_nombre = tk.Entry(win)  # entrada nombre
        e_nombre.pack(pady=6)  # empaquetar

        def agregar():  # funcion agregar
            nombre = e_nombre.get()  # obtener nombre
            if not nombre.strip():  # validar vacio
                messagebox.showwarning("Aviso", "Debe ingresar un nombre valido")  # mensaje
                return  # salir
            ok = self.sistema.agregar_departamento(nombre)  # agregar departamento
            if ok:  # exito
                messagebox.showinfo("Exito", f"Departamento {nombre} agregado")  # mensaje exito
                win.destroy()  # cerrar ventana
            else:
                messagebox.showerror("Error", "No se pudo crear el departamento (ya existe o nombre invalido)")  # mensaje error

        tk.Button(win, text="Guardar", bg="#f8d7da", command=agregar).pack(pady=10)  # boton guardar


# Programa principal
if __name__ == "__main__":
    root = tk.Tk()  # crear ventana principal
    app = Interfaz(root)  # iniciar interfaz
    root.mainloop()  # ejecutar bucle principal
