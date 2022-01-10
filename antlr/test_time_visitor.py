
import sys
from antlr4 import *
from timeLexer import timeLexer
from timeParser import timeParser
from timeVisitor import timeVisitor
from z3 import *

class timebasevisitor(timeVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.arr=[]
    def visitR(self, ctx: timeParser.RContext):
        self.visitValue(ctx.children[0])
        print(ctx.children[1])
        self.visitValue(ctx.children[2])
        # return super().visitR(ctx)

    def visitValue(self, ctx: timeParser.ValueContext):
        self.arr.append(int(ctx.getText()))
        # print(ctx.getText())
        # print(self.arr)
        return super().visitValue(ctx)



def analyze_time(time_str):
    input = InputStream(time_str)
    lexer = timeLexer(input)
    stream = CommonTokenStream(lexer)
    parser = timeParser(stream)
    tree = parser.r()
    print(tree.toStringTree(recog=parser))
    visitor = timebasevisitor()
    visitor.visit(tree)
    print(visitor.arr)
    return visitor.arr

min1,sec1 = analyze_time("10:23")
min2,sec2 = analyze_time("21:43")

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