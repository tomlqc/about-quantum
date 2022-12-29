
IEEE QCE21
==========

  Notes about some of the contributions to the IEEE's Quantum Week 2021. - December, 2021

.. contents::
    :local:

-----

.. ---------------------------------------------------------------------------

Quantum Kernel Machines
-----------------------

:draft:`More to digest:` with a focus on **quantum kernel machines**
:cite:`QCE21_Lloyd` :cite:`QCE21_Perdue` :cite:`QCE21_Scholten`:

- *Quantum embeddings for machine learning*, Lloyd & Schuld (2020) :cite:`Lloyd_2020`
  
  - about the Hilbert space of the quantum system being a natural space for kernel machines

- *Machine learning of high dimensional data on a noisy quantum processor*, FermiLab/Google (2021) :cite:`Peters_2021`

  - use classical data to compute a quantum kernel matrix, then feed this to a classical SVM
  - beyond classical advantage to be found in an "expressive kernel that is classicaly hard to compute",
    rather than in speed up (may be one day with quantum error correction)
  - *barren plateau* problems i.e. regions with vanishing gradients
  - Google Rainbow chip with 23 qubits
  - "fixed shot budget" (i.e. optimization is essential)

- *Kernel Matrix Completion for Offline Quantum-Enhanced Machine Learning*, IBM (2021) :cite:`Naveh_2021`

  - streaming data: a challenge for quantum kernels
  - matrix completion by a graph-theory-based algorithms
    using *Positive Semidefinite Matrix Completion* :cite:`Vandenberghe_2015`
  - once the overlap exceeds the rank of the extended matrix, perfect completion is possible:
    about guessing the rank *a priori*...

.. ---------------------------------------------------------------------------
