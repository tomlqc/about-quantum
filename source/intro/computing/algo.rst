
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

- examples:

.. rubric:: Shor

* | QFT > Phase Estimation > Shor (RSA) etc.
  | QFT, as a building block for other algorithms:

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

* | Grover, incl. Amplitude amplification
  | "Having a phone book (sorted by name), find the name corresponding to a given phone number".
  | classical: :math:`O(N)`
  | quantum: :math:`O(\sqrt{N})`

.. rubric:: Quantum Supremacy

- Summary of problems solved more efficiently on quantum computers.

-----

**References:**
Cirac :cite:`TUMQI2021` lecture 15.

.. ---------------------------------------------------------------------------
