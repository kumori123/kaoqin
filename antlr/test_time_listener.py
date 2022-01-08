
import sys
from antlr4 import *
from timeLexer import timeLexer
from timeParser import timeParser
from timeListener import timeListener
from z3 import *


# class Timelistener(ParseTreeListener):
#     def enterEveryRule(self, ctx: ParserRuleContext):
#         if ctx.getRuleIndex():
#             global arr
#             arr.append(int(ctx.getText()))
#         return super().enterEveryRule(ctx)
#     def exitEveryRule(self, ctx: ParserRuleContext):
#         return super().exitEveryRule(ctx)

class timebaselistener(timeListener):
    def enterR(self, ctx: timeParser.RContext):
        return super().enterR(ctx)
    def exitR(self, ctx: timeParser.RContext):
        return super().exitR(ctx)
    def enterValue(self, ctx: timeParser.ValueContext):
        arr.append(int(ctx.getText()))
        return super().enterValue(ctx)
    def exitValue(self, ctx: timeParser.ValueContext):
        return super().exitValue(ctx)

def main(time_str):
    global arr
    arr = []
    input = InputStream(time_str)
    lexer = timeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = timeParser(stream)
    tree = parser.r()
    print(tree.toStringTree(recog=parser))
    listener = timebaselistener()
    walker = ParseTreeWalker()
    walker.walk(listener,tree)
    return arr

min1,sec1 = main("10:23")
min2,sec2 = main("21:43")

diff = (min2-min1)*60+(sec2-sec1)
print(diff)
s = Solver()
s.add(diff<540)
res = s.check()
if res.r==-1:
    print("OK")
else:
    print("GG")
# if __name__ == '__main__':
#     main(sys.argv)