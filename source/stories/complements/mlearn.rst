
Machine Learning
================

- *Quantum machine learning* :cite:`Biamonte_2017`
- *Training deep quantum neural networks* :cite:`Beer_2020`
- *Circuit-centric quantum classifiers* :cite:`Schuld_2020`
- see also *Quantum Computing and Machine Learning* :cite:`Fawaz_2021`

- Learning by coding: `PennyLane QML Demos <https://pennylane.ai/qml/demos_qml.html>`_.


:draft:`Recently read:`

- *Is quantum advantage the right goal for quantum machine learning?* :cite:`Schuld_2022`

  - Using QC to speed-up classical ML (matrix inversion, sampling) challenged by overheads for QEC
  - What may be natural building blocks for quantum machine learning algorithms?
  - Quantum machine learning models are kernel methods (see dedicated paper)
  - Link connecting quantum circuits to neural tangent kernels and random Fourier features
  - Compute gradients of quantum circuits using the technique of parameter-shift rule

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

- *Power of data in quantum machine learning*, Google (2021) :cite:`Huang_2021`
- *The power of quantum neural networks*, IBM (2021) :cite:`Abbas_2021`

:draft:`About machine learning in general`: *Machine learning and the physical sciences* (2021) :cite:`Carleo_2021`.

See also about Sampling for *Restricted Boltzmann Machines* (RBM)
with the `D-Wave QPU <https://docs.dwavesys.com/docs/latest/handbook_problems.html#machine-learning>`_
:cite:`DWave_2021` (:ref:`stories/complements/adiabatic:Adiabatic Quantum Computer`).

-----

**Further reading:**

- "Quantum Machine Learning", `edX course <https://www.edx.org/course/quantum-machine-learning>`_
  by University of Toronto.
