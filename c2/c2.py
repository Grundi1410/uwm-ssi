import Common
from Param import Param

class NaiwnyKlasyfikatorBayesa():
    def main(self):
        lines = Common.listAttributesAndTheirNumbers(open("australian_TST.txt").read())
        australianTRNList = Common.listAttributesAndTheirNumbers(open("australian_TRN.txt").read())
        lines = Common.delLastColumnAndRow(lines)
        columns = Common.switchColumnsToRows(lines)
        getDecisions = Common.getIndexOfDecision(lines)
        print("abc")
        x = Common.countParam(lines, getDecisions, australianTRNList)



if __name__ == "__main__":
    NaiwnyKlasyfikatorBayesa.main("args")

