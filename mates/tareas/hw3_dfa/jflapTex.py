import xml.etree.ElementTree as ET
import sys

def flapToTex(file):
    print(file+"\n")
    tree = ET.parse(file)
    root = tree.getroot()

    transitionM = [[[""]]]

    sigmaSet = set()
    qSet = set()

    for read in root.iter("read"): sigmaSet.add(int(read.text))
    for read in sigmaSet: transitionM[0].append([read])

    for state in root.iter("state"): qSet.add(int(state.get("id")))
    for state in qSet: transitionM.append([[state]]+[ [] for i in range(len(sigmaSet)) ])

    #from -> i, read -> j, value -> to
    for trans in root.iter("transition"):
        i = int(trans.find("from").text)
        j = int(trans.find("read").text)
        val = int(trans.find("to").text)
        
        transitionM[1+i][1+j].append(val)

    nfaFlag = False
    for row in transitionM:
        for column in row:
            for cell in row:
                if len(cell) > 1:
                    nfaFlag = len(cell) > 1

    #enumerate start
    master_body = ""
    print ("\\item $Q = \\{" + ", ".join("q_"+str(i) for i in qSet) + "\\}$")
    print ("\\item $\\Sigma = \\{" + ", ".join(str(i) for i in sigmaSet) + "\\}$")
    print ("\\item $\\delta \\colon Q \\times \\Sigma \\rightarrow Q =$")


    #build TeX table
    t_body = ""
    t_body += "\\begin{tabular}{c|" + "|".join(["c" for i in sigmaSet]) + "}\n"

    ln = []
    for i in transitionM[0]:
        ln.append(str(i[0]))
    t_body +="\t" + " & ".join(ln) + " \\\\ \\hline\n"


    #ifdebug
    # for i in transitionM: print i


    #if many do { }
    for line in transitionM[1:]:
        
        ln = []
        for element, index in zip(line, range(len(line)) ):

            cellItems = "$\{ " if nfaFlag and index > 0 and len(element) > 0 else "$"

            if(len(element) == 0):
                cellItems+="\emptyset,"
            for item in element:
                cellItems+="q_{},".format(item) 

            cellItems = cellItems[:-1]
            cellItems += " \}$" if nfaFlag and index > 0 and len(element) > 0 else "$"
            ln.append(cellItems)
        
        t_body +="\t" + " & ".join(ln) + " \\\\ \\hline\n"
    t_body = t_body.rstrip("\\\\ \\hline\n") + "\n"

    t_body += "\\end{tabular}"
    print(t_body)
    #done TeX table

    #end
    print ("\\item $q_0 \\in Q$")

    bigF = []
    for state in root.iter("state"):
        if(state.find("final") is not None): bigF.append("q_"+state.get("id"))

    print ("\item $F = \{"+", ".join(bigF)+"\}$")

for arg in sys.argv[1:]:
    print("\n")
    flapToTex(arg)
