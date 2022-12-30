
Machine Learning
================

:draft:`Reviews:`

- *Quantum machine learning* (2017) :cite:`Biamonte_2017`
- Mangini, Quantum computing models for artificial neural networks, 2021,
  doi:10.1209/0295-5075/134/10002.

.. contents:: In this section
    :local:

-----

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

.. ---------------------------------------------------------------------------

Outlook
-------

- | The most promising use of QML i.e. where the chance of successfull uses is the highest,
    is for :ref:`reviews/kernels:Learning about quantum systems`.

- | The question that I raise: **Where in real (classical) life do data sets occur
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
