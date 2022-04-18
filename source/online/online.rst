
Online Resources
================

Online Resources about Quantum Science, especially about Quantum Computing.

.. note:: This list of resources reflects my knowledge as in **March 2021**.

.. ---------------------------------------------------------------------------

Learning
--------

About Quantum Mechanics and Quantum Computing:

- `Quantum Country <https://quantum.country/>`_
  by Andy Matuschak and Michael Nielsen

  An online book with a novel approach, intended to facilitate understanding and memorizing.
  It describes "the basic principles of quantum computing and quantum mechanics,
  plus two important applications: the quantum search algorithm and quantum teleportation."
  
  Michael Nielsen is, together with Isaac Chuang, the author of
  *Quantum Computation and Quantum Information* :cite:`Nielsen2010`,
  one of the `most cited books <https://dl.acm.org/doi/book/10.5555/1972505>`_
  in physics of all time.

- `An Introduction to Quantum Computing
  <https://www.quantum-inspire.com/kbase/introduction-to-quantum-computing>`_
  by `QuTech <https://qutech.nl>`_
  
  An overview with videos from the `QuTech Academy <https://qutechacademy.nl/>`_.
  The QuTech Academy also offers online courses on `edX <https://www.edx.org/school/delftx>`_
  about hardware, architecture and algorithms.
  
  More videos are available in *The School of Quantum* on `QuTube <https://www.qutube.nl>`_:
  many short videos, also
  about `quantum computer hardware <https://www.qutube.nl/quantum-computer-12>`_
  and advanced topics.
  
  QuTech was `founded in 2014 <https://qutech.nl/about-us/our-organisation/>`_
  as a collaboration between Delft University of Technology (TU Delft)
  and the Netherlands Organisation for Applied Scientific Research (TNO).

- `Quantum Computing Documentation <https://quantum-computing.ibm.com/docs/>`_ by IBM
  
  Very broad offer with many lectures and manuals. I recommend:
  
  * `Introduction to Quantum Computing and Quantum Hardware <https://qiskit.org/learn/intro-qc-qh/>`_ -
    A series of quite technical lectures with videos, notes and programming exercises.
  
  * `Qiskit Textbook <https://qiskit.org/textbook/preface.html>`_ -
    Qiskit manual that also covers physical models and quantum algorithms.

- `QuTiP User Guide <http://qutip.org/docs/latest/guide/guide.html>`_ - an academic software package

  Although just a manual to QuTiP, contents many details about physical models
  (e.g. `Bloch-Redfield master eq.
  <http://qutip.org/docs/latest/guide/dynamics/dynamics-bloch-redfield.html>`_)

- `Learning Resources <https://docs.microsoft.com/en-us/azure/quantum/further-reading-qdk>`_
  of Microsoft's Quantum Development Kit
  
  A list of further readings about advanced topics of quantum computing is provided in the
  `Azure Quantum Documentation <https://docs.microsoft.com/en-us/azure/quantum/>`_:
  building controlled gates, preparing quantum states, synthesizing circuits,
  quantum arithmetics, quantum sampling, quantum simulation, quantum optimization.

- The `IEEE Quantum Week 2020 tutorials <https://qce20.quantum.ieee.org/tutorials/>`_
  may be a further source of inspiration.

.. ---------------------------------------------------------------------------

Computing
---------

A selection of software and platforms for quantum computing:

- `IBM Quantum <https://www.ibm.com/quantum-computing/>`_ -
  Open-source SDK (`Qiskit`, *Quantum Composer*, *Quantum Lab*),
  for running on IBM's computers or simulators.

- `Google Quantum AI <https://quantumai.google/>`_ -
  *Cirq* Python library and Quantum Computing Services on simulators or on *Sycamore* & co.

- `Rigetti Forest <https://github.com/rigetti/forest-software>`_ -
  Rigetti's software for its own quantum computers.

- `Microsoft Q# & Azure Quantum <https://www.microsoft.com/en-us/quantum/development-kit>`_ -
  Microsoft's SDK, for running on the Microsoft Quantum Network of hardware and simulators.
  
- `Amazon Braket <https://docs.aws.amazon.com/braket/>`_ -
  Run quantum algorithms on Rigetti or D-Wave hardware or on a AWS simulator.

- `QuTech QuantumInspire <https://www.quantum-inspire.com/>`_ -
  Run quantum algorithms on simulators or hardware backends.
  Graphical interface to program in QASM (Quantum Assembly Language).

Tutorials:

- Qiskit tutorials:
  `Chemistry <https://quantum-computing.ibm.com/lab/docs/iql/chemistry>`_,
  `Optimization <https://quantum-computing.ibm.com/lab/docs/iql/optimization>`_,
  `Finance <https://quantum-computing.ibm.com/lab/docs/iql/finance-labs>`_

Additional software resources:

- `TensorFlow Quantum <https://www.tensorflow.org/quantum/concepts>`_ -
  a quantum machine learning library for rapid prototyping of hybrid quantum-classical ML models.
  The `announcement <https://ai.googleblog.com/2020/03/announcing-tensorflow-quantum-open.html>`_
  gives a good summary of its purpose and how it works.

See also the overview article by R. LaRose in the Quantum Journal :cite:`LaRose_2019`.

.. ---------------------------------------------------------------------------

Python Packages
-----------------

Python packages that I have played with:

- `Qiskit <https://qiskit.org/>`_ -
  "Qiskit is an open source SDK for working with quantum computers
  at the level of pulses, circuits and application modules."
- `QuTiP <http://qutip.org/>`_ -
  "Quantum Toolbox in Python, QuTiP is open-source software for simulating
  the dynamics of open quantum systems."

Python packages that I am planning to play with:

- `Cirq <https://quantumai.google/cirq>`_ - 
  "Cirq is a Python software library for writing, manipulating, and optimizing quantum circuits,
  and then running them on quantum computers and quantum simulators. "

- `pyGSTi <https://www.pygsti.info/>`_ -
  "Gate Set Tomography, pyGSTi is an open-source software for modeling and characterizing
  noisy quantum information processors (QIPs), i.e., systems of one or more qubits."

See also:

- `numpy.org <https://numpy.org>`_ > ECOSYSTEM > Quantum Computing
- `Quantum Open Source Foundation <https://qosf.org/>`_ with a catalog of evaluated packages.

.. ---------------------------------------------------------------------------
