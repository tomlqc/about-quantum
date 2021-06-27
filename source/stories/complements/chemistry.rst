
Quantum Chemistry
=================

.. ---------------------------------------------------------------------------

.. rubric:: Simulation

- Quantum Chemistry, :cite:`IQCQH_2020`, Lectures 22-27

- *Simulating Chemistry* :cite:`Kassal_2011`
  
  - reaction rates
  - molecular structure

- "energy derivates for quantum chemistry" :cite:`OBrien_2019`

- **Digital Simulation**: *Hardware-efficient VQE for small molecules*: :cite:`Kandala_2017`
  "superconducting Josephson junction (JJ) based qubits [...]
  includes 6 fixed frequency transmon qubits and a central flux-tunable asymmetric transmon qubit "

- **Analog Simulation**: *Analog quantum chemistry simulation* :cite:`ArguelloLuengo_2019`,
  with ultracold atoms in optical lattices and cavity quantum electrodynamics

.. ---------------------------------------------------------------------------

.. rubric:: Variational Quantum Eigensolver

- Lecture 19 :cite:`LMUQH2021`:, *Hardware-efficient VQE for small molecules* :cite:`Kandala_2017`

  - VQE compute energy with quantum computer, optimize parameters classically
  - makes sense if "computation of energy of trial state cannot be done efficiently with a classical computer",
  - need to map the electronic structure of the molecule (fermionic problem, atomic orbitals)
    to the gate-based quantum (single and two-qubits gates)

- | "a variational quantum eigensolver (VQE) simulation of two intermediate-scale chemistry problems:
    the binding energy of hydrogen chains (as large as H12) and the isomerization mechanism of diazene"
    :cite:`Arute_2020`

- | about variational forms:
  | UCCSD (Unitary Coupled Cluster)
    [`qiskit reference 
    <https://qiskit.org/documentation/stubs/qiskit.chemistry.components.variational_forms.UCCSD.html>`_],
    *Quantum algorithms for electronic structure calculations* :cite:`Barkoutsos_2018`

- | about current hardware:
  | "Extant quantum computers, such as those based on super conducting qubits, have limited qubit connectivity. That is, it is not possible to implement 2-qubit gates on arbitrary qubit pairs (without inserting swap gates). Thus, variational forms have been constructed for specific quantum computer architectures where the circuits are specifically tuned to maximally exploit the natively available connectivity and gates of a given quantum device. Such a variational form was used in 2017 to successfully implement VQE for the estimation of the ground state energies of molecules as large as BeH22 on an IBM quantum computer :cite:`Kandala_2017`". :cite:`IQCQH_2020`

- go further: "faster quantum gradient computation" :cite:`Gilyen_2019`


.. ---------------------------------------------------------------------------

-----

**Further readings**

* Qiskit tutorial: `Simulating Molecules using VQE
  <https://qiskit.org/textbook/ch-applications/vqe-molecules.html>`_
  :cite:`IQCQH_2020`

* *Quantum Information and Computation for Chemistry* :cite:`Olson_2017`,
  a National Science Foundation workshop report.

* *Quantum Chemistry* :cite:`IQCQH_2020`, Qiskit Global Summer School 2020,
  `lectures 23-27 <https://qiskit.org/learn/intro-qc-qh/>`_
  incl. `videos <https://youtube.com/playlist?list=PLOFEBzvs-VvrXTMy5Y2IqmSaUjfnhvBHR>`_.
