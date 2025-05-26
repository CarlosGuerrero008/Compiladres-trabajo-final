# Generated from InventarioDSL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .InventarioDSLParser import InventarioDSLParser
else:
    from InventarioDSLParser import InventarioDSLParser

# This class defines a complete generic visitor for a parse tree produced by InventarioDSLParser.

class InventarioDSLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InventarioDSLParser#script.
    def visitScript(self, ctx:InventarioDSLParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#statement.
    def visitStatement(self, ctx:InventarioDSLParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#loadStmt.
    def visitLoadStmt(self, ctx:InventarioDSLParser.LoadStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#filterStmt.
    def visitFilterStmt(self, ctx:InventarioDSLParser.FilterStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#aggregateStmt.
    def visitAggregateStmt(self, ctx:InventarioDSLParser.AggregateStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#printStmt.
    def visitPrintStmt(self, ctx:InventarioDSLParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#comparisonOperator.
    def visitComparisonOperator(self, ctx:InventarioDSLParser.ComparisonOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#aggregationOperator.
    def visitAggregationOperator(self, ctx:InventarioDSLParser.AggregationOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InventarioDSLParser#value.
    def visitValue(self, ctx:InventarioDSLParser.ValueContext):
        return self.visitChildren(ctx)



del InventarioDSLParser