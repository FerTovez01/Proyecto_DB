
# Simulador_Gestion_Memoria
 Este proyecto es una aplicación gráfica desarrollada en Python que simula diferentes técnicas de gestión de memoria en sistemas operativos. 
 La aplicación utiliza la librería `tkinter` para su interfaz gráfica, permitiendo a los usuarios interactuar con las siguientes técnicas de gestión de memoria:

- Particionamiento Fijo.
- Particionamiento Dinámico.
- Paginación (con algoritmos como FIFO, LRU y Reloj).
- Segmentación.



## Descripcion
El simulador proporciona una manera interactiva y visual de entender y gestionar la memoria mediante técnicas de particionamiento fijo, particionamiento dinámico, paginación, segmentación y algoritmos de reemplazo de páginas. Los usuarios pueden agregar procesos, compactar memoria y visualizar el estado de la memoria en tiempo real. Incluye una interfaz grafica de usuario (GUI) para facilitar la interacción y visualización de los resultados.


## Caracteristicas

- **Simulador de memoria:**:  Implementa particionamiento fijo, dinámico, paginación y segmentación.

- **Interfaz gráfica**: Usando tkinter, con pestañas y controles interactivos.

- **Representación visual**:Muestra el estado de la memoria física y virtual en un canvas.

- **Simulacion de Procesos**:  Los usuarios pueden agregar procesos a la memoria con diferentes esquemas de particionamiento.

-**Algoritmos de reemplazo de páginas**:FIFO, LRU y Reloj para manejar la paginación.

**Compactación de memoria**: Para optimizar la memoria dinámica.

**Manejo de errores**: Mensajes claros si los valores introducidos no son válidos.


## Captura de Pantalla

![Imagen de la interfaz](![alt text](image-1.png))



## Uso

1. **Particionamiento Fijo:** 

**Tamaño de Partición**:Este campo permite que el usuario ingrese el tamaño de la partición en la memoria que se desea utilizar para los procesos. Es un campo de texto que se usa para configurar el tamaño de las particiones fijas que se crearán.

**ID del Proceso**:Aquí, el usuario puede ingresar un identificador único para el proceso que va a agregar a la memoria.

**Tamaño del Proceso**:Este campo permite al usuario especificar el tamaño del proceso que se desea agregar a la partición de memoria.

**Botón "Inicializar"**:Este botón sirve para inicializar las particiones fijas en la memoria con el tamaño especificado en el campo de Tamaño de Partición.

**Botón "Agregar Proceso"**:Este botón agrega el proceso con el ID del Proceso y el Tamaño del Proceso a las particiones fijas de la memoria.

Cuando el usuario hace clic en el botón Inicializar, se ejecuta la función initialize_fixed(), que toma el tamaño de partición ingresado y llama al método fixed_partitioning() para dividir la memoria en bloques fijos.

Cuando se hace clic en Agregar Proceso, se ejecuta add_process_fixed(), que toma el ID y el tamaño del proceso y los agrega a la memoria a través de la función add_process_fixed(), como se detalla en el código anterior.

2. **Particionamiento Dinamico**

**Inicialización Dinámica**: En el código, esto podría estar relacionado con una función similar a initialize_dynamic(), que configura la memoria para trabajar con particionamiento dinámico.

**Agregar Proceso Dinámico**: La función que se encargaría de esto sería algo como add_process_dynamic(), que toma el ID y el tamaño del proceso y lo agrega a la memoria, ajustándose dinámicamente.

**Compactar Memoria**: Esto probablemente esté relacionado con una función llamada compact_memory() o algo similar, que reorganiza los procesos en la memoria para eliminar la fragmentación y mejorar la eficiencia del uso de la memoria.


3. **Paginacion**

**Campo "ID Proceso"**:Este campo permite ingresar un ID único de proceso que se utilizará para identificar al proceso que se va a asignar en la memoria virtual mediante paginación.

**Campo "Tamaño del Proceso"**:Aquí el usuario ingresa el tamaño del proceso que se va a asignar en la memoria. Este tamaño podría dividirse en varias páginas, dependiendo del tamaño de página configurado.

**Campo "Tamaño de Página"**:En este campo, se define el tamaño de cada página en la memoria virtual. Este valor es importante porque determina cuántas páginas ocupará el proceso, y cuánto espacio de memoria se asignará a cada página.

**Campo "Algoritmo de Reemplazo"**:Este es un menú desplegable que permite seleccionar el algoritmo de reemplazo de páginas a utilizar cuando la memoria virtual esté llena. Algunos algoritmos comunes son:
FIFO (First-In-First-Out): El proceso más antiguo en la memoria será el primero en ser reemplazado.
LRU (Least Recently Used): Se reemplaza la página que no ha sido utilizada durante más tiempo.
Random: Se selecciona una página al azar para reemplazar.

**Botón "Asignar Páginas"**: Al hacer clic en este botón, se ejecuta una función que asigna las páginas del proceso en la memoria virtual. El proceso será dividido en páginas del tamaño especificado, y las páginas serán asignadas de acuerdo con el algoritmo de reemplazo seleccionado si la memoria está llena.


**Asignación de Páginas**: La función que se ejecuta al hacer clic en "Asignar Páginas" tomará el ID del proceso, el tamaño del proceso, el tamaño de página, y el algoritmo de reemplazo. Esta función podría dividir el proceso en varias páginas y asignarlas a la memoria virtual. Si la memoria está llena, se utilizará el algoritmo de reemplazo seleccionado para decidir qué página debe ser reemplazada.

**Algoritmo de Reemplazo**: Dependiendo del algoritmo seleccionado en el menú desplegable, el código debe implementar una lógica para reemplazar las páginas. Este algoritmo determinará qué páginas de la memoria se eliminarán para hacer espacio para nuevas páginas cuando la memoria se llene.



4. **Segmentacion**

**Campo "ID del Proceso"**:Permite al usuario ingresar un identificador único para el proceso que será segmentado. 
Este ID ayuda a identificar y gestionar el proceso dentro de la memoria.

**Campo "Tamaño del Proceso"**:Aquí se ingresa el tamaño total del proceso en la memoria. 
Este tamaño será dividido en segmentos, dependiendo del número de segmentos definido.

**Campo "Número de Segmentos"**:En este campo, el usuario especifica cuántos segmentos tendrá el proceso. 
Cada segmento corresponde a una parte lógica del proceso (como código, datos, pila, etc.).


**Botón "Agregar Proceso Segmentado"**:Al hacer clic, se ejecuta una función que:
- Divide el proceso en el número de segmentos especificados.
- Asigna cada segmento a una región de memoria contigua o dispersa, dependiendo del estado de la memoria.
- Actualiza la representación gráfica o interna de la memoria para reflejar la asignación de segmentos.

**Visualización**
La interfaz gráfica incluye:

Memoria Física: Bloques representados como rectángulos verdes (libres) o rojos (ocupados).
Memoria Virtual: Páginas representadas como rectángulos azules (libres) o amarillos (ocupados).


## Requisitos

Antes de ejecutar este proyecto, asegúrate de tener instalado lo siguiente:

- **Python 3.13**
- La librería estándar `tkinter` (generalmente incluida en la instalación de Python).
- El archivo `memory_simulator.py` (contiene la lógica del simulador de memoria).


## Instalación
1. Clona este repositorio:
   ```bash
   git clone https://github.com/FerTovez01/Proyecto_DB.git


## Estructura del Proyecto


main.py               # Archivo principal para ejecutar el simulador
interfaz.py           # Archivo que contiene la lógica de la interfaz gráfica
gestion_memoria.py    # Archivo que implementa la lógica de gestión de memoria
README.md             # Este archivo de documentación


## Archivos del Proyecto
- **`gui.py`**: Contiene el código relacionado con la interfaz gráfica de usuario del simulador.
- **`memory_simulator.py`**: Contiene la lógica principal del simulador, incluyendo los algoritmos de gestión de memoria para esquemas fijos y dinámicos.

## Uso
1. Ejecuta el archivo `gui.py` para iniciar la interfaz gráfica: `python gui.py`
2. Interactúa con la GUI para simular la gestión de memoria en esquemas fijos , dinámicos, paginacion y segmentacion.
