
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

Quantum Annealing Algorithm 
---------------------------

Optimization by *Adiabatic Evolution* :cite:`Farhi_2000` solves *Quadratic Unconstrained Binary Optimization* (**QUBO**) problems,
and is implemented on an :ref:`stories/complements/adiabatic:Adiabatic Quantum Computer`.

It is also a heuristic approach to solve optimization problems.

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

- See my notes about :ref:`reviews/ieee_qce21:Quantum Approximate Optimization` at IEEE QCE21.

- See also about early applications in industry:
  :ref:`reviews/industry_opti:Optimization in Industry`.


.. ===========================================================================

-----

**Further reading:**

- IEEE Tutorial on Combinatorial Optimization on Quantum Computers :cite:`Shaydulin_2020`:
  `slides <https://github.com/rsln-s/IEEE_QW_2020/blob/master/Slides.pdf>`_, 
  `videos <https://www.youtube.com/playlist?list=PLn2GetlnOf-sdGdmCa_P35iC64KlH_pHo>`_,
  about mapping combinatorial optimization problems onto quantum computers,
  QAOA and AQC.

-----

Complements:
:ref:`intro/intro:An Introduction` »
:ref:`intro/computing/computing:Quantum Computing` »
:ref:`intro/computing/apps:Applications`
