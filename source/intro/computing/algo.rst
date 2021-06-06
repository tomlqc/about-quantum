
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


.. rubric:: HHL

* | *Solving Linear Systems of Equations* :cite:`Harrow_2009`
  | "We consider the case where one doesn't need to know the solution x itself,
     but rather an approximation of the expectation value of some operator associated with x."

* | *Hybrid quantum linear equation algorithm* :cite:`Lee_2019`
  | ...

* Application: :ref:`stories/complements/classical:Classical Physics`

* Qiskit tutorial: `Solving Linear Systems of Equations using HHL
  <https://qiskit.org/textbook/ch-applications/hhl_tutorial.html>`_
  :cite:`IQCQH_2020`
  

.. rubric:: VQE

* Application: Quantum Simulation, :ref:`intro/simulation/VQE:Variational Quantum Eigensolver`.

* Qiskit tutorial: `Simulating Molecules using VQE
  <https://qiskit.org/textbook/ch-applications/vqe-molecules.html>`_
  :cite:`IQCQH_2020`


.. rubric:: QAOA

* Application: :ref:`stories/complements/opti:Combinatorial Optimization`

* Qiskit tutorial: `Solving combinatorial optimization problems using QAOA
  <https://qiskit.org/textbook/ch-applications/qaoa.html>`_
  :cite:`IQCQH_2020`


-----

**References:**
Cirac :cite:`TUMQI2021` lecture 15 ; Qiskit tutorials :cite:`IQCQH_2020`.

.. ---------------------------------------------------------------------------
