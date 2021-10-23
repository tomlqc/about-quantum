
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

* incl. **QFT** and **Phase Estimation**, building blocks for other algorithms.

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

* Application: :ref:`stories/complements/classical:Classical Physics`

* Qiskit tutorial: `Solving Linear Systems of Equations using HHL
  <https://qiskit.org/textbook/ch-applications/hhl_tutorial.html>`_
  :cite:`IQCQH_2020`
  
* | *Solving Linear Systems of Equations* :cite:`Harrow_2009`
  | "We consider the case where one doesn't need to know the solution x itself,
     but rather an approximation of the expectation value of some operator associated with x."

* | *Hybrid quantum linear equation algorithm* :cite:`Lee_2019`
  | ...


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

- Google's *Quantum Supremacy* claim with 53 qubits :cite:`Arute_2019`

- Estimate of the number of qubits to achieve *Quantum Supremacy* :cite:`Dalzell_2020`

    An IQP circuit with 208 qubits, a QAOA circuit with 420 qubits,
    and a boson sampling circuit with 98 photons
    each would require at least one century to be simulated using a classical simulation algorithm

- *todo:* A list of problems solved more efficiently on quantum computers.
- *todo:* Where can we expect an exponential speedup?

.. ---------------------------------------------------------------------------

-----

**References:**
Cirac :cite:`TUMQI2021` lecture 15 ; Qiskit tutorials :cite:`IQCQH_2020`.

.. ---------------------------------------------------------------------------
