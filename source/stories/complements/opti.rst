
Combinatorial Optimization
==========================

Heuristic quantum algorithms to solve combinatorial optimization problems

There is currently no general statement about the complexity
of either the *Quantum Annealing Algorithm*
or the *Variational Quantum Algorithm*.

About the current state of the art:
`Where is the quantum advantage? <https://blog.xa0.de/post/Where-is-the-quantum-advantage%3F/>`_
:cite:`Ratke_2021`

.. ---------------------------------------------------------------------------

Quantum Annealing Algorithm 
---------------------------

Optimization by *Adiabatic Evolution* :cite:`Farhi_2000` solves *Quadratic Unconstrained Binary Optimization* (**QUBO**) problems,
and is implemented on an :ref:`stories/complements/adiabatic:Adiabatic Quantum Computer`.

.. ---------------------------------------------------------------------------

Variational Quantum Algorithm
-----------------------------

*Quantum Approximate Optimization Algorithm* (**QAOA**) :cite:`Farhi_2014`

- :draft:`to detail: the hybrid procedure...`

- :draft:`about the relation between Adiabatic Evolution and QAOA`

.. comment - https://math.stackexchange.com/questions/1768999/notation-square-brackets-with-a-unique-scalar


Selected resources:

* *QAOA: Performance, Mechanism, and Implementation on Near-Term Devices* :cite:`Zhou_2020`

* *Variational Quantum Algorithms* :cite:`Cerezo_2021` covers VQE, QAOA.

* "`The living QAOA reference <https://marwahaha.github.io/qaoa-reference/>`_" :cite:`Marwaha_2021_blog`:
  a great collection of references to papers with very useful comments.

.. ---------------------------------------------------------------------------

Reformulating Problems
----------------------

The optimization problems need to be reformulated in terms of binary optimization problems
in order to be described by qubits.

* *Reformulating a Problem* :cite:`DWave_2021` provides a detailed procedure in
  `D-Wave's Problem-Solving Handbook <https://docs.dwavesys.com/docs/latest/handbook_reformulating.html>`_.

* *Equality constraints* are formulated as **penalty** terms,
  while for *inequality constraints* **slack variables** may be introduced.

Selected topics:

* Discrete non-binary variables can be treated as *one-hot* variables
  (see `D-Wave's "Reformulating a Problem" <https://docs.dwavesys.com/docs/latest/handbook_reformulating.html>`_
  :cite:`DWave_2021`)
  i.e. by adding a penalty such that (with :math:`n` the number of the variable's possible values)

    .. math:: P = \alpha \left( \sum_{i=1}^{n} x_i - 1 \right)

Selected resources:

* *Ising formulations of many NP problems* :cite:`Lucas_2014`:

    "Ising formulations for many NP-complete and NP-hard problems, including all of Karp's 21 NP-complete problems."

* *A Tutorial on Formulating and Using QUBO Models*, :cite:`Glover_2019`:

    "how many different types of constraining relationships arising in practice
    can be embodied within the "unconstrained" QUBO formulation"

* `List of QUBO formulations <https://blog.xa0.de/post/List-of-QUBO-formulations/>`_
  :cite:`Ratke_2021`
  
    "a list of 81 optimization problems and a reference to the QUBO formulation of each problem is shown"

Example: Traveling Salesman
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's start with the Traveling Salesman Problem (TSP).
It is derived  from the Hamiltonian Cycles Problem :cite:`Lucas_2014`:
    
    "Our solution will use :math:`N^2` bits :math:`x_{v,i}`,
    where :math:`v` represents the vertex and :math:`i` represents its order in a prospective cycle.
    The first two things we require are that every vertex can only appear once in a cycle,
    and that there must be a jth node in the cycle for each j.
    Finally, for the nodes in our prospective ordering, if :math:`x_{u,j}` and :math:`x_{v,j+1}` are both 1,
    then there should be an energy penalty if :math:`(uv) \not\in E`."

such that it can be encoded in the Hamiltonian

.. math::

    H_A =
    A \sum_{v=1}^n \left( 1 - \sum_{j=1}^{N} x_{v,j} \right) ^ 2 +
    A \sum_{j=1}^n \left( 1 - \sum_{v=1}^{N} x_{v,j} \right) ^ 2 +
    A \sum_{(uv) \not\in E} \sum_{j=1}^N x_{u,j} x_{v,j+1}

For the TSP, "each edge :math:`uv` in the graph has a weight :math:`W_{uv}` associated to it",
and we simply add a second term to the previous Hamiltonian

.. math::

    H_B =
    B \sum_{(uv) \in E} W_{uv} \sum_{j=1}^N x_{u,j} x_{v,j+1}

Example: Routing Problems
^^^^^^^^^^^^^^^^^^^^^^^^^

:draft:`About how to consider time and capacity:`

* *Quantum Annealing of Vehicle Routing Problem with Time, State and Capacity* :cite:`Hirotaka_2019`

* *Formulating and Solving Routing Problems on Quantum Computers* :cite:`Harwood_2021` :cite:`QCE21_Trenev`

:draft:`Discretize time, add capacity as constraint...`

.. ---------------------------------------------------------------------------

Recent results
--------------

My notes about `Pranav Gokhale <https://pranavgokhale.com/>`_'s talk at QCE21 :cite:`QCE21_Gokhale`:

- initial optimism:

    - *A Quantum Approximate Optimization Algorithm* :cite:`Farhi_2014`:
      QAOA applied to a bound occurence constraint problem,
      [v1] beats the best known classical algorithm, but [v2] classical algo. have been improved ever since
    - *Quantum Supremacy through the QAOA* :cite:`Farhi_2016` 

- but more recently:

    - *QAOA for Max-Cut requires hundreds of qubits for quantum speed-up* :cite:`Guerreschi_2019` ->
      classical :math:`\textrm{akmaxsat}` in seconds while QAOA in days (for sparse graphs)
    - *Classical and Quantum Bounded Depth Approximate Algorithm* :cite:`Hastings_2019` ->
      local classical MAX-3-LIN-2 scales better then QAOA
    - *Bounds on approximating Max kXOR with quantum and classical local algorithms* :cite:`Marwaha_2021` ->
      QAOA beats classical algorithms, but very far away from "Parisi limit" theoretical benchmark

- noise issue:

    - *Noise-Induced Barren Plateaus in VQAs* :cite:`Wang_2021`, 
      -> increasing the circuit depth makes **gradients vanish** for points more far away from solution
    - *Quantifying the impact of precision errors on QAOA* :cite:`Quiroz_2021` 

- optimism on **dense (hyper)graphs**:

    - :math:`\textrm{akmaxsat}`'s runtime increases exponentially with graph density
    - *Optimized fermionic SWAP networks [...] for QAOA* :cite:`Hashim_2021` 

- more optimism:

    - *The QAOA and the Sherrington-Kirkpatrick Model at Infinite Size* :cite:`Farhi_2021` ->
      from depth p = 11 on, advantage (?)
    - *Obstacles to State Preparation and Variational Optimization from Symmetry Protection*, IBM/TUM (Alexander Kliesch, Robert Koenig) :cite:`Bravyi_2020` ->
      run **QAOA recursively** on subgraphs

.. ===========================================================================

-----

**Further reading:**

- IEEE Tutorial on Combinatorial Optimization on Quantum Computers :cite:`Shaydulin_2020`:
  `slides <https://github.com/rsln-s/IEEE_QW_2020/blob/master/Slides.pdf>`_, 
  `videos <https://www.youtube.com/playlist?list=PLn2GetlnOf-sdGdmCa_P35iC64KlH_pHo>`_,
  about mapping combinatorial optimization problems onto quantum computers,
  QAOA and AQC.
