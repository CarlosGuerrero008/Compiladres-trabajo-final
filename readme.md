DSL para Consultas Dinámicas sobre Inventarios CSV
Objetivo del Proyecto
Este proyecto consiste en diseñar, implementar e interpretar un mini-compilador funcional basado en un Lenguaje de Dominio Específico (DSL) para realizar consultas dinámicas sobre archivos CSV con datos de inventario. Utilizando ANTLR4 y Python, el DSL permite cargar archivos, aplicar filtros, realizar agregaciones y mostrar resultados de forma secuencial y clara.


Tecnologías y Herramientas Usadas
ANTLR4: para definir la gramática del DSL, generar el lexer y parser en Python.

Python 3: para implementar el visitor e intérprete que ejecuta las instrucciones del DSL.

Pandas: para manejar y procesar los datos CSV fácilmente.

Java (JDK): para ejecutar ANTLR4 y generar el código fuente del lexer y parser.


Explicación de la Gramática
La gramática define las reglas y tokens que componen el lenguaje específico para consultas de inventario. Incluye instrucciones para:

Cargar un archivo CSV: load "archivo.csv";
Filtrar datos con condiciones sobre columnas: filter column "categoria" = "Escolar";
Realizar funciones agregadas: aggregate count column "id_producto";
Imprimir resultados: print;

Estas reglas permiten escribir scripts que ejecutan consultas complejas y secuenciales.
Cómo Generar el Lexer y Parser con ANTLR4
Primero, coloca el archivo InventarioDSL.g4 con la gramática en tu carpeta de trabajo.
Luego, ejecuta los siguientes comandos para generar los archivos en Python:

java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 InventarioDSL.g4
Este comando genera el lexer y parser.

Para generar también la clase visitor, que facilita la interpretación, usa:

java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor InventarioDSL.g4
Esto crea los archivos:
InventarioDSLLexer.py
InventarioDSLParser.py
InventarioDSLVisitor.py


Implementación del Visitor (myvisitor.py)
El Visitor es una clase que "visita" cada nodo del árbol de análisis sintáctico generado por ANTLR y define qué hacer en cada tipo de instrucción del DSL.
En este proyecto, el visitor carga el archivo CSV, acumula filtros y agregaciones, y al final procesa y muestra los resultados.
Usamos el patrón Visitor para separar la lógica del lenguaje (gramática) de la lógica de procesamiento (acciones).


El Intérprete (interpreter.py)
El intérprete lee el script DSL, ejecuta el lexer y parser para crear el árbol sintáctico, y luego usa el visitor para interpretar el árbol.
El flujo es:

Leer archivo .dsl
Tokenizar y parsear con ANTLR
Visitar el árbol con InventarioVisitor para ejecutar la consulta
Mostrar resultados

Configuración del Main
Para correr el intérprete, usa la consola con:


python interpreter.py consulta.dsl
Esto ejecuta el script DSL con el visitor y muestra resultados.

Modos de Ejecución y Comandos
Ejecutar consulta normal:


python interpreter.py consulta.dsl 1
Ejecuta la consulta #1 del archivo consulta.dsl.

Mostrar tokens generados:


python interpreter.py consulta.dsl tokens 1
Muestra la lista de tokens generados para la consulta #1, útil para debugging léxico.

Mostrar árbol sintáctico:


python interpreter.py consulta.dsl tree 1
Imprime el árbol de análisis sintáctico para la consulta #1, para ver la estructura del parseo.

Ejecutar interfaz gráfica de ANTLR para depuración:


python interpreter.py consulta.dsl gui
Abre una ventana gráfica que permite ver el parseo y el árbol de forma visual (requiere configuración adicional).

Resumen
Este proyecto muestra cómo construir un lenguaje específico para consultas dinámicas en inventarios, desde la definición de la gramática, generación del parser con ANTLR, implementación del visitor para interpretar el lenguaje, hasta la ejecución de scripts para consultar datos reales en CSV.

