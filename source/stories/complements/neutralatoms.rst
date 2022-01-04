
Neutral Atoms
-------------

- in still very academic implementation by `Pasqal <https://pasqal.io/>`_

About **Neutral Atoms in an Optical Lattice**.

:draft:`My notes from QCE21` :cite:`QCE21_Silverio`

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
