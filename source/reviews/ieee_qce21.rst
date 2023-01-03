
IEEE QCE21
==========

  Notes about some of the contributions to the IEEE's Quantum Week 2021. - December, 2021

.. contents::
    :local:

-----

.. ---------------------------------------------------------------------------

Quantum Approximate Optimization
--------------------------------

About `Pranav Gokhale <https://pranavgokhale.com/>`_'s talk at QCE21 :cite:`QCE21_Gokhale`:

- initial optimism:

    - *A Quantum Approximate Optimization Algorithm* :cite:`Farhi_2014`:
      QAOA applied to a bound occurence constraint problem,
      [v1] beats the best known classical algorithm, but [v2] classical algo. have been improved ever since
    - *Quantum Supremacy through the QAOA* :cite:`Farhi_2016` 

- but more recently:

    - *QAOA for Max-Cut requires hundreds of qubits for quantum speed-up* :cite:`Guerreschi_2019` ->
      classical :math:`\textrm{akmaxsat}` in seconds while QAOA in days (for sparse graphs)
    - *Classical and Quantum Bounded Depth Approximate Algorithm* :cite:`Hastings_2019` ->
      local classical MAX-3-LIN-2 scales better then QAOA
    - *Bounds on approximating Max kXOR with quantum and classical local algorithms* :cite:`Marwaha_2021` ->
      QAOA beats classical algorithms, but very far away from "Parisi limit" theoretical benchmark

- noise issue:

    - *Noise-Induced Barren Plateaus in VQAs* :cite:`Wang_2021`, 
      -> increasing the circuit depth makes **gradients vanish** for points more far away from solution
    - *Quantifying the impact of precision errors on QAOA* :cite:`Quiroz_2021` 

- optimism on **dense (hyper)graphs**:

    - :math:`\textrm{akmaxsat}`'s runtime increases exponentially with graph density
    - *Optimized fermionic SWAP networks [...] for QAOA* :cite:`Hashim_2021` 

- more optimism:

    - *The QAOA and the Sherrington-Kirkpatrick Model at Infinite Size* :cite:`Farhi_2021` ->
      from depth p = 11 on, advantage (?)
    - *Obstacles to State Preparation and Variational Optimization from Symmetry Protection*, IBM/TUM (Alexander Kliesch, Robert Koenig) :cite:`Bravyi_2020` ->
      run **QAOA recursively** on subgraphs

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

Realizations
------------

Neutral Atoms
^^^^^^^^^^^^^

About :cite:`QCE21_Silverio`.

- neutral atoms trapped in an array of optical tweezers (square or triangular lattice, arbitrary patterns)
- atoms encoded in TLS
- laser is tuned to drive a coherent transition between the two energy levels
  
  - incl. detuning (wrt. Rabi frequency)

- Rydberg states, highly excited electronic states - two atoms will interact through large dipole interaction
- Rydberg blockade: states get coupled to the entangled Bell state :math:`\ket{\phi_+}`
  
  - *Many-body physics with individually controlled Rydberg atoms* :cite:`Browaeys_2020`

- measurement through push-out beams and then fluorescence image of the remaining atoms

- analog vs. digital

  - analog: shine all atoms with the same laser, continuously control the Hamiltonian,
    of all the qubits at the same time ; and measured at the end 
    
    - a tunable Ising Hamiltonian

  - digital: usual circuit, local operations on specific qubits

    - qubits encoded in 2 hyperfine ground states
    - atoms don't interact when not in a Rydberg state: no interaction term in the Hamiltonian
    - with one resonant pulse (combined with a change of phase of the laser),
      any arbitrary single-qubit gate can be performed
    - multi-qubits gates: atoms a brought briefly to the Rydberg state to exploit the Rydberg blockade
    - controlled Z gate (CZ), see below

  - no equivalence of the analog approach as a circuit


Photonics
^^^^^^^^^

About :cite:`QCE21_Pfister`.

- **Continuous-variable** quantum information, and the **measurement-based** computing model :cite:`TUMQI2021`.
  
  - *A One-Way Quantum Computer* :cite:`Raussendorf_2001`
  - *Universal Quantum Computation with Continuous-Variable Cluster States* :cite:`Menicucci_2006`
  - starting from a pre-entangled cluster state, all qubits in :math:`\ket{0} + \ket{1}`,
    measurements on individual qubits act as qubit operations

- *Continuous-variable quantum computing in the quantum optical frequency comb* :cite:`Pfister_2019`


.. ---------------------------------------------------------------------------
