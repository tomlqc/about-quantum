
Google Quantum AI
=================

  Today I wanted to get an insight into Google's research activities,
  and I reviewed the publicly available research publications since 2017
  as listed on `Quantum AI <https://quantumai.google/research/publications>`_.
  I focussed on three areas: quantum advantage, quantum chemistry,
  quantum computation (linear system solvers, QAOA, QML). - December 12, 2022

.. contents::
    :local:

-----

.. ---------------------------------------------------------------------------

Quantum Advantage
-----------------

- | Mohseni et al., **Commercialize Quantum Technologies in Five Years**, 2017,
    `research.google:45919 <https://research.google/pubs/pub45919>`_.

- | Boixo et al., **Characterizing Quantum Supremacy in Near-Term Devices**, 2018,
    `research.google:46227 <https://research.google/pubs/pub46227>`_.

- | Markov et al., **Quantum Supremacy Is Both Closer and Farther than It Appears**, 2018,
    `research.google:47252 <https://research.google/pubs/pub47252>`_.

- | Arute et al., **Quantum Supremacy using a Programmable Superconducting Processor**, 2019,
    `research.google:48651 <https://research.google/pubs/pub48651>`_.

  - report of quantum supremacy on the task of **sampling the output of a pseudo-random quantum circuit**,
    that takes about 200 seconds on the **53-qubit** Sycamore superconducting processor
    while classical state-of-the-art classical algorithms would take 10.000 years.
  - "Up to 43 qubits, we use a Schrödinger algorithm, which simulates the evolution of the full quantum state;
    the Jülich supercomputer (with 100,000 cores, 250 terabytes) runs the largest cases. Above this size,
    there is not enough random access memory (RAM) to store the quantum state. For larger qubit numbers,
    we use a hybrid Schrödinger–Feynman algorithm running on Google data centres to compute
    the amplitudes of individual bitstrings. [...]
    Although it is more memory-efficient, the Schrödinger–Feynman algorithm becomes **exponentially
    more computationally expensive** with increasing circuit depth."
  - "We have performed random quantum circuit sampling in polynomial time using a physically realizable quantum processor
    (with sufficiently low error rates), yet no efficient method is known to exist for classical computing machinery."
  
- | Mi et al., **Information scrambling in quantum circuits**, 2021,
    `research.google:50297 <https://research.google/pubs/pub50297>`_ :cite:`Mi_2021`.

  - "Interaction in quantum systems can spread initially localized quantum information into the many
    degrees of freedom of the entire system. Understanding this process, known as **quantum scrambling**,
    is the key to resolving various conundrums in physics."
  - "We show that while operator spreading is captured by an efficient classical model,
    operator entanglement requires exponentially scaled computational resources to simulate.
    These results open the path to studying complex and practically relevant physical observables
    with near-term quantum processors."
  - "Analogous to classical chaos, scrambling manifests itself as a **“butterfly effect”**,
    wherein a local perturbation is rapidly amplified over time. [...]
    Quantum scrambling is enabled by two different mechanisms: operator spreading and operator entanglement."
  - "entanglement in the space of quantum operators is the key to computational complexity of quantum observable."
  - :draft:`To read again ;)`

- | Babbush et al., **Focus Beyond Quadratic Speedups for Error-Corrected Quantum Advantage**, 2021,
    `research.google:49747 <https://research.google/pubs/pub49747>`_.

  - "We conclude that **quadratic speedups will not enable quantum advantage** on early generations of such fault-tolerant devices
    unless there is a significant improvement in how we realize quantum error correction. [...]
    find that quartic speedups look significantly more practical."
  - The central issue is that quantum error correction and the device operation time introduce significant constant factor
    slowdowns to the algorithm runtime.
  - The comparison with parallel classical resources is particularly damning for quantum computing,
    and unfortunately many quadratic quantum speedups (especially those leveraging amplitude amplification)
    apply to problems that are highly parallelizeable.

- | McClean et al., **What the foundations of quantum computer science teach us about chemistry**, 2021,
    `research.google:50415 <https://research.google/pubs/pub50415>`_ :cite:`McClean_2021`.

  - "Leveraging results that quantum computers cannot outpace the physical world, we build to the controversial stance that some chemical problems are best viewed as problems for which no algorithm can deliver their solution in general, known in computer science as undecidable problems. This has implications for the predictive power of thermodynamic models and topics like the ergodic hypothesis. However, we argue that this perspective is not defeatist, but rather helps shed light on the success of existing chemical models like transition state theory, molecular orbital theory, and thermodynamics as models that benefit from data.
  - :draft:`To read again ;)`

- | Huang et al., **Quantum advantage in learning from experiments**, 2022,
    `research.google:50941 <https://research.google/pubs/pub50941>`_ :cite:`Huang_2022`.

  - The first demonstration of a **provable exponential advantage in learning about quantum systems**
    that is robust even on today's noisy hardware.
  - Combines quantum computing and quantum sensing to squeeze out more accuracy when measurement quantum systems.
  - Recipe: Entangle the multiple samples of the measurement (by transducing data from a physical system to a stable quantum memory)
    and process by a quantum agent: quantum PCA, quantum learning.
  - experiments with up to 40 superconducting qubits and 1300 quantum gates
  
- See also Tazhigulov (2022) :cite:`Tazhigulov_2022` about reaching quantum advantage for modelling (real) physical problems.

.. ---------------------------------------------------------------------------

Quantum Chemistry
-----------------

Experiments
^^^^^^^^^^^

- | O'Malley et al., **Scalable Quantum Simulation of Molecular Energies**, 2016,
    `research.google:44815 <https://research.google/pubs/pub44815>`_ :cite:`OMalley_2016`.
  
  - first electronic structure calculation performed on a quantum computer *without exponentially costly precompilation*,
    on an array of **3 superconducting qubits** to compute the energy surface of molecular hydrogen
    using two distinct quantum algorithms:
    (1) unitary coupled cluster method using the variational quantum eigensolver
    (2) canonical quantum algorithm for chemistry, which consists of Trotterization and quantum phase estimation
  - results within chemical accuracy of the numerically exact result

- | Hempel et al., **Quantum Chemistry Calculations on a Trapped-Ion Quantum Simulator**, 2018,
    `research.google:46839 <https://research.google/pubs/pub46839>`_ :cite:`Hempel_2018`.
  
  - experimental implementation of the variational quantum eigensolver algorithm
    to calculate the molecular ground-state energies of two simple molecules -
    molecular hydrogen and lithium hydride -
    on a trapped-ion quantum hardware using up to **4 qubits**
  - first multi-ion quantum simulation of quantum chemistry
  - details two different encodings,
    trick to circumvent algorithmic unstability during optimization,
    LiH expensive in terms of runtime
  - further investigations needed: in mitigation of errors or error suppression,
    in reducing number of required measurements, for reducing the circuit depth

- | Arute et al., **Hartree-Fock on a Superconducting Qubit Quantum Computer**, 2020,
    `research.google:49057 <https://research.google/pubs/pub49057>`_ :cite:`Arute_2020`.
  
  - quantum modelling of the binding energy of
    :math:`{\rm H}_6`, :math:`{\rm H}_8`, :math:`{\rm H}_{10}` and :math:`{\rm H}_{12}` chains
    as well as the isomerization of diazene on a superconducting circuit made of up to **12 qubits**,
    with a parameterized ansatz circuits realizing the Givens rotation approach to free fermion evolution,
    variationally optimized to prepare the Hartree-Fock wavefunction,
    using error-mitigation strategies based on :math:`N`-representability 

- | Tazhigulov et al., **Simulating Challenging Correlated Molecules and Materials on the Sycamore Quantum Processor**, 2022,
    `research.google:51198 <https://research.google/pubs/pub51198>`_ :cite:`Tazhigulov_2022`.
  
  - "With strong quantum advantage demonstrated in artificial tasks, **we examine how such advantage translates
    into modeling physical problems**, and in particular, strongly correlated electronic structure."
  - simulate static and dynamical electronic structure on a superconducting quantum processor
    for two representative correlated electron problems, on up to **11 qubits** with up to 780 two-qubit gates:
    the nitrogenase iron-sulfur molecular clusters, and α-ruthenium trichloride, a proximate spin-liquid material
  - run on the best-performing qubits of Google’s 53-qubit Weber processor based on the Sycamore architecture
  - "Qualitatively correct features in the spin structure, excited-state spectrum, and heat capacity can be obtained.
    However, to achieve this, implemented circuits need to be obtained with the help of classical recompilation and
    the data require significant processing. Unfortunately, these steps raise questions with regard to effectively simulating
    more classically difficult systems."
  - The main limitation in the experiments is the two-qubit gate count: simulations with more than 100 gates are not successful.


Algorithms
^^^^^^^^^^

- | Kivlichan et al., **Quantum Simulation of Electronic Structure with Linear Depth and Connectivity**, 2018,
    `research.google:46718 <https://research.google/pubs/pub46718>`_.
  
  - proposes an arrangement of qubits to reduce cost of algorithms for practical *connectivities between qubits*,
    assuming only a minimal, linearly connected architecture
  - applies both to variational and phase-estimation-based simulation of quantum chemistry

- | Berry et al., **Qubitization of Arbitrary Basis Quantum Chemistry Leveraging Sparsity and Low Rank Factorization**, 2019,
    `research.google:47849 <https://research.google/pubs/pub47849>`_.
  
  - proposes a method to reduce the gate complexity by taking advantage of structure in the Coulomb operator
  - applied to simulation of the FeMoco molecule (relevant to Nitrogen fixation)

- | O'Brien et al., **Efficient Quantum Computation of Molecular Forces and Other Energy Gradients**, 2021,
    `research.google:50837 <https://research.google/pubs/pub50837>`_ :cite:`OBrien_2019`.

  - introduces new quantum algorithms for computing molecular energy derivatives
    with significantly lower complexity than prior methods
  - concludes that calculation of forces on a single nuclei may be of similar cost to estimating energies of chemical systems
  
- | McClean et al., **Discontinuous Galerkin Discretization for Quantum Simulation of Chemistry**, 2020,
    `research.google:48291 <https://research.google/pubs/pub48291>`_.

  - proposes a method to reduce the costs (in terms of number of integrals) of Gaussian and molecular orbital discretizations
    in electronic structure calculations
  - enables to optimize the use of quantum algorithms

- | Huggins et al., **Efficient and Noise Resilient Measurements for Quantum Chemistry on Near-Term Quantum Computers**, 2021,
    `research.google:48383 <https://research.google/pubs/pub48383>`_.

  - previous bounds on the measurement time required by variational algorithms have suggested
    that the application of these techniques to larger molecules might be infeasible
  - presents an optimized measurement strategy
  - provides numerical estimations for calculation of ground-state energies of strongly correlated electronic systems

- | Su et al., **Fault-Tolerant Quantum Simulations of Chemistry in First Quantization**, 2021,
    `research.google:50356 <https://research.google/pubs/pub50356>`_.

  - compile, optimize, and analyze the finite resources required to implement two **first quantized quantum algorithms** for chemistry,
    compare to more commonly studied algorithms in second quantization
  - qubitized algorithm will often be more practical than the interaction-picture algorithm

- | Goings et al., **Reliably Assessing the Electronic Structure of Cytochrome P450 on Today’s Classical Computers
    and Tomorrow’s Quantum Computers**, 2022,
    `research.google:51132 <https://research.google/pubs/pub51132>`_.

  - Both classical and quantum resource estimates suggest that simulation of CYP models at scales large enough
    to balance dynamic and multiconfigurational electron correlation has the **potential to be a quantum advantage problem** and
    emphasizes the important interplay between classical computations and quantum algorithms development for chemical simulation.

.. ---------------------------------------------------------------------------

Quantum Computation
-------------------

Linear System Solvers
^^^^^^^^^^^^^^^^^^^^^

- | Costa et al., **Optimal Scaling Quantum Linear Systems Solver via Discrete Adiabatic Theorem**, 2022,
    `research.google:50899 <https://research.google/pubs/pub50899>`_.

  - ...

QAOA
^^^^

- | Rieffel et al., **XY-mixers: analytical and numerical results for QAOA**, 2020,
    `research.google:49033 <https://research.google/pubs/pub49033>`_.

  - ...

- | McClean et al., **Low-Depth Mechanisms for Quantum Optimization**, 2021,
    `research.google:49421 <https://research.google/pubs/pub49421>`_.

  - ...

- | Cerezo et al., **Variational Quantum Algorithms**, 2021,
    `research.google:49853 <https://research.google/pubs/pub49853>`_.

  - ...

QML
^^^

- | Verdon et al., **Learning to learn with quantum neural networks via classical neural networks**, 2019,
    `research.google: <https://research.google/pubs/pub>`_.

  - ...

- | Broughton et al., **TensorFlow Quantum: A Software Framework for Quantum Machine Learning**, 2020,
    `research.google:49371 <https://research.google/pubs/pub49371>`_.

  - ...

- | Huang et al., **Power of data in quantum machine learning**, 2021,
    `research.google:49725 <https://research.google/pubs/pub49725>`_.

  - This paper is about **learning quantum models**.
  - Data can elevate classical [machine learning] models to rival quantum models, even when the quantum circuits generating the data are hard to compute classically.
  - Following these constructions, in numerical experiments, we find that a variety of common quantum models in the literature perform similarly or worse than classical ML on both classical and quantum datasets due to a small geometric difference.
  - With the large geometric difference endowed by the projected quantum model, we are able to construct engineered datasets to demonstrate large prediction advantage over common classical ML models

.. ---------------------------------------------------------------------------
