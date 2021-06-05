
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

* incl. **QFT** > **Phase Estimation**

* Application: :ref:`stories/complements/shor:Breaking RSA`

QFT, as a building block for other algorithms:

* | classical discrete Fourier transform with N terms:
  | :math:`O(N^2)`, or :math:`O(N \log{N})` (FFT)

* | We can interpret the discrete Fourier transform as a mapping
    from and to a N-dimensional space.
  | We note that a set of n qubits evolve in a space of dimension :math:`N = 2^n`,
    what allows us to write the QFT's complexity in terms of :math:`n`.
  | It can be shown that the QFT can be implemented by a quantum circuit
    using :math:`O(n^2)` elementary gates,
    i.e. :math:`O((\log{N})^2)`
    i.e. an exponential speedup compared to the FFT :math:`O(N \log{N}) = O(2^n n)`
  | But the FT and the QFT achieve two different goals:
    while the FT returns the :math:`N` coefficients as numbers,
    the QFT generates a superposition of states whose amplitudes are the Fourier coefficients.


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

* Application: :ref:`stories/complements/classical:Classical Systems`

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
