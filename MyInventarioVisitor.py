import pandas as pd
from InventarioDSLVisitor import InventarioDSLVisitor

class MyInventarioVisitor(InventarioDSLVisitor):
    def __init__(self):
        self.data = None

    def visitLoadStmt(self, ctx):
        file_name = ctx.STRING().getText().strip('"')
        print(f"Archivo cargado: {file_name}")
        self.data = pd.read_csv(file_name)

    def visitFilterStmt(self, ctx):
        column = ctx.STRING().getText().strip('"')

        if ctx.BETWEEN() is not None:
            values = ctx.value()
            min_value_text = values[0].getText()
            max_value_text = values[1].getText()

            if min_value_text.startswith('"') and min_value_text.endswith('"'):
                min_value = min_value_text.strip('"')
                max_value = max_value_text.strip('"')
            else:
                try:
                    min_value = float(min_value_text)
                    max_value = float(max_value_text)
                except ValueError:
                    min_value = min_value_text
                    max_value = max_value_text

            print(f"Filtro aplicado: {column} BETWEEN {min_value} AND {max_value}")
            self.data = self.data[(self.data[column] >= min_value) & (self.data[column] <= max_value)]

        else:
            operator = ctx.comparisonOperator().getText()
            value_text = ctx.value(0).getText()

            if value_text.startswith('"') and value_text.endswith('"'):
                value = value_text.strip('"')
            else:
                try:
                    value = float(value_text)
                except ValueError:
                    value = value_text

            print(f"Filtro aplicado: {column} {operator} {value}")

            if operator == '>':
                self.data = self.data[self.data[column] > value]
            elif operator == '<':
                self.data = self.data[self.data[column] < value]
            elif operator == '=':
                self.data = self.data[self.data[column] == value]
            elif operator == '>=':
                self.data = self.data[self.data[column] >= value]
            elif operator == '<=':
                self.data = self.data[self.data[column] <= value]

    def visitAggregateStmt(self, ctx):
        # Aquí corregimos para que use getChild() según la gramática
        function_name = ctx.getChild(1).getText()  # aggregationOperator
        column = ctx.getChild(3).getText().strip('"')  # STRING

        print(f"Agregación: {function_name} sobre {column}")

        if self.data is None:
            print("Error: no hay datos cargados")
            return

        func = function_name.lower()

        if func == "count":
            result = len(self.data[column])
        elif func == "sum":
            result = self.data[column].sum()
        elif func == "average":
            result = self.data[column].mean()
        else:
            result = None
            print(f"Función de agregación no soportada: {function_name}")

        print(f"Resultado de agregación: {result}")

    def visitPrintStmt(self, ctx):
        print("Resultado actual de datos:")
        print(self.data)
