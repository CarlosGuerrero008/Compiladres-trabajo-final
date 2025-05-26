# Generated from InventarioDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .InventarioDSLParser import InventarioDSLParser
else:
    from InventarioDSLParser import InventarioDSLParser

# This class defines a complete listener for a parse tree produced by InventarioDSLParser.
class InventarioDSLListener(ParseTreeListener):

    # Enter a parse tree produced by InventarioDSLParser#script.
    def enterScript(self, ctx:InventarioDSLParser.ScriptContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#script.
    def exitScript(self, ctx:InventarioDSLParser.ScriptContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#statement.
    def enterStatement(self, ctx:InventarioDSLParser.StatementContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#statement.
    def exitStatement(self, ctx:InventarioDSLParser.StatementContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#loadStmt.
    def enterLoadStmt(self, ctx:InventarioDSLParser.LoadStmtContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#loadStmt.
    def exitLoadStmt(self, ctx:InventarioDSLParser.LoadStmtContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#filterStmt.
    def enterFilterStmt(self, ctx:InventarioDSLParser.FilterStmtContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#filterStmt.
    def exitFilterStmt(self, ctx:InventarioDSLParser.FilterStmtContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#aggregateStmt.
    def enterAggregateStmt(self, ctx:InventarioDSLParser.AggregateStmtContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#aggregateStmt.
    def exitAggregateStmt(self, ctx:InventarioDSLParser.AggregateStmtContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#printStmt.
    def enterPrintStmt(self, ctx:InventarioDSLParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#printStmt.
    def exitPrintStmt(self, ctx:InventarioDSLParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#comparisonOperator.
    def enterComparisonOperator(self, ctx:InventarioDSLParser.ComparisonOperatorContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#comparisonOperator.
    def exitComparisonOperator(self, ctx:InventarioDSLParser.ComparisonOperatorContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#aggregationOperator.
    def enterAggregationOperator(self, ctx:InventarioDSLParser.AggregationOperatorContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#aggregationOperator.
    def exitAggregationOperator(self, ctx:InventarioDSLParser.AggregationOperatorContext):
        pass


    # Enter a parse tree produced by InventarioDSLParser#value.
    def enterValue(self, ctx:InventarioDSLParser.ValueContext):
        pass

    # Exit a parse tree produced by InventarioDSLParser#value.
    def exitValue(self, ctx:InventarioDSLParser.ValueContext):
        pass



del InventarioDSLParser