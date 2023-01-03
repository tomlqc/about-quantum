
Quantum Chemistry
=================

.. ---------------------------------------------------------------------------

- | **Quantum Chemistry**:

  - Motivation for *Simulating Chemistry* :cite:`Kassal_2011`:
    **reaction rates, molecular structure**

  -  A more recent review paper about *Quantum computational chemistry* :cite:`McArdle_2020`.
  
  - *Gate-count estimates for performing quantum chemistry on small quantum computers?* :cite:`Wecker_2014`
  
  - *Elucidating reaction mechanisms on quantum computers* :cite:`Reiher_2017`:
    "how quantum computers can augment classical computer simulations", and
    "quantum computers will be able to tackle important problems in chemistry
    without requiring exorbitant resources" 

- | **Digital Simulation**:

  - :ref:`stories/complements/chemistry:Exact Quantum Eigensolver` (see below)
  
  - **Approximate** :ref:`stories/complements/chemistry:Variational Quantum Eigensolver` (see below)

- | **Analog Simulation**:

  - *Analogue quantum chemistry simulation* :cite:`ArguelloLuengo_2019`,
    with ultracold atoms in optical lattices and cavity quantum electrodynamics

.. ---------------------------------------------------------------------------

Exact Quantum Eigensolver
^^^^^^^^^^^^^^^^^^^^^^^^^

- | Abrams et al., **A quantum algorithm providing exponential speed increase**, 1999 :cite:`Abrams_1999`

  - **Abstract:**
    We describe a new polynomial time quantum algorithm that uses the quantum fast Fourier transform to find eigenvalues and eigenvectors of a local Hamiltonian, and that can be applied in cases (commonly found in ab initio physics and chemistry problems) for which all known classical algorithms require exponential time. Applications of the algorithm to specific problems are considered, and we find that classically intractable and interesting problems from atomic physics may be solved with between 50 and 100 quantum bits.

  - Thus provides an exponential speedup over classical algorithms
    but requires **error-corrected** (logical) qubits.

.. ---------------------------------------------------------------------------

Variational Quantum Eigensolver
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

- From lecture 19 :cite:`LMUQH2021`:

  - VQE compute energy with quantum computer, optimize parameters classically
  - makes sense if "computation of energy of trial state cannot be done efficiently with a classical computer",
  - need to map the electronic structure of the molecule (fermionic problem, atomic orbitals)
    to the gate-based quantum (single and two-qubits gates)

- | about current hardware :cite:`IQCQH_2020`:
  | "Extant quantum computers, such as those based on super conducting qubits, have **limited qubit connectivity**.
    That is, it is not possible to implement 2-qubit gates on arbitrary qubit pairs (without inserting swap gates).
    Thus, **variational forms have been constructed for specific quantum computer architectures**
    where the circuits are specifically tuned to maximally exploit the natively available connectivity and
    gates of a given quantum device.
    Such a variational form was used in 2017 to successfully implement VQE for the estimation
    of the ground state energies of molecules as large as BeH22 on an IBM quantum computer :cite:`Kandala_2017`".

.. rubric:: An examination

... of *Hardware-efficient VQE for small molecules* :cite:`Kandala_2017`.

- "superconducting Josephson junction (JJ) based qubits [...]
  includes 6 fixed frequency transmon qubits and a central flux-tunable asymmetric transmon qubit "

- ...

- :draft:`about accessing the eigenvalues by reading the state...`

- :draft:`Jordan-Wigner Representation...` :cite:`IQCQH_2020` :cite:`AQCL_2021`

- ...

.. rubric:: More papers

- | "a variational quantum eigensolver (VQE) simulation of two intermediate-scale chemistry problems:
    the binding energy of hydrogen chains (as large as H12) and the isomerization mechanism of diazene"
    :cite:`Arute_2020`

.. rubric:: Go further

- | about variational forms:
  | UCCSD (Unitary Coupled Cluster)
    [`qiskit reference 
    <https://qiskit.org/documentation/stubs/qiskit.chemistry.components.variational_forms.UCCSD.html>`_],
    *Quantum algorithms for electronic structure calculations* :cite:`Barkoutsos_2018`

- "energy derivates for quantum chemistry" :cite:`OBrien_2019`

- "faster quantum gradient computation" :cite:`Gilyen_2019`

.. ---------------------------------------------------------------------------

-----

**Further readings**

* Qiskit tutorial: `Simulating Molecules using VQE
  <https://qiskit.org/textbook/ch-applications/vqe-molecules.html>`_
  :cite:`IQCQH_2020`

* *Quantum Chemistry* :cite:`IQCQH_2020`, Qiskit Global Summer School 2020,
  `lectures 23-27 <https://qiskit.org/learn/intro-qc-qh/>`_
  incl. `videos <https://youtube.com/playlist?list=PLOFEBzvs-VvrXTMy5Y2IqmSaUjfnhvBHR>`_.

* *Quantum Information and Computation for Chemistry* :cite:`Olson_2017`,
  a National Science Foundation workshop report.

-----

Complements:
:ref:`intro/intro:An Introduction` »
:ref:`intro/computing/computing:Quantum Computing` »
:ref:`intro/computing/apps:Applications`
