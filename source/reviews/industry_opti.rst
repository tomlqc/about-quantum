
Optimization in Industry
========================

  Is quantum computing already in use in industry for solving optimization problems? -
  December, 2022

.. contents::
    :local:

-----

.. `arXiv: <https://arxiv.org/abs/>`_
.. `doi: <https://doi.org/>`_

.. ---------------------------------------------------------------------------

Published 2021/2022
-------------------

- | Weinberg et al.,
    **Supply Chain Logistics with Quantum and Classical Annealing Algorithms**, 2022,
    `arXiv:2205.04435 <https://arxiv.org/abs/2205.04435>`_
    :cite:`Weinberg_2022` - QC Ware, Aisin
  
  -  "Rather than distilling the mathematical problem and constructing a version with very few
     variables, we instead use a hybrid workflow approach: we iteratively construct small QUBO instances
     that are of reasonable size for near-term hardware with NISQ algorithms.
     Solutions to these small instances do not solve the full and very complex vehicle routing problem,
     but they do provide a route for a single truck."
     
  - "However, our instances are just slightly too large for direct application on D-Wave annealers
    due to the difficulty of embedding QUBO connectivity graphs."
    See another quote from this paper in the section about :ref:`stories/complements/adiabatic:Embedding`.
  
  - "It is believed, if not yet proven, that quantum annealing will be better at exploring
    the global search space and, via the power of quantum tunneling, might avoid
    getting stuck in local minima. [...]
    The quantum annealing and QAOA are heuristics without relevant proven guarantees."
  
  - "[...] **the quantum annealing solutions are providing improved performance**, at least for the problem
    types and instances studied to date. [...]
    There may be constraints that logistics experts must account for that
    we have not been able to include in the simulation of section VI B, so the overall reduction
    in truck number may not be as dramatic as it appears."
  
  - Includes a recipe for performing PUBO (polynomial) to QUBO (quadratic) conversions.
   
- | Schuetz et al.,
    **Optimization of Robot Trajectory Planning with Nature-Inspired and Hybrid Quantum Algorithms**, 2022, 
    `arXiv:2206.03651 <https://arxiv.org/abs/2206.03651>`_,
    `doi:10.1103/PhysRevApplied.18.054045 <https://doi.org/10.1103/PhysRevApplied.18.054045>`_
    :cite:`Schuetz_2022` - AWS, BMW, Washington
    
  - "Our end-to-end solution integrates highly versatile random-key algorithms with model stacking and
    ensemble techniques, as well as path relinking for solution refinement.
    The core optimization module consists of a biased random-key genetic algorithm. [...]
    To assess the capabilities of today’s quantum hardware, we complement the classical approach
    with results obtained on quantum annealing hardware."
  
  - "**Biased random-key genetic algorithms (BRKGA)** represent a (nature-inspired, because genetic)
    heuristic framework for solving optimization problems." :cite:`Goncalves_2011`

  - "Let us also compare the size of the combinatorial search space any QUBO-based approach is exposed to,
    as compared to the native search space underlying the random-key formalism. [...]
    **the QUBO search space is many orders of magnitude larger**, thus demonstrating the benefits of an efficient,
    native encoding for sequencing-type problems as relevant here."
  
  - "**The QUBO-SA solver is found to be the least competitive, and the least scalable.**"

- | Fernandez-Campoamor et al.,
    **Community Detection in Electrical Grids Using Quantum Annealing**, 2021,
    `arXiv:2112.08300 <https://arxiv.org/abs/2112.08300>`_ - E.ON, TUM

  - "This paper focuses on the application of quantum annealing
    to the partition of an electrical grid into logical communities,
    by maximizing the quality of the partition measured through
    modularity." [...]
    "These methods are then benchmarked against
    two classical approaches: a well-known greedy algorithm
    for modularity optimization, the Louvain‘s algorithm ;
    and an industry-standard integer programming solver, Gurobi Mixed Integer Programming (MIP) solver."

  - "Several methods were applied for testing and benchmarking three test cases [...].
    The first one was able to be run applying directly quantum annealing. [...]
    **Pure quantum as well hybrid annealing samplers
    produces results with a quality slightly better (+1%) or equal
    (less than 5%) than the classical benchmark**, Gurobi MIP
    Solver. In terms of running time, both classical approaches
    outperformed quantum and hybrid samplers, except when the
    size of the problem increased."
    
- | Yarkoni et al.,
    **Multi-car paint shop optimization with quantum annealing**, 2021,
    `arXiv:2109.07876 <https://arxiv.org/abs/2109.07876>`_ - VW, Erlangen, Leiden

  - Uses **quantum annealing**.
    
  - "The objective of the optimization is to minimize the number of color switches between cars
    in a paint shop queue during manufacturing, a known NP-hard problem. "

  - "We found that for
    small problems of up to 30 cars the two QPUs tested, the
    hybrid algorithm, and simulated annealing were able to significantly improve results
    over production conditions (**random distributions of colors**). At intermediate and large problem
    sizes (100 cars and up), only the D-Wave HSS [Hybrid Solver Service] was able to
    consistently beat the greedy algorithm. Although the improvement over random grew with system size,
    the performance of the HSS and the greedy algorithm converged in the large size limit."
  
  - How much is the quantum's part in the hybrid solutions?

- | Streif et al.,
    **Beating classical heuristics for the binary paint shop problem with the quantum approximate optimization algorithm**, 2021,
    `arXiv:2011.03403 <https://arxiv.org/abs/2011.03403>`_,
    `doi:10.1103/PhysRevA.104.012403 <https://doi.org/10.1103/PhysRevA.104.012403>`_ - VW, Erlangen, Leiden
    
  - Uses **QAOA**.
  
  - "The binary paint shop problem (BPSP) is an APX-hard [#APX]_ optimization problem of the automotive industry."

  - "For the BPSP, it is known that no
    classical algorithm can exist which approximates the problem in polynomial runtime. We introduce
    a BPSP instance which is hard to solve with QAOA, and numerically investigate its performance
    and discuss QAOA’s ability to generate approximate solutions."
  
  - "As mentioned, in real-world industrial settings, coloring
    car bodies requires more than two colors. Finding a
    suitable mapping for the generalized paint shop problem
    is another task for the future."

A critical viewpoint from IBM researchers:

- | Davis et al.,
    **Cutting Through the Hype of Quantum Optimization**, Sep 29, 2021,
    `medium.com:cutting-through-the-hype-of-quantum-optimization
    <https://medium.com/qiskit/cutting-through-the-hype-of-quantum-optimization-6d4b5c95e377>`_
    
  - "“Optimization has been hyped by people outside the field, but **researchers in the field never had reason to believe that optimization was as likely to demonstrate exponential quantum advantage as, for example, certain areas of applications in quantum chemistry**,” said IBM researcher Giacomo Nannicini. That’s because the quantum algorithms we have today only offer modest speed-ups over their classical counterparts."
    
  - "Quantum computers don’t seem to offer exponential speedups for black box optimization problems — problems where we don’t know anything about the dataset from which we’re trying to find an optimal solution. However, **it’s possible that there may be some exponential speedup in cases where you know a bit more about the problem**."
    
  - This article exposes with much clarity a position that is in contrast to other presentations
    of the potential of quantum optimization, as e.g. for  
    `use cases in manufacturing 
    <https://www.ibm.com/thought-leadership/institute-business-value/report/quantum-manufacturing>`_
    :cite:`Malina_2019_report`.

.. ---------------------------------------------------------------------------

Routing Problems
----------------

:draft:`About how to consider time and capacity:`

* Hirotaka et al.,
  **Quantum Annealing of Vehicle Routing Problem with Time, State and Capacity**, 2019
  :cite:`Hirotaka_2019`

* Harwood et al.,
  **Formulating and Solving Routing Problems on Quantum Computers**, 2021
  :cite:`Harwood_2021` :cite:`QCE21_Trenev`

:draft:`Discretize time, add capacity as constraint...`

.. ---------------------------------------------------------------------------

-----

.. [#APX]

  From `wikipedia <https://en.wikipedia.org/wiki/APX>`_:
  "The class APX (an abbreviation of "approximable") is the set of NP optimization problems that allow polynomial-time approximation algorithms with approximation ratio bounded by a constant."
