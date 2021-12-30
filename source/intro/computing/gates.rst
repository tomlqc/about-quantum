
Gate Model
==========

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

Requirements for the implementation
-----------------------------------

DiVincenzo :cite:`DiVincenzo_2000` proposed five criteria necessary
to successfully implement a quantum computer [#QH-01]_ [#Nielsen-4.6]_:

#. A scalable physical system with well characterized qubits 
#. The ability to initialize the state of the qubits to a simple fiducial state,
   such as :math:`\ket{000 \ldots}`
#. Long relevant decoherence times, much longer than the gate operation time
#. A “universal” set of quantum gates
#. A qubit-specific measurement capability

.. ---------------------------------------------------------------------------

Gates and circuits
------------------

Operations on qubits in a quantum computer are realized using so-called **gates**
acting on either only one qubit or on several of them.
A **quantum circuit** describes a sequence of gates applied to a set of qubits.

**Single-qubit gates** can be represented as :math:`2 \times 2` matrices acting in
the qubit's state space spanned by its basis vectors
:math:`\ket{0}` and :math:`\ket{1}`.

.. list-table:: Examples of single-qubit gates
    
    * - Name
      - Symbol
      - Representation
    * - Hadamard
      - :math:`\boxed{H}`
      - :math:`\frac{1}{\sqrt{2}} \begin{bmatrix} 1 & 1 \\ 1 & -1 \end{bmatrix}`
    * - Pauli-X
      - :math:`\boxed{X}`
      - :math:`\begin{bmatrix} 0 & 1 \\ 1 & 0 \end{bmatrix}`
    * - Pauli-Y
      - :math:`\boxed{Y}`
      - :math:`\begin{bmatrix} 0 & -i \\ i & 0 \end{bmatrix}`
    * - Pauli-Z
      - :math:`\boxed{Z}`
      - :math:`\begin{bmatrix} 1 & 0 \\ 0 & -1 \end{bmatrix}`
    * - Phase
      - :math:`\boxed{S}`
      - :math:`\begin{bmatrix} 1 & 0 \\ 0 & i \end{bmatrix}`
    * - :math:`\pi / 8`
      - :math:`\boxed{T}`
      - :math:`\begin{bmatrix} 1 & 0 \\ 0 & e^{i \pi / 4} \end{bmatrix}`

The most common and useful **multiple-qubit gates** implement controlled operations,
where the state of one *control* qubit conditions the execution of an operation
on one or several *target* qubits.
The two most common are:

- **CNOT**: controlled-NOT gate

  .. math::
        \begin{bmatrix}
        1 & 0 & 0 & 0 \\
        0 & 1 & 0 & 0 \\
        0 & 0 & 0 & 1 \\
        0 & 0 & 1 & 0
        \end{bmatrix}

- **Toffoli** gate: a "controlled-controlled-NOT" gate involving two control qubits and one target qubit.
  "It performs an X on the target only if both controls are in the state :math:`\ket{1}`.
  The final state of the target is then equal to either the AND or the NAND of the two controls,
  depending on whether the initial state of the target was :math:`\ket{0}` or :math:`\ket{1}`." [#qiskit]_
  It is a universal reversible gate, which means that any *classical* reversible circuit
  can be constructed from Toffoli gates, as for example the AND gate as described previously.

.. ---------------------------------------------------------------------------

Universal set of gates
----------------------

[#Nielsen-4.5]_ It can be proven that there exists sets of gates with which any arbitrary unitary operation
can be approximated to arbitrary accuracy by a quantum circuit.

Examples are:

- CNOT and single qubit unitaries in general
- CNOT and Hadamard gate, phase gate, :math:`\pi / 8` in particular

Nevertheless, not all unitary operations can be efficiently implemented.

Worth mentioning are also the *Clifford gates*:
quantum circuits that consist only of Clifford gates can be efficiently simulated with a classical computer,
see :ref:`stories/complements/stabilizer:Clifford operators`.

.. ---------------------------------------------------------------------------

References
----------

.. [#QH-01]
    "Introduction", lecture 01 :cite:`LMUQH2021`

.. [#Nielsen-4.5]
    "Universal quantum gates", section 4.5 :cite:`Nielsen2010`

.. [#Nielsen-4.6]
    "Summary of the quantum circuit model of computation", section 4.6 :cite:`Nielsen2010`

.. [#qiskit]
    `More Circuit Identities <https://qiskit.org/textbook/ch-gates/more-circuit-identities.html#ccx>`_
    in :cite:`QiskitTextbook`

.. ---------------------------------------------------------------------------
