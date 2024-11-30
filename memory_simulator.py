class MemorySimulator:
    def __init__(self, total_memory, page_size):
        # Aseguramos que el total de memoria sea divisible por el tamaño de la página
        if total_memory % page_size != 0:
            raise ValueError("El tamaño total de la memoria debe ser divisible por el tamaño de la página.")
        
        self.total_memory = total_memory
        self.page_size = page_size
        self.num_pages = total_memory // page_size  # Calcular número de páginas
        self.fixed_partitions = [None] * total_memory
        self.dynamic_partitions = []
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
        """Inicializa la memoria dinámica."""
        self.dynamic_partitions = [None] * self.total_memory

    def add_process_dynamic(self, process_id, process_size):
        """Agrega un proceso a la memoria dinámica."""
        for i in range(self.total_memory - process_size + 1):
            if all(self.dynamic_partitions[i + j] is None for j in range(process_size)):
                for j in range(process_size):
                    self.dynamic_partitions[i + j] = process_id
                return f"Proceso {process_id} agregado exitosamente en memoria dinámica."
        return f"No hay suficiente espacio para el proceso {process_id}."

    def compact_memory(self):
        """Compacta la memoria dinámica, moviendo los procesos."""
        compacted_memory = [None] * self.total_memory
        current_index = 0
        for i in range(self.total_memory):
            if self.dynamic_partitions[i] is not None:
                compacted_memory[current_index] = self.dynamic_partitions[i]
                current_index += 1
        self.dynamic_partitions = compacted_memory
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
