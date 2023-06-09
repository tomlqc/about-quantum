
Combinatorial Optimization
==========================

Mostly heuristic quantum algorithms to solve combinatorial optimization problems.

.. contents:: In this section
    :local:

-----

.. ---------------------------------------------------------------------------

Grover Algorithm
----------------

The
:ref:`Grover Algorithm <intro/computing/algo:Grover>`
offers a way to perform a "brute-force" search for the optimal solution,
but it provides only a quadratic speedup
i.e. NP problems will remain hard to solve,
and it requires an error-corrected hardware.

.. ---------------------------------------------------------------------------

Variational Quantum Algorithm
-----------------------------

Variational quantum algorithms are a new class of algorithms that provides
a heuristic for solving optimization problems in the NISQ era,
but their overall performance and scaling has yet to be evaluated.

The *Quantum Approximate Optimization Algorithm* (**QAOA**) :cite:`Farhi_2014`
is an iterative hybrid algorithm using a quantum circuit to evaluate the expecation value
of the energy of a parametrized state for the hamiltonian representing the optimization problem,
while the parameters are optimized using a classical algorithm to minimize this energy.

It can be shown that the QAOA is an approximation of the
:ref:`stories/complements/opti:Quantum Annealing Algorithm`
obtained by discretizing the adiabatic process i.e. by trotterization of the time evolution
of the system under the changing hamiltonian.

Selected resources:

* *QAOA: Performance, Mechanism, and Implementation on Near-Term Devices* :cite:`Zhou_2020`

* *Variational Quantum Algorithms* :cite:`Cerezo_2021` covers VQE, QAOA.

* "`The living QAOA reference <https://marwahaha.github.io/qaoa-reference/>`_" :cite:`Marwaha_2021_blog`:
  a great collection of references to papers with very useful comments.
  
* The qiskit tutorial
  `Solving combinatorial optimization problems using QAOA <https://learn.qiskit.org/course/ch-applications/solving-combinatorial-optimization-problems-using-qaoa#Constructing%20Hamiltonian>`_ :cite:`QiskitTextbook`
  describes the construction of the hamiltonian and the principle of QAOA [#notation]_.

And about recent algorithmic improvements:

- | Matsuo et al.,
    *Problem-specific Parameterized Quantum Circuits of the VQE Algorithm for Optimization Problems*, 2020, 
    arXiv:2006.05643.

- | Glos et al., *Space-efficient binary optimization for variational quantum computing*, 2022,
    doi:10.1038/s41534-022-00546-y.

- :draft:`add references to bib`

And finally a recenct critical viewpoint:

- | Anschuetz and Kiani, *Quantum variational algorithms are swamped with traps*, 2022,
    `pdf:s41467-022-35364-5 <https://www.nature.com/articles/s41467-022-35364-5.pdf>`_,
    `doi:10.1038/s41467-022-35364-5 <https://doi.org/10.1038/s41467-022-35364-5>`_ -
  
  - :draft:`summarize...`

.. ---------------------------------------------------------------------------

Quantum Annealing Algorithm 
---------------------------

Optimization by *Adiabatic Evolution* :cite:`Farhi_2000` solves *Quadratic Unconstrained Binary Optimization* (**QUBO**) problems,
and is implemented on an :ref:`stories/complements/adiabatic:Adiabatic Quantum Computer`.
It is based on the idea of setting a quantum system in its ground state
(the hamiltonian is chosen for having a known ground state),
and to slowly and smoothly transform this initial hamiltonian into the problem hamiltonian.
If the process is sufficiently slow, the system will remain in its ground state.

It is a heuristic approach to solve optimization problems, as there is no general result
about the required time or number of finite steps to transform the hamiltonian for the
algorithm to work properly.

.. ---------------------------------------------------------------------------

Reformulating Problems
----------------------

The optimization problems need to be reformulated in terms of binary optimization problems
in order to be described by qubits.

* *Reformulating a Problem* :cite:`DWave_2021` provides a detailed procedure in
  `D-Wave's Problem-Solving Handbook <https://docs.dwavesys.com/docs/latest/handbook_reformulating.html>`_.

* *Equality constraints* are formulated as **penalty** terms,
  while for *inequality constraints* **slack variables** may be introduced.

On quantum annealers, the QUBO needs to be mapped on the Ising model implemented by the hardware, see
:ref:`stories/complements/adiabatic:Embedding`.

Selected topics:

* Discrete non-binary variables can be treated as *one-hot* variables
  (see `D-Wave's "Reformulating a Problem" <https://docs.dwavesys.com/docs/latest/handbook_reformulating.html>`_
  :cite:`DWave_2021`)
  what makes it necessary to add a penalty such that
  (with :math:`n` the number of the variable's possible values)

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

.. ---------------------------------------------------------------------------

Summary
-------

- The Grover algorithm provides only a quadratic speedup over classical exhaustive search.
  This doesn't make intractable problems solvable. It also requires error-correction and
  therefore many physical qubits for few logical ones.

- There is currently no conclusive general statement about the complexity
  of either the *Quantum Annealing Algorithm*
  or the *Variational Quantum Algorithm*.
  These may successfully serve as a new heuristic but this still has to be demonstrated.

- The use of quantum algorithms is strongly limited by the hardware:
  both in terms of noise, especially for the gate-based hardware, and
  because of the limited connectivity between qubits, especially for quantum annealers,
  that significantly increases the number of physical qubits required to map many
  optimization problems (see
  :ref:`stories/complements/adiabatic:Embedding`).

- About the current state of the art:
  
  - `Where is the quantum advantage? <https://blog.xa0.de/post/Where-is-the-quantum-advantage%3F/>`_
    :cite:`Ratke_2021`
  
  - See also the :ref:`stories/complements/adiabatic:State of the art` of adiabatic quantum computing,
    especially the need to improve the coherence of current quantum annealers.

  - There are some tentatives of early applications in industry, but there cannot be considered more then
    proof of concepts, see :ref:`reviews/industry_opti:Optimization in Industry` and especially
    Yarkoni's paper :cite:`Yarkoni_2022` that gives a good overview of quantum annealing.
    No general conclusion can be made about the performance of quantum annealing compared to
    classical algorithms and about the problems best suited for it.
  
  - Poggel :cite:`Poggel_2022` presents strategies for solving optimization problems with QC, this include
    hybrid algorithms, encoding and decomposition methods among others.

- See my notes about :ref:`reviews/ieee_qce21:Quantum Approximate Optimization` at IEEE QCE21.

.. ===========================================================================

-----

**Further reading:**

- IEEE Tutorial on Combinatorial Optimization on Quantum Computers :cite:`Shaydulin_2020`:
  `slides <https://github.com/rsln-s/IEEE_QW_2020/blob/master/Slides.pdf>`_, 
  `videos <https://www.youtube.com/playlist?list=PLn2GetlnOf-sdGdmCa_P35iC64KlH_pHo>`_,
  about mapping combinatorial optimization problems onto quantum computers,
  QAOA and AQC.

-----

.. [#notation]

    The notation :math:`[n]` used in the qiskit tutorial represents the set
    :math:`\{1,2,…,x\}`,
    see `Notation: square brackets with a unique scalar? <https://math.stackexchange.com/questions/1768999/notation-square-brackets-with-a-unique-scalar>`_

-----

Complements:
:ref:`intro/intro:An Introduction` »
:ref:`intro/computing/computing:Quantum Computing` »
:ref:`intro/computing/apps:Applications`
