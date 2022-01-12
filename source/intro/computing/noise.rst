
Noise & Errors
==============

.. include:: ../../qutex.rst

Noise is the uncontrolled interaction of the quantum system of interest
with the :ref:`stories/background/environment:Environment`.
It is one major source of errors, though it is not the only one.

Errors can be cast four different types (according to
`Lecture Notes 9
<https://github.com/qiskit-community/intro-to-quantum-computing-and-quantum-hardware/blob/master/lectures/introqcqh-lecture-notes-9.pdf>`_
:cite:`IQCQH_2020`:

- **Incoherent errors:**

  - **Energy relaxation:** A qubit in state :math:`\ket{1}` will loose its excitation energy
    and spontaneously decay to its ground state :math:`\ket{0}`
    (characteristic time :math:`T_1`).
  - **Dephasing:** A qubit will also loose its phase information
    i.e. the relative phase between the :math:`\ket{0}` and :math:`\ket{1}` states will be altered
    (characteristic time :math:`T_2`).

- **Leakage errors:**
  Leakage out of the computational space e.g. excitation towards an additional state :math:`\ket{2}`.
  This can be triggered by the shape of the pulse.

- **Coherent errors:**
  The control of the qubits is not perfect i.e. rotations by a given angle
  can only be done within a certain accuracy.
  The cumulation of small deviations will lead to qubit errors.

- **Measurement:**
  The measurement process itself is prone to errors.

:draft:`More to explore:`

- Quantum Error Correction, :cite:`Nielsen2010` section 10.3,

- Fault-tolerant Algorithms, :cite:`Nielsen2010` section 10.6,

- Randomized Benchmarking :cite:`QCE21_Clarke`:

  - apply random series of rotations in sphere,
    go back to :math:`\ket{0}` (or :math:`\ket{1}`) and check recovery .

- Error mitigation :cite:`QCE21_Gambetta`,
  e.g. using Richardson extrapolation :cite:`Temme_2017`

- :draft:`Recent advances:`

  - *Dynamically Generated Logical Qubits* :cite:`Hastings_2021`

.. ---------------------------------------------------------------------------
