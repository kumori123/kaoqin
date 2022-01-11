# Generated from time.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .timeParser import timeParser
else:
    from timeParser import timeParser

# This class defines a complete generic visitor for a parse tree produced by timeParser.

class timeVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by timeParser#r.
    def visitR(self, ctx:timeParser.RContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by timeParser#value.
    def visitValue(self, ctx:timeParser.ValueContext):
        return self.visitChildren(ctx)



del timeParser