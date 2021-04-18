
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
  | classical: :math:`O(N \log{N})` (FFT)
  | quantum: :math:`O(\log{N}^2)` i.e. an exponential speedup
    
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
