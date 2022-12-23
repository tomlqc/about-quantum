
Quantum Kernels
===============

  On my fall vacation, I spent some time to understand the scope and goals of
  **Quantum Machine Learning**. For that purpose I walked through IBM's
  `Quantum Machine Learning course <https://learn.qiskit.org/course/machine-learning/introduction>`_
  as well as the
  `2021 Qiskit Global Summer School <https://qiskit.org/learn/summer-school/quantum-computing-and-quantum-learning-2021/>`_.
  A great alternative view is offered by Xanadu's
  `PennyLane QML tutorials <https://pennylane.ai/qml>`_.
  Finally I selected two recent paper by Google Quantum AI about learning about quantum system.
  In this review I have summarized the main concepts around **Supervised Learning** with **Quantum Kernels**,
  since it is fundamental to much of the current quantum machine learning research. - November 6, 2022

.. contents::
    :local:

-----

.. ---------------------------------------------------------------------------

Summary
-------

Following summary is my main take away from IBM qiskit's
`Quantum Machine Learning course <https://learn.qiskit.org/course/machine-learning/introduction>`_.

In quantum machine learning,
`parameterized quantum circuits <https://learn.qiskit.org/course/machine-learning/parameterized-quantum-circuits>`_
tend to be used for two things:

#. To encode data, where the parameters are determined by the data being encoded.
#. As a quantum model, where the parameters are determined by an optimization process.

`Training quantum circuits <https://learn.qiskit.org/course/machine-learning/training-quantum-circuits>`_
is performed using Quantum Natural Gradient that uses the Quantum Fisher Information
to adapt the steepest descent direction.

In Havlicek (2019), the authors propose a family of
`quantum feature maps <https://learn.qiskit.org/course/machine-learning/quantum-feature-maps-kernels>`_
that are conjectured to be hard to simulate classically, and can be implemented as short-depth circuits on near-term quantum devices. Qiskit implements these as the `PauliFeatureMap <https://qiskit.org/documentation/stubs/qiskit.circuit.library.PauliFeatureMap.html>`_.

#. Application 1: Feature map is known, but is classically intractable. This is demonstrated with the hybrid algo combining quantum feature map and classical SVM.
#. Application 2: We want to optimize a parametrized quantum feature map to minimize classification error. This technique is called kernel alignment.
   See also the `Quantum kernel trainer tutorial <https://qiskit.org/documentation/machine-learning/tutorials/08_quantum_kernel_trainer.html>`_.

Insightful PennyLane tutorials:

- `Training and evaluating quantum kernels <https://pennylane.ai/qml/demos/tutorial_kernels_module.html>`_
- `How to approximate a classical kernel with a quantum computer <https://pennylane.ai/qml/demos/tutorial_classical_kernels.html>`_


References
----------

- | Farhi et Neven, **Classification with Quantum Neural Networks on Near Term Processors**, 2018,
    `arXiv:1802.06002 <https://arxiv.org/abs/1802.06002>`_.
  
  - Introduces the **Variational classifier**.
  - “We introduce a quantum neural network, QNN, that can represent labeled data, classical or quantum,
    and be trained by supervised learning. […]
    We introduce parameter dependent unitaries that can be adapted by supervised learning of labeled data. […]
    We then discuss presenting the data as quantum superpositions of computational basis states corresponding to different label values. […]
    Our work is exploratory and relies on the classical simulation of small quantum systems.”

- | Havlicek, **Supervised learning with quantum enhanced feature spaces**, 2019,
    `arXiv:1804.11326 <https://arxiv.org/abs/1804.11326>`_,
    `doi:10.1038/s41586-019-0980-2 <https://www.nature.com/articles/s41586-019-0980-2>`_.

  - methods for data encoding
  - kernel based training is shown to find better or equally good quantum models than variational circuit training,
    using less quantum processing

- | Schuld & Killoran, **Quantum machine learning in feature Hilbert spaces**, 2019,
    arXiv:1803.07128, doi:10.1103/PhysRevLett.122.040504.

- | Lloyd, Schuld et al., **Quantum embeddings for machine learning**, 2020,
    arXiv:2001.03622.

  - a technique called **quantum metric learning** is introduced which enables effective quantum kernel alignment

- | Matsuo et al., **Problem-specific Parameterized Quantum Circuits of the VQE Algorithm
    for Optimization Problems**, 2020,
    arXiv:2006.05643.


Learning about quantum systems
------------------------------

- | Huang et al., **Power of data in quantum machine learning**, 2021,
    arXiv:2011.01938, doi:10.1038/s41467-021-22539-9.

  - QKSVM is used to quantify the computational power of data in quantum machine learning algorithms and
    to understand the conditions under which quantum models will be capable of outperforming classical ones.

  - Summary [all of this is about **learning quantum models**]

    - Data can elevate classical [machine learning] models to rival quantum models, even when the quantum circuits generating the data are hard to compute classically. 
    - Following these constructions, in numerical experiments, we find that a variety of common quantum models in the literature perform similarly or worse than classical ML on both classical and quantum datasets due to a small geometric difference.
    - With the large geometric difference endowed by the projected quantum model, we are able to construct engineered datasets to demonstrate large prediction advantage over common classical ML models

  - The quantum model considered here is also referred to as a quantum neural network (QNN) [variational classifier as in Farhi (2018)]. In this work, we focus on both classical and quantum ML models based on kernel functions k(xi, xj). The quantum kernel used is Tr[rho(x_i) rho(x_j)].

  - Our foundation is a general prediction error bound for training classical/quantum ML models to predict some quantum model [= learning quantum models].

  - The potential advantage for one ML algorithm defined by K1 to predict better than another ML algorithm defined by K2 depends on the largest possible separation between s^K1 and s^K2 for a dataset [s is the model complexity of the trained function. Small complexity means good generalization]. The quantity to measure this separation is the asymmetric geometrical difference between models.

  - Uses Fashion-MNIST preprocessed with PCA to reduce the dimensionality.
  
  - Associated `Supplementary Information <https://www.nature.com/articles/s41467-021-22539-9#Sec9>`_

    - formal equivalence of an arbitrary depth neural network with a quantum kernel method built from the original quadratic quantum kernel.
    - Constructing dataset to separate quantum and classical model [i.e. redefine the targets y_i for each x_i].

  - Associated `TensorFlow Quantum Data tutorial <https://www.tensorflow.org/quantum/tutorials/quantum_data>`_.

- | Huang et al., **Quantum advantage in learning from experiments**, 2022,
    doi:10.1126/science.abn7293.

  - The first demonstration of a provable exponential advantage in **learning about quantum systems** that is robust even on today's noisy hardware.
  - Combines quantum computing and quantum sensing to squeeze out more accuracy when measurement quantum systems.
  - Recipe: Entangle the multiple samples of the measurement (by transducing data from a physical system to a stable quantum memory) and process by a quantum agent: quantum PCA, quantum learning.
  - Associated `Google AI Blog <https://ai.googleblog.com/2022/06/quantum-advantage-in-learning-from.html>`_.
  - See also `Pennylane tutorial <https://pennylane.ai/qml/demos/tutorial_learning_from_experiments.html>`_


Further readings
----------------

- | About **Quantum Natural Gradient**:

  - Stokes, **Quantum Natural Gradient**, 2020,
    `arXiv:1909.02108 <https://arxiv.org/abs/1909.02108>`_. 
  - Gacon, **Simultaneous Perturbation Stochastic Approximation of the Quantum Fisher Information**, 2021, 
    `arXiv:2103.09232 <https://arxiv.org/abs/2103.09232>`_. 

- | Hubregtsen et al., **Training quantum embedding kernels on near-term quantum computers**, 2022,
    `arXiv:2105.02276 <https://arxiv.org/abs/2105.02276>`_,
    `doi:10.1103/PhysRevA.106.042431> <https://doi.org/10.1103/PhysRevA.106.042431>`_.
  
  - **Quantum embedding kernels (QEKs)** constructed by embedding data into the Hilbert space of a quantum computer
    are a particular quantum kernel technique that allows to gather insights into learning problems and
    that are particularly suitable for noisy intermediate-scale quantum devices.
  - We further show under which conditions **noise from device imperfections** influences the predicted kernel and
    provide a **strategy to mitigate these detrimental effects** which is tailored to quantum embedding kernels.

- | Glick et al., **Covariant quantum kernels for data with group structure**, 2022,
    `arXiv:2105.03406 <https://arxiv.org/abs/2105.03406>`_,
    `aps:S37.00007 <https://meetings.aps.org/Meeting/MAR22/Session/S37.7>`_

  - Quantum kernels exist that, subject to computational hardness assumptions, cannot be computed classically.
    It is an important **challenge to find quantum kernels that provide an advantage in the classification of real-world data**. We introduce a class of quantum kernels that can be used for data with a group structure.
  
- |	Liu et al., **A rigorous and robust quantum speed-up in supervised machine learning**, 2021,
    arXiv:2010.02174, doi:10.1038/s41567-021-01287-z.
    
  - Proposes a machine learning problem based on discrete logarithm which is assumed to be hard for any classical machine learning algorithm.
  - QKSVM is proven to provide a speed up over classical methods for certain specific input data classes.
  
.. ---------------------------------------------------------------------------
