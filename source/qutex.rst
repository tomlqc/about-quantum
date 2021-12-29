
.. math::
    
    % https://latex.wikia.org/wiki/List_of_LaTeX_symbols
    % https://www.overleaf.com/learn/latex/Main_Page
    %
    % latex commands for quantum mechanics: bra & kets
    \newcommand{\bra}[1]{\left<#1\right|}
    \newcommand{\ket}[1]{\left|#1\right>}
    \newcommand{\bk}[2]{\left<#1\middle|#2\right>}
    \newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}
    %
    % general shortcuts
    \newcommand{\bm}[1]{\boldsymbol{#1}}  % bold math
    \newcommand{\super}[2]{#1 {}^{#2}}  % superscript
    \newcommand{\half}{\frac{1}{2}}
    %
    % hats together with subscripts or superscript (e.g. for angular momentum)
    \newcommand{\hatb}[1]{\bm{\hat{#1}}}  % hat + bold
    \newcommand{\hatsub}[2]{\hat{{#1}_{#2}}}  % hat + subscript
    \newcommand{\hatsup}[2]{\super{\hat{#1}}{#2}}  % hat + superscript
    \newcommand{\hatsubsup}[3]{\super{\hat{#1}}{#3}_{#2}}  % hat + sub + superscript
    %
    % Pauli operators
    \newcommand{\pauliX}{\hatsubsup{\sigma}{X}{}}
    \newcommand{\pauliY}{\hatsubsup{\sigma}{Y}{}}
    \newcommand{\pauliZ}{\hatsubsup{\sigma}{Z}{}}
    \newcommand{\pauliP}{\hatsubsup{\sigma}{+}{}}
    \newcommand{\pauliM}{\hatsubsup{\sigma}{-}{}}
    \newcommand{\pauliPM}{\hatsubsup{\sigma}{\pm}{}}
    %
    % derivates
    \newcommand{\odv}[2]{\frac{\textrm{d} #1}{\textrm{d} #2}}
    \newcommand{\pdv}[2]{\frac{\partial #1}{\partial #2}}
    
.. about the Mathjax equation numbering
    https://github.com/readthedocs/sphinx_rtd_theme/pull/383
    https://github.com/dmey/synthia/commit/ee48def68bdb240bad68978f48d6dbb75b893e8b
