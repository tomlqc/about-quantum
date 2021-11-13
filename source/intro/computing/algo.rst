
Algorithms
==========

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

Complexity classes
------------------

- Refresher:
  **P**, **NP**, **PSPACE**, :cite:`Nielsen2010` section 3.2.4,

- *Quantum computational complexity* :cite:`Nielsen2010` section 4.5.5


.. ---------------------------------------------------------------------------

Quantum algorithms
------------------

- Overview

  - *Quantum algorithms: an overview* :cite:`Montanaro_2016`

  - an extensive list in `Quantum Algorithm Zoo <https://quantumalgorithmzoo.org/>`_ :cite:`Jordan_2021`

  - a review about *Variational Quantum Algorithms* :cite:`Cerezo_2021`

  - :draft:`... oracles ...`

- Examples described in this section

  - **"Pure" quantum algorithms:**
    :ref:`intro/computing/algo:Shor` |
    :ref:`intro/computing/algo:Grover` |
    :ref:`intro/computing/algo:HHL`

  - **Hybrid quantum-classical variational algorithms:**
    :ref:`intro/computing/algo:QAOA` |
    :ref:`intro/computing/algo:VQE`


Shor
^^^^

The Shor algorithm describes a way to break the RSA public-key cryptosystem in polynomial time.
It uses :ref:`stories/complements/shor:Quantum Fourier Transform` and
:ref:`stories/complements/shor:Phase Estimation`, which both are general building blocks for quantum algorithms.

* Application: :ref:`stories/complements/shor:Breaking RSA`


Grover
^^^^^^

* | Grover, the *quantum search algorithm*, incl. **Amplitude amplification**
  | "Having a phone book (sorted by name), find the name corresponding to a given phone number".
  | classical: :math:`O(N)`
  | quantum: :math:`O(\sqrt{N})`
  
* | Grover algorithm is optimal :cite:`Bennett_1997`:
  | "relative to an oracle chosen uniformly at random, with probability 1,
    the class NP cannot be solved on a quantum Turing machine in time :math:`o(2^{n/2})`"
  | "recent work of Grover shows how to accept the class NP relative to any oracle
    on a quantum computer in time :math:`O(2^{n/2})`."

* An approaching to TSP and SAT using Grover's *quantum search algorithm*:

    - | `How the quantum search algorithm works <https://quantum.country/search>`_
         :cite:`Matuschak_2019`,
         about the traveling salesperson problem (TSP): 
      | "consider a variation on TSP, namely,
        searching for a route shorter than some specified threshold distance, :math:`T`."
    - | `Solving Satisfiability Problems using Grover's Algorithm
         <https://qiskit.org/textbook/ch-applications/satisfiability-grover.html>`_
         :cite:`IQCQH_2020`
      | "While it doesn’t make sense to use Grover’s algorithm on 3-sat problems, the techniques here can be applied to the more general case (k-SAT, discussed in the next section) for which Grover’s algorithm can outperform the best classical algorithm."


HHL
^^^

*Solving Linear Systems of Equations* :cite:`Harrow_2009`

    "We consider the case where one doesn't need to know the solution x itself,
    but rather an approximation of the expectation value of some operator associated with x."

* Application: :ref:`stories/complements/classical:Classical Physics`

* Qiskit tutorial: `Solving Linear Systems of Equations using HHL
  <https://qiskit.org/textbook/ch-applications/hhl_tutorial.html>`_
  :cite:`IQCQH_2020`
  
* See also *Hybrid quantum linear equation algorithm* :cite:`Lee_2019`


QAOA
^^^^

* Application: :ref:`stories/complements/opti:Combinatorial Optimization`

* Qiskit tutorial: `Solving combinatorial optimization problems using QAOA
  <https://qiskit.org/textbook/ch-applications/qaoa.html>`_
  :cite:`IQCQH_2020`


VQE
^^^

* Application: :ref:`stories/complements/chemistry:Quantum Chemistry`.

* Qiskit tutorial: `Simulating Molecules using VQE
  <https://qiskit.org/textbook/ch-applications/vqe-molecules.html>`_
  :cite:`IQCQH_2020`


.. ---------------------------------------------------------------------------

Quantum Supremacy
-----------------

:draft:`Draft`

- Quantum Supremacy (Google) vs. Quantum Advantage (IBM)`.

- For what problems:

  - *todo:* A list of problems solved more efficiently on quantum computers.
  - *todo:* Where can we expect an exponential speedup?

- For estimations about the required hardware, see :ref:`intro/computing/state:State of the Art`.

.. ---------------------------------------------------------------------------

-----

**References:**
Cirac :cite:`TUMQI2021` lecture 15 ; Qiskit tutorials :cite:`IQCQH_2020`.

.. ---------------------------------------------------------------------------
