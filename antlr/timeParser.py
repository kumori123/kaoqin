# Generated from .\antlr\time.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\r\4\2\t\2\4\3\t\3\3\2\3\2\3\2\3\2\3\3\3\3\3\3\2\2\4\2")
        buf.write("\4\2\2\2\n\2\6\3\2\2\2\4\n\3\2\2\2\6\7\5\4\3\2\7\b\7\3")
        buf.write("\2\2\b\t\5\4\3\2\t\3\3\2\2\2\n\13\7\4\2\2\13\5\3\2\2\2")
        buf.write("\2")
        return buf.getvalue()


class timeParser ( Parser ):

    grammarFileName = "time.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "':'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Num", "WS" ]

    RULE_r = 0
    RULE_value = 1

    ruleNames =  [ "r", "value" ]

    EOF = Token.EOF
    T__0=1
    Num=2
    WS=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(timeParser.ValueContext)
            else:
                return self.getTypedRuleContext(timeParser.ValueContext,i)


        def getRuleIndex(self):
            return timeParser.RULE_r

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterR" ):
                listener.enterR(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitR" ):
                listener.exitR(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitR" ):
                return visitor.visitR(self)
            else:
                return visitor.visitChildren(self)




    def r(self):

        localctx = timeParser.RContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_r)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.value()
            self.state = 5
            self.match(timeParser.T__0)
            self.state = 6
            self.value()
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

        def Num(self):
            return self.getToken(timeParser.Num, 0)

        def getRuleIndex(self):
            return timeParser.RULE_value

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

        localctx = timeParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.match(timeParser.Num)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





