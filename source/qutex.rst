
.. math::
    
    % https://latex.wikia.org/wiki/List_of_LaTeX_symbols
    % https://www.overleaf.com/learn/latex/Main_Page
    %
    % latex commands for quantum mechanics
    \newcommand{\bra}[1]{\left<#1\right|}
    \newcommand{\ket}[1]{\left|#1\right>}
    \newcommand{\bk}[2]{\left<#1\middle|#2\right>}
    \newcommand{\bke}[3]{\left<#1\middle|#2\middle|#3\right>}
    %
    % general shortcuts
    \newcommand{\bm}[1]{\boldsymbol{#1}}  % bold math
    \newcommand{\super}[2]{#1 {}^{#2}}  % superscript
    %
    % hats together with subscripts or superscript (e.g. for angular momentum)
    \newcommand{\hatb}[1]{\bm{\hat{#1}}}  % hat + bold
    \newcommand{\hatsub}[2]{\hat{{#1}_{#2}}}  % hat + subscript
    \newcommand{\hatsup}[2]{\super{\hat{#1}}{#2}}  % hat + superscript

.. about the Mathjax equation numbering
    https://github.com/readthedocs/sphinx_rtd_theme/pull/383
    https://github.com/dmey/synthia/commit/ee48def68bdb240bad68978f48d6dbb75b893e8b
