# First run     :source script.vim     on TeX file
# then run this code to take care of equation environments

import numpy as np

fname = 'cv2a3L'
f = open(fname+'.tex', 'r')
g = open(fname+'EqFix.ipynb', 'w')
tog = 1
eqcnt = 0
ifblock = 0          # will keep track of whether we are inside an if block
eqlab = np.zeros(1,)   # will keep track of which equations had label, for 2nd pass
for line in f:
    #print(line[0:3])
    #print("ifblock = ",ifblock)
    if (line[0] != '%'):  # ignore lines that start with % (comments in TeX)
        if (line[0:3] != '\\if' and ifblock == 0):   # ignore if blocks
            p = line.find('$$')
            q = line.find('label{eq')
            if (q != -1):
                eqlab = np.append(eqlab, eqcnt)
            if (p == -1):
                # g.write(line)
                newline = line.replace("pmatrix","bmatrix")
                newline = newline.replace("qquad","hskip 0.25in")
                newline = newline.replace("quad ","hskip 0.25in ")
                newline = newline.replace("l{example:","l{fig:")
                g.write(newline)
            else:
                if (tog == 1):
                    g.write(line.replace("$$",""))  # blank line before
                    g.write(line.replace("$$","\\begin{equation*}"))
                    eqcnt = eqcnt + 1            
                else:
                    g.write(line.replace("$$","\\end{equation*}"))
                    g.write(line.replace("$$",""))  # blank line after
                    # check for last line in cell
                    #if (line.find(',') > -1):
                    #   g.write(line.replace("$$",""))  # blank line after
                tog = -tog
        else:
            if (line[0:3] == '\\fi'):
                ifblock = 0
                # print("flipped")
            else:
                ifblock = 1
                

#print(eqlab)
f.close()
g.close()

# second pass, remove * from labeled equations

g = open(fname+'EqFix.ipynb', 'r')
h = open(fname+'EqFixDeluxe.ipynb', 'w')
tog = 1
eqcnt = 0

for line in g:
    p = line.find('begin{equation')
    q = line.find('end{equation')
    if (p != -1 and q != -1):
        h.write(line)
    else:
        if (p != -1):
            eqcnt = eqcnt + 1 
        if (eqcnt in eqlab):
            #print(eqcnt)
            h.write(line.replace("n*}","n}"))
        else:
            h.write(line)

g.close()
h.close()
            
        

