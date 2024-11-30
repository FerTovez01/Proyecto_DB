class MemorySimulator:
    def __init__(self, total_memory, page_size):
        # Aseguramos que el total de memoria sea divisible por el tamaño de la página
        if total_memory % page_size != 0:
            raise ValueError("El tamaño total de la memoria debe ser divisible por el tamaño de la página.")
        
        self.total_memory = total_memory
        self.page_size = page_size
        self.num_pages = total_memory // page_size  # Calcular número de páginas
        self.fixed_partitions = [None] * (self.total_memory // page_size)  # Inicializa la memoria fija
        self.dynamic_partitions = [{'start': 0, 'size': total_memory, 'status': 'free', 'process_id': None}]  # Inicializa una partición dinámica
        self.virtual_memory = [None] * self.num_pages
        self.page_table = {}
        self.use_bits = []

    def fixed_partitioning(self, partition_size):
        """Inicializa las particiones fijas."""
        self.fixed_partitions = [None] * (self.total_memory // partition_size)
        self.partition_size = partition_size

    def add_process_fixed(self, process_id, process_size):
        """ Agrega un proceso a una partición fija. """
        for i, partition in enumerate(self.fixed_partitions):
            if partition is None:  # Si la partición está libre
                if self.page_size <= process_size:
                    # Asignar el proceso a la partición
                    self.fixed_partitions[i] = process_id
                    internal_frag = self.page_size - process_size  # Fragmentación interna
                    print(f"Proceso {process_id} asignado a la partición {i + 1} con {internal_frag} bytes de fragmentación interna.")
                    return f"Proceso {process_id} agregado con {internal_frag} bytes de fragmentación interna."
                else:
                    return f"El proceso {process_id} es demasiado grande para esta partición."
        return "No hay particiones disponibles."

    def dynamic_partitioning(self):
        """ Inicializa la memoria dinámica con particiones libres. """
        # Aquí se puede inicializar la memoria dinámica con particiones de tamaño flexible
        self.dynamic_partitions = [{'start': 0, 'size': self.total_memory, 'status': 'free', 'process_id': None}]

    def add_process_dynamic(self, process_id, process_size):
        """ Asigna un proceso a una partición dinámica. """
        for partition in self.dynamic_partitions:
            if partition['status'] == 'free' and partition['size'] >= process_size:
                # Asignar el proceso a esta partición
                internal_frag = partition['size'] - process_size  # Fragmentación interna
                partition['status'] = 'occupied'
                partition['process_id'] = process_id
                
                # Si hay fragmentación interna, dividir la partición
                if internal_frag > 0:
                    # Crear una nueva partición libre después del proceso
                    new_partition = {'start': partition['start'] + process_size, 
                                     'size': internal_frag, 
                                     'status': 'free', 
                                     'process_id': None}
                    self.dynamic_partitions.append(new_partition)
                
                print(f"Proceso {process_id} agregado al bloque de memoria con {internal_frag} bytes de fragmentación interna.")
                return f"Proceso {process_id} agregado al bloque de memoria con {internal_frag} bytes de fragmentación interna."
        return "No hay suficiente espacio para el proceso."

    def display_memory(self):
        """ Muestra el estado de la memoria dinámica. """
        return "\n".join([f"Partición desde {partition['start']} bytes, tamaño: {partition['size']} bytes, Estado: {'Libre' if partition['status'] == 'free' else 'Ocupado'}, Proceso: {partition['process_id'] if partition['process_id'] else 'N/A'}" 
                          for partition in self.dynamic_partitions])

    def compact_memory(self):
        """ Compacta la memoria dinámica, moviendo los procesos. """
        free_partitions = [partition for partition in self.dynamic_partitions if partition['status'] == 'free']
        occupied_partitions = [partition for partition in self.dynamic_partitions if partition['status'] == 'occupied']
        
        # Compactar: Mover las particiones ocupadas al inicio de la memoria
        compacted_memory = occupied_partitions + free_partitions
        self.dynamic_partitions = compacted_memory

        # Ajustar las posiciones de las particiones ocupadas
        current_start = 0
        for partition in self.dynamic_partitions:
            partition['start'] = current_start
            current_start += partition['size']

        return "Memoria dinámica compactada exitosamente."


    def paging(self, process_id, process_size, page_size):
        """Simula la paginación del proceso."""
        num_pages = (process_size // page_size) + (1 if process_size % page_size != 0 else 0)
        frames_needed = num_pages

        for i in range(len(self.virtual_memory)):
            if self.virtual_memory[i] is None:
                self.virtual_memory[i] = process_id
                frames_needed -= 1
                if frames_needed == 0:
                    return f"Proceso {process_id} asignado con {num_pages} páginas."
        return f"No hay suficiente espacio en la memoria virtual para el proceso {process_id}."

    def replace_page_fifo(self, page_table, process_id):
        """Algoritmo FIFO para reemplazo de páginas."""
        for page, pid in page_table.items():
            if pid == process_id:
                page_table[page] = None
                break
        return "Página reemplazada con el algoritmo FIFO."

    def replace_page_lru(self, page_table, process_id):
        """Algoritmo LRU para reemplazo de páginas."""
        if process_id in page_table.values():
            for page, pid in page_table.items():
                if pid == process_id:
                    page_table[page] = None
                    break
        return "Página reemplazada con el algoritmo LRU."

    def replace_page_clock(self, page_table, process_id, use_bits):
        """Algoritmo de reloj para reemplazo de páginas."""
        for i, page in enumerate(page_table):
            if page_table[page] == process_id and use_bits[i] == 0:
                page_table[page] = None
                use_bits[i] = 0
                break
        return "Página reemplazada con el algoritmo Reloj."

    def add_process_segments(self, process_id, process_size, num_segments):
        """Simula la segmentación de un proceso."""
        segment_size = process_size // num_segments
        segments_needed = num_segments

        for i in range(len(self.virtual_memory)):
            if self.virtual_memory[i] is None:
                self.virtual_memory[i] = process_id
                segments_needed -= 1
                if segments_needed == 0:
                    return f"Proceso {process_id} asignado con {num_segments} segmentos."
        return f"No hay suficiente espacio en la memoria virtual para el proceso {process_id}."

    def display_memory(self):
        """Devuelve el estado de la memoria como una cadena."""
        memory_display = "Estado de la Memoria Física:\n"
        memory_display += "Memoria Fija:\n"
        for i, block in enumerate(self.fixed_partitions):
            memory_display += f"Bloque {i + 1}: {'Libre' if block is None else block}\n"
        
        memory_display += "\nMemoria Dinámica:\n"
        for i, block in enumerate(self.dynamic_partitions):
            memory_display += f"Posición {i + 1}: {'Libre' if block is None else block}\n"

        memory_display += "\nMemoria Virtual:\n"
        for i, page in enumerate(self.virtual_memory):
            memory_display += f"Página {i + 1}: {'Libre' if page is None else page}\n"

        return memory_display
