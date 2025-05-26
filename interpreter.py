from antlr4 import *
from InventarioDSLLexer import InventarioDSLLexer
from InventarioDSLParser import InventarioDSLParser
from MyInventarioVisitor import MyInventarioVisitor
from antlr4.tree.Tree import TerminalNodeImpl
import sys
import pydot
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tempfile
import os
from PIL import Image




def run_query(dsl_code):
    input_stream = InputStream(dsl_code)
    lexer = InventarioDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = InventarioDSLParser(stream)
    tree = parser.script()
    visitor = MyInventarioVisitor()
    visitor.visit(tree)

def print_tokens(dsl_code):
    input_stream = InputStream(dsl_code)
    lexer = InventarioDSLLexer(input_stream)
    tokens = lexer.getAllTokens()
    print("Tokens de la consulta:")
    for t in tokens:
        print(f'Token: "{t.text}", Type: {t.type}, Line: {t.line}, Column: {t.column}')

def print_tree(node, parser, indent=0):
    pad = "  " * indent
    if isinstance(node, TerminalNodeImpl):
        print(f"{pad}Terminal: {node.getText()}")
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        print(f"{pad}{rule_name}")
        for i in range(node.getChildCount()):
            print_tree(node.getChild(i), parser, indent + 1)

def print_parse_tree(dsl_code):
    input_stream = InputStream(dsl_code)
    lexer = InventarioDSLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = InventarioDSLParser(stream)
    tree = parser.script()
    
    print_tree(tree, parser)

# --- Funciones para generar gráfico del árbol ---

def node_to_pydot(node, graph, parser):
    node_id = str(id(node))
    if node.getChildCount() == 0:
        label = node.getText()
        graph.add_node(pydot.Node(node_id, label=label, shape='box', style='filled', fillcolor='lightgrey'))
    else:
        rule_name = parser.ruleNames[node.getRuleIndex()]
        graph.add_node(pydot.Node(node_id, label=rule_name, shape='ellipse', style='filled', fillcolor='lightblue'))
        for i in range(node.getChildCount()):
            child = node.getChild(i)
            child_id = node_to_pydot(child, graph, parser)
            graph.add_edge(pydot.Edge(node_id, child_id))
    return node_id

def generate_tree_graph(dsl_code):
    try:
        input_stream = InputStream(dsl_code)
        lexer = InventarioDSLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = InventarioDSLParser(stream)
        tree = parser.script()

        graph = pydot.Dot(graph_type='digraph')
        node_to_pydot(tree, graph, parser)
        print("Árbol generado correctamente.")  # Debug
        return graph
    except Exception as e:
        print(f"Error en generate_tree_graph: {e}")
        raise

# --- GUI con Tkinter para mostrar árbol y exportar PNG ---

class TreeGUI:
    def __init__(self, master, queries):
        self.master = master
        self.queries = queries
        master.title("Árbol Sintáctico DSL")

        self.label = Label(master, text="Número de consulta:")
        self.label.pack(pady=(10, 0))

        self.entry = Entry(master)
        self.entry.pack()

        self.show_button = Button(master, text="Mostrar Árbol", command=self.show_tree)
        self.show_button.pack(pady=5)

        self.save_button = Button(master, text="Guardar PNG", command=self.save_png)
        self.save_button.pack(pady=5)

        self.canvas = Canvas(master, bg='white', height=300)
        self.canvas.pack(fill=BOTH, expand=True)

        self.graph = None
        self.img = None
        self.tmpfile = None

    def show_tree(self):
        try:
            index = int(self.entry.get()) - 1
            if index < 0 or index >= len(self.queries):
                messagebox.showwarning("Índice inválido", "Número fuera de rango.")
                return
            code = self.queries[index]
            self.graph = generate_tree_graph(code)
        except ValueError:
            messagebox.showwarning("Entrada inválida", "Por favor ingresa un número entero.")
            return
        except Exception as e:
            messagebox.showerror("Error", f"Error generando árbol: {e}")
            return

        with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as tmp:
            self.graph.write_png(tmp.name)
            self.display_image(tmp.name)
            self.tmpfile = tmp.name

    def display_image(self, filename):
        canvas_width = 700
        canvas_height = 300
        image = Image.open(filename)
        image = image.resize((canvas_width, canvas_height), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(image)
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=NW, image=self.img)

    def save_png(self):
        if self.graph is None:
            messagebox.showerror("Error", "Primero debes mostrar el árbol.")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".png",
                                                filetypes=[("PNG files","*.png")])
        if filename:
            self.graph.write_png(filename)
            messagebox.showinfo("Guardado", f"Árbol guardado en {filename}")

    def on_close(self):
        if self.tmpfile and os.path.exists(self.tmpfile):
            os.remove(self.tmpfile)
        self.master.destroy()

# --- Main modificado para aceptar consola o GUI ---

def main():
    # Si se pasa "gui" como argumento, abre la interfaz gráfica
    if len(sys.argv) >= 2 and sys.argv[1].lower().endswith(".dsl"):
        filename = sys.argv[1]
        with open(filename, "r", encoding="utf-8") as f:
            queries = f.read().split("print;")
        queries = [q.strip() + "\nprint;" for q in queries if q.strip()]

        if len(sys.argv) >= 3 and sys.argv[2].lower() == "gui":
            root = Tk()
            root.geometry("800x600")
            app = TreeGUI(root, queries)
            root.protocol("WM_DELETE_WINDOW", app.on_close)
            root.mainloop()
            return

    # Si no, ejecuta modo consola como antes
    if len(sys.argv) < 2:
        print("Se debe proporcionar un archivo DSL como argumento o 'gui' para interfaz gráfica.")
        return

    filename = sys.argv[1]
    with open(filename, "r", encoding="utf-8") as f:
        queries = f.read().split("print;")

    queries = [q.strip() + "\nprint;" for q in queries if q.strip()]

    if len(sys.argv) >= 3:
        option = sys.argv[2]

        if option == "tokens" and len(sys.argv) == 4:
            try:
                index = int(sys.argv[3]) - 1
                if 0 <= index < len(queries):
                    print(f"\n🔍 Tokens de la consulta #{index + 1}:\n")
                    print_tokens(queries[index])
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("El índice debe ser un número entero.")

        elif option == "tree" and len(sys.argv) == 4:
            try:
                index = int(sys.argv[3]) - 1
                if 0 <= index < len(queries):
                    print(f"\n🌳 Árbol de la consulta #{index + 1}:\n")
                    print_parse_tree(queries[index])
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("El índice debe ser un número entero.")

        else:
            try:
                index = int(sys.argv[2]) - 1
                if 0 <= index < len(queries):
                    print(f"\n✅ Ejecutando consulta #{index + 1}:\n")
                    run_query(queries[index])
                else:
                    print("Índice fuera de rango.")
            except ValueError:
                print("El argumento debe ser un número entero.")

    else:
        print(f"✅ Ejecutando todas las {len(queries)} consultas:\n")
        for i, query in enumerate(queries):
            print(f"\n🔹 Consulta #{i + 1}:\n")
            run_query(query)

if __name__ == '__main__':
    main()
