\documentclass{article}
    
    \usepackage{amsmath}
    \usepackage{amssymb}
    \usepackage[utf8]{inputenc}
    \usepackage{graphicx}
    
    \renewcommand{\thesubsection}{\thesection.\alph{subsection}}
    
    \title{Tarea2}
    \date{8/14/2017}
    \author{Ian Neumann}
    
    \begin{document}
      
      \newpage
      \begin{center}
        \Large\textbf{Tarea 3}\\
        \large\textit{Ian Fernando Neumann Sánchez - A01377503}
      \end{center}
      \Large\textbf{Ejercicios de DFA}
        \begin{enumerate}
          \item $A_1= \{\omega | \omega $ has an even number of 1s$\}$
            \paragraph{}
              \includegraphics{ejercicio1}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                         & 0 & 1 \\ \hline
                        $q_0$ & $q_1$ & $q_2$ \\ \hline
                        $q_1$ & $q_1$ & $q_1$ \\ \hline
                        $q_2$ & $q_3$ & $q_2$ \\ \hline
                        $q_3$ & $q_3$ & $q_2$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_3\}$
            \end{enumerate}
            
          \item $A_2= \{\omega | \omega $ contains at least one 1 and an even number of 0s follow the last 1$\}$
            \paragraph{}
              \includegraphics{ejercicio2}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                     & 0 & 1 \\ \hline
                    $q_0$ & $q_0$ & $q_1$ \\ \hline
                    $q_1$ & $q_1$ & $q_2$ \\ \hline
                    $q_2$ & $q_2$ & $q_3$ \\ \hline
                    $q_3$ & $q_3$ & $q_3$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_3\}$
            \end{enumerate}
          
          \item $A_3= \{\omega | \omega $ is the empty string or ends in 0 $\epsilon$ or ends in a 0 $\}$
            \paragraph{}
              \includegraphics{ejercicio3}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3, q_4\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                     & 0 & 1 \\ \hline
                    $q_0$ & $q_1$ & $q_0$ \\ \hline
                    $q_1$ & $q_1$ & $q_2$ \\ \hline
                    $q_2$ & $q_3$ & $q_0$ \\ \hline
                    $q_3$ & $q_1$ & $q_4$ \\ \hline
                    $q_4$ & $q_4$ & $q_4$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_4\}$
            \end{enumerate}
  
          \item $A_4= \{\omega | \omega $ contains at least one 1 and ends with 1 $\}$
            \paragraph{}
              \includegraphics{ejercicio4}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3, q_4\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                     & 0 & 1 \\ \hline
                    $q_0$ & $q_1$ & $q_1$ \\ \hline
                    $q_1$ & $q_2$ & $q_2$ \\ \hline
                    $q_2$ & $q_3$ & $q_4$ \\ \hline
                    $q_3$ & $q_3$ & $q_3$ \\ \hline
                    $q_4$ & $q_4$ & $q_4$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_3\}$
                
            \end{enumerate}   
  
          \item $A_5= \{\omega | \omega $ starts and ends with the same symbol $\}$
            \paragraph{}
              \includegraphics{ejercicio5}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3, q_4\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                     & 0 & 1 \\ \hline
                    $q_0$ & $q_1$ & $q_2$ \\ \hline
                    $q_1$ & $q_3$ & $q_3$ \\ \hline
                    $q_2$ & $q_4$ & $q_4$ \\ \hline
                    $q_3$ & $q_1$ & $q_1$ \\ \hline
                    $q_4$ & $q_2$ & $q_2$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_1, q_4\}$
            \end{enumerate}  
  
          \item $A_6= \{\omega | \omega $ contains the substring 001 $\}$
            \paragraph{}
              \includegraphics{ejercicio6}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                     & 0 & 1 \\ \hline
                    $q_0$ & $q_0$ & $q_1$ \\ \hline
                    $q_1$ & $q_0$ & $q_2$ \\ \hline
                    $q_2$ & $q_3$ & $q_2$ \\ \hline
                    $q_3$ & $q_3$ & $q_3$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_0, q_1, q_2\}$                
            \end{enumerate}  
  
          \item Design an automatic door controller using a DFA. An auto-
          matic door has a pad in front to detect the presence of a person about to walk through the doorway. Another pad is located to the rear of the doorway
          so that the controller can hold the door open long enough for the person to
          pass all the way through and also so that the door does not strike someone
          standing behind it as it opens (Fig (1)).
            \paragraph{}
              \includegraphics{ejercicio7}
            \begin{enumerate}
                \item $Q = \{q_0, q_1, q_2, q_3, q_4, q_5\}$
                \item $\Sigma = \{0, 1\}$
                \item $\delta \colon Q \times \Sigma \rightarrow Q =$
                \begin{tabular}{c|c|c}
                     & 0 & 1 \\ \hline
                    $q_0$ & $q_1$ & $q_1$ \\ \hline
                    $q_1$ & $q_2$ & $q_2$ \\ \hline
                    $q_2$ & $q_3$ & $q_3$ \\ \hline
                    $q_3$ & $q_4$ & $q_4$ \\ \hline
                    $q_4$ & $q_5$ & $q_5$ \\ \hline
                    $q_5$ & $q_6$ & $q_6$
                \end{tabular}
                \item $q_0 \in Q$
                \item $F = \{q_0, q_1, q_2, q_3, q_4, q_5\}$
                
            \end{enumerate}  
        \end{enumerate}
          
    
    \bibliography{Tarea2} 
    \bibliographystyle{ieeetr}
    \end{document}
