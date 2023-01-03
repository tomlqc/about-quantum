
What to expect
==============

Preskill's summary
------------------

`John Preskill <http://theory.caltech.edu/~preskill/>`_
is one of the leading professor's in quantum computing, and 
I would like to quote a few of his statements about the potential of QC.
In my opinion, this makes a very good summary of what to expect.

These quotes are taken from the
`2020 slides <http://theory.caltech.edu/~preskill/ph219/Ph-CS-219A-Slides-2020/Ph-CS-219A-Lecture-1-Introduction.pdf>`_
of Preskill's
`Lecture about Quantum Computation <http://theory.caltech.edu/%7Epreskill/ph219/ph219_2020-21>`_.


- **Why we think quantum computing is powerful**, p.8

    (1) Problems believed to be hard classically, which are easy for quantum computers. Factoring is the best known example.
    
    (2) Complexity theory arguments indicating that quantum computers are hard to simulate classically.
    
    (3) We don’t know how to simulate a quantum computer efficiently using a digital (“classical”) computer. The cost of the best known simulation algorithm rises exponentially with the number of qubits.
    
    But ... the power of quantum computing is limited. For example, **we don’t believe that quantum computers can efficiently solve worst-case instances of NP-hard optimization problems** (e.g., the traveling salesman problem).


- **Hybrid quantum/classical optimizers**, p.28

    Eddie Farhi: “Try it and see if it works!”

    We don’t expect **a quantum computer** to solve worst case instances of NP-hard problems, but it **might find better approximate solutions, or find them faster**.

    Classical optimization algorithms (for both classical and quantum problems) are sophisticated and well-honed after decades of hard work.

    We don’t know whether NISQ devices can do better, but we can try it and see how well it works.


- **The era of quantum heuristics**, p.29

    [...] 
    **Sometimes algorithms are effective in practice even though theorists are not able to validate their performance in advance.**

    [...]
    Possible quantum examples:
    Quantum annealers, approximate optimizers, variational eigensolvers, quantum machine learning ... playing around may give us new ideas.

    What can we do with, say, < 100 qubits, depth < 100? We need a dialog between quantum algorithm experts and application users.

    **Maybe we’ll get lucky ...**
