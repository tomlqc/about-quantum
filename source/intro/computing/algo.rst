
Algorithms
==========

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

.. rubric:: Complexity classes

- Refresher:
  **P**, **NP**, **PSPACE**, :cite:`Nielsen2010` section 3.2.4,

- *Quantum computational complexity* :cite:`Nielsen2010` section 4.5.5


.. rubric:: Quantum algorithms

- "oracles"

- *Quantum algorithms: an overview* :cite:`Montanaro_2016`

- examples below


.. rubric:: Shor

* incl. **QFT** and **Phase Estimation**, building blocks for other algorithms.

* Application: :ref:`stories/complements/shor:Breaking RSA`


.. rubric:: Grover

* | Grover, incl. **Amplitude amplification**
  | "Having a phone book (sorted by name), find the name corresponding to a given phone number".
  | classical: :math:`O(N)`
  | quantum: :math:`O(\sqrt{N})`
  
* | Grover algorithm is optimal :cite:`Bennett_1997`:
  | "relative to an oracle chosenuniformly at random, with probability 1,
    the class NP cannot be solved on a quantum Turing machine in time :math:`o(2^{n/2})`"
  | "recent work of Grover shows how to accept the class NP relative to any oracle
    on a quantum computer in time :math:`O(2^{n/2})`."


.. rubric:: HHL

* Application: :ref:`stories/complements/classical:Classical Physics`

* Qiskit tutorial: `Solving Linear Systems of Equations using HHL
  <https://qiskit.org/textbook/ch-applications/hhl_tutorial.html>`_
  :cite:`IQCQH_2020`
  
* | *Solving Linear Systems of Equations* :cite:`Harrow_2009`
  | "We consider the case where one doesn't need to know the solution x itself,
     but rather an approximation of the expectation value of some operator associated with x."

* | *Hybrid quantum linear equation algorithm* :cite:`Lee_2019`
  | ...


.. rubric:: QAOA

* Application: :ref:`stories/complements/opti:Combinatorial Optimization`

* Qiskit tutorial: `Solving combinatorial optimization problems using QAOA
  <https://qiskit.org/textbook/ch-applications/qaoa.html>`_
  :cite:`IQCQH_2020`


.. rubric:: VQE

* Application: :ref:`stories/complements/chemistry:Quantum Chemistry`.

* Qiskit tutorial: `Simulating Molecules using VQE
  <https://qiskit.org/textbook/ch-applications/vqe-molecules.html>`_
  :cite:`IQCQH_2020`


-----

**References:**
Cirac :cite:`TUMQI2021` lecture 15 ; Qiskit tutorials :cite:`IQCQH_2020`.

.. ---------------------------------------------------------------------------
