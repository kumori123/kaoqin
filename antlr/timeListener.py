# Generated from .\antlr\time.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .timeParser import timeParser
else:
    from timeParser import timeParser

# This class defines a complete listener for a parse tree produced by timeParser.
class timeListener(ParseTreeListener):

    # Enter a parse tree produced by timeParser#r.
    def enterR(self, ctx:timeParser.RContext):
        pass

    # Exit a parse tree produced by timeParser#r.
    def exitR(self, ctx:timeParser.RContext):
        pass


    # Enter a parse tree produced by timeParser#value.
    def enterValue(self, ctx:timeParser.ValueContext):
        pass

    # Exit a parse tree produced by timeParser#value.
    def exitValue(self, ctx:timeParser.ValueContext):
        pass



del timeParser