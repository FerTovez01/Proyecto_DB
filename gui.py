import tkinter as tk
from tkinter import ttk, messagebox
from memory_simulator import MemorySimulator

# Configuración del simulador
total_memory = 1000
page_size = 10
simulator = MemorySimulator(total_memory,page_size)

def initialize_fixed():
    try:
        partition_size = int(entry_partition_size.get())  # Lee el tamaño de partición
        simulator.fixed_partitioning(partition_size)
        update_memory_display()
        messagebox.showinfo("Particiones Fijas", f"Particiones inicializadas con tamaño {partition_size}.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

def add_process_fixed():
    """ Agregar un proceso a la memoria con particiones fijas. """
    try:
        process_id = entry_process_id_fixed.get()  # Obtener el ID del proceso
        process_size = int(entry_process_size.get())  # Obtener el tamaño del proceso
        result = simulator.add_process_fixed(process_id, process_size)  # Llamar al método del simulador
        messagebox.showinfo("Agregar Proceso Fijo", result)
        update_memory_display()
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un número válido para el tamaño del proceso.")

def initialize_dynamic():
    simulator.dynamic_partitioning()
    update_memory_display()
    messagebox.showinfo("Particiones Dinámicas", "Memoria dinámica inicializada.")

def add_process_dynamic():
    try:
        process_id = entry_process_id_dynamic.get()  # Lee el ID del proceso
        process_size = int(entry_process_size_dynamic.get())  # Lee el tamaño del proceso
        result = simulator.add_process_dynamic(process_id, process_size)
        update_memory_display()
        messagebox.showinfo("Agregar Proceso Dinámico", result)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido.")

def compact_dynamic_memory():
    """
    Llama a la compactación de memoria dinámica y actualiza la visualización.
    """
    result = simulator.compact_memory()
    update_memory_display()
    messagebox.showinfo("Compactación", result)

def assign_pages():
    """Asigna páginas a un proceso en función del tamaño de página y proceso."""
    result = ""  # Aseguramos que result tenga un valor predeterminado
    try:
        process_id = entry_process_id_paging.get()  # O también entry_process_id_fixed si es necesario
        process_size = int(entry_process_size_paging.get())
        page_size = int(entry_page_size_paging.get())  # Obtiene el tamaño de página
        algorithm = algorithm_choice.get()

        if algorithm == "FIFO":
            result = simulator.paging(process_id, process_size, page_size)
        elif algorithm == "LRU":
            result = simulator.replace_page_lru(simulator.page_table, process_id)
        elif algorithm == "Reloj":
            result = simulator.replace_page_clock(simulator.page_table, process_id, simulator.use_bits)
        else:
            result = "Algoritmo no válido seleccionado."

        update_memory_display()
        messagebox.showinfo("Paginación", result)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")
    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {e}")


def add_process_segmentation():
    """Agrega un proceso con segmentación."""
    try:
        process_id = entry_process_id_segmentation.get()  # Lee el ID del proceso
        process_size = int(entry_process_size_segmentation.get())  # Lee el tamaño del proceso
        num_segments = int(entry_num_segments.get())  # Lee el número de segmentos
        result = simulator.add_process_segments(process_id, process_size, num_segments)
        update_memory_display()
        messagebox.showinfo("Agregar Proceso con Segmentación", result)
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce números válidos.")

def update_memory_display():
    memory_state = simulator.display_memory()
    memory_label.config(text=memory_state)
    draw_memory()  # Llamar a la función de dibujo para actualizar el estado visual de la memoria



def draw_memory():
    """Dibuja el estado de la memoria física y virtual en el canvas."""
    memory_canvas.delete("all")  # Limpiar el canvas antes de redibujar
    block_height = 40  # Altura de cada bloque de memoria
    current_y = 20

    # Memoria física
    memory_canvas.create_text(210, 10, text="Memoria Física", fill="white")
    for i, block in enumerate(simulator.fixed_partitions):
        color = "green" if block is None else "red"
        memory_canvas.create_rectangle(20, current_y, 400, current_y + block_height, fill=color, outline="black")
        memory_canvas.create_text(210, current_y + block_height / 2, text=f"Bloque {i + 1}: {'Libre' if block is None else block}", fill="white")
        current_y += block_height + 10

    # Memoria virtual
    current_y = 20
    memory_canvas.create_text(575, 10, text="Memoria Virtual", fill="white")
    
    # Imprimir la memoria virtual para depurar
    print("Memoria virtual actual: ", simulator.virtual_memory)

    for i, page in enumerate(simulator.virtual_memory):
        color = "blue" if page is None else "yellow"
        memory_canvas.create_rectangle(450, current_y, 700, current_y + block_height, fill=color, outline="black")
        memory_canvas.create_text(575, current_y + block_height / 2, text=f"Página {i + 1}: {page}", fill="white")
        current_y += block_height + 10
        
       # Memoria dinámica
    current_y = 20
    memory_canvas.create_text(575, 10, text="Memoria Dinámica", fill="white")
    for partition in simulator.dynamic_partitions:  # Iterar sobre las particiones dinámicas
        color = "green" if partition['status'] == 'free' else "red"
        memory_canvas.create_rectangle(450, current_y, 700, current_y + block_height, fill=color, outline="black")
        memory_canvas.create_text(575, current_y + block_height / 2,
                                  text=f"Bloque {partition['start']} - Tamaño {partition['size']}: {'Libre' if partition['status'] == 'free' else partition['process_id']}",
                                  fill="white")
        current_y += block_height + 10

    def add_process_fixed(self, process_id, process_size):
        # Lógica para agregar un proceso fijo (ejemplo)
        result = self.simulator.add_process_fixed(process_id, process_size)
        self.draw_memory()  # Llamar a draw_memory() para actualizar la visualización

    def add_process_dynamic(self, process_id, process_size):
        # Lógica para agregar un proceso dinámico (ejemplo)
        result = self.simulator.add_process_dynamic(process_id, process_size)
        self.draw_memory()  # Llamar a draw_memory() para actualizar la visualización

# Interfaz gráfica
root = tk.Tk()
root.title("Simulador de Gestión de Memoria")
root.geometry("800x600")
root.config(bg="#2e3b4e")

# Crear el contenedor para las pestañas
tab_control = ttk.Notebook(root)
tab_control.pack(pady=10, fill=tk.BOTH, expand=True)

# Pestaña Particionamiento Fijo
fixed_frame = tk.Frame(tab_control, bg="#4e5d6c")
tab_control.add(fixed_frame, text="Particionamiento Fijo")

# Campos y botones para particionamiento fijo
tk.Label(fixed_frame, text="Tamaño de Partición:", bg="#4e5d6c", fg="white").grid(row=0, column=0, pady=10)
entry_partition_size = tk.Entry(fixed_frame)
entry_partition_size.grid(row=0, column=1, pady=10)

tk.Label(fixed_frame, text="ID del Proceso:", bg="#4e5d6c", fg="white").grid(row=1, column=0, pady=10)
entry_process_id_fixed = tk.Entry(fixed_frame)
entry_process_id_fixed.grid(row=1, column=1, pady=10)

tk.Label(fixed_frame, text="Tamaño del Proceso:", bg="#4e5d6c", fg="white").grid(row=2, column=0, pady=10)
entry_process_size = tk.Entry(fixed_frame)
entry_process_size.grid(row=2, column=1, pady=10)

tk.Button(fixed_frame, text="Inicializar", command=initialize_fixed).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(fixed_frame, text="Agregar Proceso", command=add_process_fixed).grid(row=4, column=0, columnspan=2, pady=10)

# Pestaña Particionamiento Dinámico
dynamic_frame = tk.Frame(tab_control, bg="#4e5d6c")
tab_control.add(dynamic_frame, text="Particionamiento Dinámico")

# Campos y botones para particionamiento dinámico
tk.Button(dynamic_frame, text="Inicializar Dinámico", command=initialize_dynamic).pack(pady=10)

# Definición de entradas para el ID del proceso y tamaño del proceso en particionamiento dinámico
tk.Label(dynamic_frame, text="ID del Proceso (Dinámico):", bg="#4e5d6c", fg="white").pack(pady=5)
entry_process_id_dynamic = tk.Entry(dynamic_frame)
entry_process_id_dynamic.pack(pady=5)

tk.Label(dynamic_frame, text="Tamaño del Proceso (Dinámico):", bg="#4e5d6c", fg="white").pack(pady=5)
entry_process_size_dynamic = tk.Entry(dynamic_frame)
entry_process_size_dynamic.pack(pady=5)

tk.Button(dynamic_frame, text="Agregar Proceso Dinámico", command=add_process_dynamic).pack(pady=10)
tk.Button(dynamic_frame, text="Compactar Memoria", command=compact_dynamic_memory).pack(pady=10)

# Pestaña Paginación
paging_frame = tk.Frame(tab_control, bg="#4e5d6c")
tab_control.add(paging_frame, text="Paginación")

# Etiqueta y campo para ID del Proceso
tk.Label(paging_frame, text="ID del Proceso:", bg="#4e5d6c", fg="white").grid(row=0, column=0, pady=10)
entry_process_id_paging = tk.Entry(paging_frame)
entry_process_id_paging.grid(row=0, column=1, pady=10)

# Etiqueta y campo para tamaño del proceso
tk.Label(paging_frame, text="Tamaño del Proceso:", bg="#4e5d6c", fg="white").grid(row=1, column=0, pady=10)
entry_process_size_paging = tk.Entry(paging_frame)
entry_process_size_paging.grid(row=1, column=1, pady=10)

# Etiqueta y campo para tamaño de la página
tk.Label(paging_frame, text="Tamaño de Página:", bg="#4e5d6c", fg="white").grid(row=2, column=0, pady=10)
entry_page_size_paging = tk.Entry(paging_frame)
entry_page_size_paging.grid(row=2, column=1, pady=10)

# Elegir algoritmo de reemplazo de páginas
tk.Label(paging_frame, text="Algoritmo de Reemplazo:", bg="#4e5d6c", fg="white").grid(row=3, column=0, pady=10)
algorithm_choice = ttk.Combobox(paging_frame, values=["FIFO", "LRU", "Reloj"])
algorithm_choice.grid(row=3, column=1, pady=10)

tk.Button(paging_frame, text="Asignar Páginas", command=assign_pages).grid(row=4, column=0, columnspan=2, pady=10)

# Pestaña Segmentación
segmentation_frame = tk.Frame(tab_control, bg="#4e5d6c")
tab_control.add(segmentation_frame, text="Segmentación")

# Campos y botones para segmentación
tk.Label(segmentation_frame, text="ID del Proceso:", bg="#4e5d6c", fg="white").grid(row=0, column=0, pady=10)
entry_process_id_segmentation = tk.Entry(segmentation_frame)
entry_process_id_segmentation.grid(row=0, column=1, pady=10)

tk.Label(segmentation_frame, text="Tamaño del Proceso:", bg="#4e5d6c", fg="white").grid(row=1, column=0, pady=10)
entry_process_size_segmentation = tk.Entry(segmentation_frame)
entry_process_size_segmentation.grid(row=1, column=1, pady=10)

tk.Label(segmentation_frame, text="Número de Segmentos:", bg="#4e5d6c", fg="white").grid(row=2, column=0, pady=10)
entry_num_segments = tk.Entry(segmentation_frame)
entry_num_segments.grid(row=2, column=1, pady=10)

tk.Button(segmentation_frame, text="Agregar Proceso Segmentado", command=add_process_segmentation).grid(row=3, column=0, columnspan=2, pady=10)

# Canvas para mostrar el estado de la memoria
memory_canvas = tk.Canvas(root, width=800, height=300, bg="black")
memory_canvas.pack(pady=20)

# Label para mostrar el estado de la memoria
memory_label = tk.Label(root, text="", fg="white", bg="black", font=("Helvetica", 10))
memory_label.pack(pady=10)

root.mainloop()
