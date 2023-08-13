%s/\\index{\(.*\)}//g

%s/\\proclabel{\(.*\)}//g

%s/\\subsechead{\(.*\)}//g

%s/\\par//g

%s/{\\it \(.*\)}/ *\1* /g 

%s/{\\bf \(.*\)}/ **\1** /g
 
%s/{\\tt \(.*\)}/ *\1*  /g

%s/\\Eqref{\(.*\)}/(\\ref{eq:\1})/g

%s/\\eqlabel{\(.*\)}/\\label{eq:\1}/g

%s/--/-/g

%s/``/"/g

%s/`/'/g

%s/\\medskip//g

%s/\\noindent//g

%s/\\begin{enumerate}//g

%s/\\end{enumerate}//g

%s/\\Matlab\\/Matlab/g

%s/\\Prop\\procref{/\\begin{proposition}\\label{prop:/g

%s/\\pf/**Proof:**

%s/\\cpf/**End of Proof.**

%s/\\begin{tcolorbox}//g

%s/\\end{tcolorbox}//g

%s/\\item\\label{/\\begin{exercise}\\label{ex:/g

%s/\\vfil\\eject//g

%s/\\figref{/\\ref{fig:/g

%s/\\figlabel{\(.*\)}//g

%s/\\fig/Figure /g
