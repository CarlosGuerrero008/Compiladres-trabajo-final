# Generated from InventarioDSL.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,20,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,3,1,3,1,3,1,3,3,3,50,8,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,
        5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,
        3,1,0,7,11,1,0,12,14,1,0,17,18,62,0,19,1,0,0,0,2,27,1,0,0,0,4,29,
        1,0,0,0,6,49,1,0,0,0,8,51,1,0,0,0,10,57,1,0,0,0,12,60,1,0,0,0,14,
        62,1,0,0,0,16,64,1,0,0,0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,
        0,21,19,1,0,0,0,21,22,1,0,0,0,22,1,1,0,0,0,23,28,3,4,2,0,24,28,3,
        6,3,0,25,28,3,8,4,0,26,28,3,10,5,0,27,23,1,0,0,0,27,24,1,0,0,0,27,
        25,1,0,0,0,27,26,1,0,0,0,28,3,1,0,0,0,29,30,5,1,0,0,30,31,5,17,0,
        0,31,32,5,2,0,0,32,5,1,0,0,0,33,34,5,3,0,0,34,35,5,4,0,0,35,36,5,
        17,0,0,36,37,3,12,6,0,37,38,3,16,8,0,38,39,5,2,0,0,39,50,1,0,0,0,
        40,41,5,3,0,0,41,42,5,4,0,0,42,43,5,17,0,0,43,44,5,15,0,0,44,45,
        3,16,8,0,45,46,5,16,0,0,46,47,3,16,8,0,47,48,5,2,0,0,48,50,1,0,0,
        0,49,33,1,0,0,0,49,40,1,0,0,0,50,7,1,0,0,0,51,52,5,5,0,0,52,53,3,
        14,7,0,53,54,5,4,0,0,54,55,5,17,0,0,55,56,5,2,0,0,56,9,1,0,0,0,57,
        58,5,6,0,0,58,59,5,2,0,0,59,11,1,0,0,0,60,61,7,0,0,0,61,13,1,0,0,
        0,62,63,7,1,0,0,63,15,1,0,0,0,64,65,7,2,0,0,65,17,1,0,0,0,3,21,27,
        49
    ]

class InventarioDSLParser ( Parser ):

    grammarFileName = "InventarioDSL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'load'", "';'", "'filter'", "'column'", 
                     "'aggregate'", "'print'", "'>'", "'<'", "'='", "'>='", 
                     "'<='", "'count'", "'sum'", "'average'", "'between'", 
                     "'and'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "BETWEEN", 
                      "AND", "STRING", "NUMERIC", "ID", "WS" ]

    RULE_script = 0
    RULE_statement = 1
    RULE_loadStmt = 2
    RULE_filterStmt = 3
    RULE_aggregateStmt = 4
    RULE_printStmt = 5
    RULE_comparisonOperator = 6
    RULE_aggregationOperator = 7
    RULE_value = 8

    ruleNames =  [ "script", "statement", "loadStmt", "filterStmt", "aggregateStmt", 
                   "printStmt", "comparisonOperator", "aggregationOperator", 
                   "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    BETWEEN=15
    AND=16
    STRING=17
    NUMERIC=18
    ID=19
    WS=20

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ScriptContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InventarioDSLParser.StatementContext)
            else:
                return self.getTypedRuleContext(InventarioDSLParser.StatementContext,i)


        def getRuleIndex(self):
            return InventarioDSLParser.RULE_script

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScript" ):
                listener.enterScript(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScript" ):
                listener.exitScript(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitScript" ):
                return visitor.visitScript(self)
            else:
                return visitor.visitChildren(self)




    def script(self):

        localctx = InventarioDSLParser.ScriptContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_script)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 106) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loadStmt(self):
            return self.getTypedRuleContext(InventarioDSLParser.LoadStmtContext,0)


        def filterStmt(self):
            return self.getTypedRuleContext(InventarioDSLParser.FilterStmtContext,0)


        def aggregateStmt(self):
            return self.getTypedRuleContext(InventarioDSLParser.AggregateStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(InventarioDSLParser.PrintStmtContext,0)


        def getRuleIndex(self):
            return InventarioDSLParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = InventarioDSLParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.loadStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.filterStmt()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 3)
                self.state = 25
                self.aggregateStmt()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 26
                self.printStmt()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LoadStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(InventarioDSLParser.STRING, 0)

        def getRuleIndex(self):
            return InventarioDSLParser.RULE_loadStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoadStmt" ):
                listener.enterLoadStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoadStmt" ):
                listener.exitLoadStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLoadStmt" ):
                return visitor.visitLoadStmt(self)
            else:
                return visitor.visitChildren(self)




    def loadStmt(self):

        localctx = InventarioDSLParser.LoadStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_loadStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(InventarioDSLParser.T__0)
            self.state = 30
            self.match(InventarioDSLParser.STRING)
            self.state = 31
            self.match(InventarioDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(InventarioDSLParser.STRING, 0)

        def comparisonOperator(self):
            return self.getTypedRuleContext(InventarioDSLParser.ComparisonOperatorContext,0)


        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InventarioDSLParser.ValueContext)
            else:
                return self.getTypedRuleContext(InventarioDSLParser.ValueContext,i)


        def BETWEEN(self):
            return self.getToken(InventarioDSLParser.BETWEEN, 0)

        def AND(self):
            return self.getToken(InventarioDSLParser.AND, 0)

        def getRuleIndex(self):
            return InventarioDSLParser.RULE_filterStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterStmt" ):
                listener.enterFilterStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterStmt" ):
                listener.exitFilterStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterStmt" ):
                return visitor.visitFilterStmt(self)
            else:
                return visitor.visitChildren(self)




    def filterStmt(self):

        localctx = InventarioDSLParser.FilterStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterStmt)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(InventarioDSLParser.T__2)
                self.state = 34
                self.match(InventarioDSLParser.T__3)
                self.state = 35
                self.match(InventarioDSLParser.STRING)
                self.state = 36
                self.comparisonOperator()
                self.state = 37
                self.value()
                self.state = 38
                self.match(InventarioDSLParser.T__1)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 40
                self.match(InventarioDSLParser.T__2)
                self.state = 41
                self.match(InventarioDSLParser.T__3)
                self.state = 42
                self.match(InventarioDSLParser.STRING)
                self.state = 43
                self.match(InventarioDSLParser.BETWEEN)
                self.state = 44
                self.value()
                self.state = 45
                self.match(InventarioDSLParser.AND)
                self.state = 46
                self.value()
                self.state = 47
                self.match(InventarioDSLParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregateStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def aggregationOperator(self):
            return self.getTypedRuleContext(InventarioDSLParser.AggregationOperatorContext,0)


        def STRING(self):
            return self.getToken(InventarioDSLParser.STRING, 0)

        def getRuleIndex(self):
            return InventarioDSLParser.RULE_aggregateStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregateStmt" ):
                listener.enterAggregateStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregateStmt" ):
                listener.exitAggregateStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregateStmt" ):
                return visitor.visitAggregateStmt(self)
            else:
                return visitor.visitChildren(self)




    def aggregateStmt(self):

        localctx = InventarioDSLParser.AggregateStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_aggregateStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(InventarioDSLParser.T__4)
            self.state = 52
            self.aggregationOperator()
            self.state = 53
            self.match(InventarioDSLParser.T__3)
            self.state = 54
            self.match(InventarioDSLParser.STRING)
            self.state = 55
            self.match(InventarioDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return InventarioDSLParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = InventarioDSLParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(InventarioDSLParser.T__5)
            self.state = 58
            self.match(InventarioDSLParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return InventarioDSLParser.RULE_comparisonOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparisonOperator" ):
                listener.enterComparisonOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparisonOperator" ):
                listener.exitComparisonOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparisonOperator" ):
                return visitor.visitComparisonOperator(self)
            else:
                return visitor.visitChildren(self)




    def comparisonOperator(self):

        localctx = InventarioDSLParser.ComparisonOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_comparisonOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AggregationOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return InventarioDSLParser.RULE_aggregationOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregationOperator" ):
                listener.enterAggregationOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregationOperator" ):
                listener.exitAggregationOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAggregationOperator" ):
                return visitor.visitAggregationOperator(self)
            else:
                return visitor.visitChildren(self)




    def aggregationOperator(self):

        localctx = InventarioDSLParser.AggregationOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_aggregationOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 28672) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(InventarioDSLParser.STRING, 0)

        def NUMERIC(self):
            return self.getToken(InventarioDSLParser.NUMERIC, 0)

        def getRuleIndex(self):
            return InventarioDSLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = InventarioDSLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





