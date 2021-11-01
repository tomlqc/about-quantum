
Combinatorial Optimization
==========================

Heuristic quantum algorithms to solve combinatorial optimization problems

.. ---------------------------------------------------------------------------

Adiabatic Quantum Computation
-----------------------------

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

.. ---------------------------------------------------------------------------

Reformulating Problems
----------------------

The optimization problems need to be reformulated in terms of binary optimization problems
in order to be described by qubits.

* *Reformulating a Problem* :cite:`DWave_2021` provides a detailed procedure in
  `D-Wave's Problem-Solving Handbook <https://docs.dwavesys.com/docs/latest/handbook_reformulating.html>`_.

* *Equality constraints* are formulated as **penalty** terms,
  while for *inequality constraints* **slack variables** may be introduced.

Selected resources:

* *Ising formulations of many NP problems* :cite:`Lucas_2014`:

    "Ising formulations for many NP-complete and NP-hard problems, including all of Karp's 21 NP-complete problems."

* *A Tutorial on Formulating and Using QUBO Models*, :cite:`Glover_2019`:

    "how many different types of constraining relationships arising in practice
    can be embodied within the "unconstrained" QUBO formulation"

* `List of QUBO formulations <https://blog.xa0.de/post/List-of-QUBO-formulations/>`_
  :cite:`Ratke_2021`
  
    "a list of 81 optimization problems and a reference to the QUBO formulation of each problem is shown"

.. ===========================================================================

-----

**Further reading:**

- IEEE Tutorial on Combinatorial Optimization on Quantum Computers :cite:`Shaydulin_2020`:
  `slides <https://github.com/rsln-s/IEEE_QW_2020/blob/master/Slides.pdf>`_, 
  `videos <https://www.youtube.com/playlist?list=PLn2GetlnOf-sdGdmCa_P35iC64KlH_pHo>`_,
  about mapping combinatorial optimization problems onto quantum computers,
  QAOA and AQC.
