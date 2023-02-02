# convert $$ $$ to \begin and \end equation in python notebook files
# adding blank lines before and after

import numpy as np

fname = '5. The Fundamental Theorem and Beyond'
f = open(fname+'.ipynb', 'r')
g = open(fname+'EqFix.ipynb', 'w')
tog = 1
eqcnt = 0
eqlab = np.zeros(1,)   # will keep track of which equations had label, for 2nd pass
for line in f:
    p = line.find('$$')
    q = line.find('label{eq')
    if (q != -1):
        eqlab = np.append(eqlab, eqcnt)
    if (p == -1):
        # g.write(line)
        newline = line.replace("pmatrix","bmatrix")
        newline = newline.replace("quad","hskip 0.25in")
        newline = newline.replace("qquad","hskip 0.25in")
        g.write(newline)
    else:
        if (tog == 1):
            g.write(line.replace("$$",""))  # blank line before
            g.write(line.replace("$$","\\\\begin{equation*}"))
            eqcnt = eqcnt + 1            
        else:
            g.write(line.replace("$$","\\\end{equation*}"))
            # check for last line in cell
            if (line.find(',') > -1):
               g.write(line.replace("$$",""))  # blank line after
        tog = -tog

print(eqlab)
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
            print(eqcnt)
            h.write(line.replace("n*}","n}"))
        else:
            h.write(line)

g.close()
h.close()
            
        

