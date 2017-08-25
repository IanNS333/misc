import xml.etree.ElementTree as ET

tree = ET.parse(raw_input()+".jff")
root = tree.getroot()

transitionM = [[""]]

sigmaSet = set()
qSet = set()

for read in root.iter("read"): sigmaSet.add(int(read.text))
for read in sigmaSet: transitionM[0].append(read)

for state in root.iter("from"): qSet.add(int(state.text))
for state in qSet: transitionM.append([state]+[-1 for i in range(len(sigmaSet))])

#from -> i, read -> j, value -> to
for trans in root.iter("transition"):
    i = int(trans.find("from").text)
    j = int(trans.find("read").text)
    val = int(trans.find("to").text)

    transitionM[1+i][1+j] = val



#enumerate start
master_body = ""
print "\\item $Q = \\{" + ", ".join("q_"+str(i) for i in qSet) + "\\}$"
print "\\item $\\Sigma = \\{" + ", ".join(str(i) for i in sigmaSet) + "\\}$"
print "\\item $\\delta \\colon Q \\times \\Sigma \\rightarrow Q =$"


#build TeX table
t_body = ""
t_body += "\\begin{tabular}{c|" + "|".join(["c" for i in sigmaSet]) + "}\n"

ln = []
for i in transitionM[0]:
    ln.append(str(i))
t_body +="\t" + " & ".join(ln) + " \\\\ \\hline\n"

for line in transitionM[1:] :
    ln = []
    for i in line:
        ln.append("$q_%d$"%i)
    t_body +="\t" + " & ".join(ln) + " \\\\ \\hline\n"
t_body += "\\end{tabular}"
print t_body
#done TeX table

#end
print "\\item $q_0$ (the start state) = $q_0 \\in Q$"

bigF = []
for state in root.iter("state"):
    if(state.find("final") is not None): bigF.append("q_"+state.get("id"))

print "\item $F = \{"+", ".join(bigF)+"\}$"