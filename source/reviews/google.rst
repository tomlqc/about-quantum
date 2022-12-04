
Google Quantum AI
=================

  Today I wanted to get an insight into Google's research activities,
  and I reviewed the publicly available research publications since 2017
  as listed on `Quantum AI <https://quantumai.google/research/publications>`_.
  I focussed on three areas: quantum chemistry, quantum optimization together with QML,
  and quantum advantage. - December 12, 2022

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
