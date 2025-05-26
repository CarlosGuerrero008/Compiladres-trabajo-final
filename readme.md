                                                                DSL para Consultas Dinámicas sobre Inventarios CSV
Objetivo del Proyecto
    Diseñar e implementar un mini-compilador funcional basado en un Lenguaje de Dominio Específico (DSL), que permita realizar consultas dinámicas y secuenciales sobre archivos CSV de inventarios. Se usa ANTLR4 y Python para procesar, filtrar y agregar datos de forma sencilla y extensible.


Tecnologías Utilizadas
    ANTLR4: Definición de la gramática y generación de lexer/parser en Python.
    Python 3: Implementación del visitor e intérprete para ejecutar consultas.
    Pandas: Manipulación eficiente de datos CSV.


Explicación de la Gramática

    El DSL permite comandos secuenciales para:
        Carga de archivos CSV:
        load "inventario.csv";

    Filtrado de registros:
    filter column "categoria" = "Escolar";

    Agregaciones:
    Contar registros: aggregate count column "id_producto";
    Sumar valores: aggregate sum column "cantidad_stock";
    Calcular promedio: aggregate average column "precio_unitario";

    Mostrar resultados:
    print;

    Esta gramática facilita consultas claras y fáciles de modificar.


Generación del Lexer y Parser con ANTLR4

    Ejecuta los comandos en la terminal para generar los archivos Python necesarios:

        java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 InventarioDSL.g4
        Para generar además el visitor:
        java -jar antlr-4.13.2-complete.jar -Dlanguage=Python3 -visitor InventarioDSL.g4

    Archivos generados:

        InventarioDSLLexer.py

        InventarioDSLParser.py

        InventarioDSLVisitor.py


Visitor: ¿Qué es y cómo se usa?

    El visitor es una clase que recorre el árbol sintáctico generado por ANTLR para ejecutar las acciones definidas en el DSL. En nuestro proyecto:

    Carga el CSV

    Acumula filtros y agregaciones

    Ejecuta las operaciones y muestra resultados

    El patrón visitor ayuda a separar la lógica de análisis del procesamiento real.


Intérprete (interpreter.py)

    El intérprete es el programa principal que:

    Lee el archivo .dsl con las instrucciones.

    Tokeniza y parsea el contenido usando ANTLR.

    Usa el visitor para ejecutar las consultas.

    Muestra los resultados en consola.

Uso y Comandos

    python interpreter.py consulta.dsl 1
    Ejecuta la consulta número 1 en el archivo consulta.dsl.

Mostrar tokens:

    python interpreter.py consulta.dsl tokens 1
    Muestra los tokens léxicos para la consulta #1.

Mostrar árbol sintáctico:

    python interpreter.py consulta.dsl tree 1
    Imprime la estructura del árbol sintáctico para la consulta #1.

Abrir interfaz gráfica ANTLR:

    python interpreter.py consulta.dsl gui
    Muestra un GUI para explorar el árbol (requiere configuración adicional).