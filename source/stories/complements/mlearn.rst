
Machine Learning
================

.. contents:: In this section
    :local:

-----


.. ---------------------------------------------------------------------------

Introduction
------------

- | Biamonte et al., *Quantum machine learning*, 2017 :cite:`Biamonte_2017`
  
  - "If small quantum information processors can produce statistical patterns that are computationally difficult to be produced by a classical computer, then perhaps they can also recognize patterns that are equally difficult to recognize classically."
  
  - "The notion of a quantum speedup depends on whether one takes a formal computer science perspective—which demands mathematical proofs—or a perspective based on what can be done with realistic, finite-size devices—which requires solid statistical evidence of a scaling advantage over some finite range of problem sizes. For the case of quantum machine learning, the best possible performance of classical algorithms isn’t always known. This is similar to the case of Shor’s polynomial-time quantum algorithm for integer factorization: no subexponential-time classical algorithm has been found, but the possibility is not provably ruled out."
  - "The required resources of classical machine learning algorithms are mostly quantified by numerical experimentation. The resource requirements of quantum machine learning algorithms are likely to be similarly difficult to quantify in practice. "
  - Theoretical exponential speedups have been derived,
    based mainly on the speedup for underlying linear algebra problems
    (see :ref:`intro/computing/algo:HHL`), that show some prohibitive caveats for practical use.
  - Many algorithms require quantum random access memory (qRAM).
  - Deep quantum learning can be implemented form of quantum Boltzmann machines,
    and it can be implemented on a quantum annealer.
    "Quantum computers can accelerate Boltzmann training by providing improved ways of sampling"
    by using quantum coherence.
  - Promising is to use QML for quantum data.

- | Mangini et al., *Quantum computing models for artificial neural networks*, 2021 :cite:`Mangini_2021`
  
  - Covers quantum networks incl. quantum perceptron models, kernel methods, generative models (QBM, QGAN, QCBM),
    QCNN, quantum dissipative networks and trainability (barren plateaus, optimization routines)
  - optimization: backpropagation is difficult to implement, so classical optimizers are used,
    while the *parameter-shift* rule may elegantly provide gradients.
  - about the data: needs metrics such as effective dimension, Fisher information may be useful for this tasks.
    The geometric difference between models :cite:`Huang_2021` is of use too, and motivated to project
    the data on just a subspace of the whole Hilbert space.

.. ---------------------------------------------------------------------------

Variational Classification
--------------------------

In quantum machine learning, one **first set of methods** implements
`parameterized quantum circuits <https://learn.qiskit.org/course/machine-learning/parameterized-quantum-circuits>`_
that can be used for two things:

#. To encode data, where the parameters are determined by the data being encoded.
#. As a quantum model, where the parameters are determined by an optimization process.

Thus the circuits are used to generate the separating hyperplane.

See more details in :ref:`reviews/kernels:Quantum Kernels`.

.. ---------------------------------------------------------------------------

Quantum Kernel Machines
-----------------------

The **second class of methods** makes use of quantum circuits to estimate kernels.

The quantum kernels can be integrated in two ways:

#. Application 1: Feature map is known, but is classically intractable. This is demonstrated with the hybrid algo combining quantum feature map and classical SVM.
#. Application 2: We want to optimize a parametrized quantum feature map to minimize classification error. This technique is called kernel alignment.

See more details in :ref:`reviews/kernels:Quantum Kernels`.

.. ---------------------------------------------------------------------------

Quantum Boltzmann Machines
--------------------------

:draft:`To review:` Amin, Quantum Boltzmann Machine, 2016, arXiv:1601.02036.

See also about Sampling for *Restricted Boltzmann Machines* (RBM)
with the `D-Wave QPU <https://docs.dwavesys.com/docs/latest/handbook_problems.html#machine-learning>`_
:cite:`DWave_2021` (:ref:`stories/complements/adiabatic:Adiabatic Quantum Computer`).

See more details in :ref:`reviews/qbm:Quantum Generative Models`.

.. ---------------------------------------------------------------------------

Summary
-------

- | The most promising use of QML i.e. where the chance of successfull uses is the highest,
    is for :ref:`reviews/kernels:Learning about quantum systems`.

- | The question that I raise about Quantum Kernels: **Where in real (classical) life do data sets occur
    that require a classically non-tractable feature map to be accurately classified?**

- *Is quantum advantage the right goal for quantum machine learning?* :cite:`Schuld_2022`

  - Using QC to speed-up classical ML (matrix inversion, sampling) challenged by overheads for QEC
  - What may be natural building blocks for quantum machine learning algorithms?
  - Quantum machine learning models are kernel methods (see dedicated paper)
  - Link connecting quantum circuits to neural tangent kernels and random Fourier features
  - Compute gradients of quantum circuits using the technique of parameter-shift rule

- See :ref:`reviews/ieee_qce21:Quantum Kernel Machines` at IEEE QCE21.

-----

Courses and Tutorials
---------------------

- `QGSS 2021 QML
  <https://qiskit.org/learn/summer-school/quantum-computing-and-quantum-learning-2021/>`_
- `Qiskit QML Course
  <https://qiskit.org/learn/course/machine-learning-course/>`_
- `IBM Quantum Lab QML Qiskit Tutorials
  <https://quantum-computing.ibm.com/lab/docs/iql/machine-learning>`_
- Learning by coding: `PennyLane QML Demos <https://pennylane.ai/qml/demos_qml.html>`_

- "Quantum Machine Learning", `edX course <https://www.edx.org/course/quantum-machine-learning>`_
  by University of Toronto.

.. ---------------------------------------------------------------------------

-----

Complements:
:ref:`intro/intro:An Introduction` »
:ref:`intro/computing/computing:Quantum Computing` »
:ref:`intro/computing/apps:Applications`
