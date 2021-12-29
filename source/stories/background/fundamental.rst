
Fundamental Principles
======================

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

Postulates of Quantum Mechanics
-------------------------------

State Space
^^^^^^^^^^^

Any isolated system evolves in an abstract Hilbert space,
basically a complex vector space with an inner product,
known as the *state space* :math:`\mathcal{E}_H` of the system.
The state of the system is completely described by a *state vector* :math:`\ket{\psi}`,
a normalized vector of the state space.


Measurement
^^^^^^^^^^^

- Every physical quantity of the system is described by a linear Hermitian operator
  :math:`\hat{A}` acting in :math:`\mathcal{E}_H`: it is called an *observable*.

- The only possible result of a measurement of an observable :math:`\hat{A}`
  is one of the eigenvalues :math:`a_\alpha` of :math:`\hat{A}`.

- The probability of measuring :math:`a_\alpha` when the system is
  in the generic state :math:`\psi` is given by the square of the inner product of :math:`\ket{\psi}`
  with the normalized eigenstate :math:`\ket{a_\alpha}`: :math:`\| \bk{\psi}{a_\alpha} \|^2`

- Immediately after the measurement of an observable :math:`\hat{A}`,
  the state of the system is the normalized eigenstate :math:`\ket{a_\alpha}`
  corresponding to the eigenvalue :math:`a_\alpha`.

Different variants of measurements must be considered, see
:ref:`stories/background/measurements:Measurements`.


Time Evolution
^^^^^^^^^^^^^^

The time evolution of a  *closed* quantum system is given by the Schrödinger equation

.. math:: i \hbar \odv{\ket{\psi(t)}}{t} = \hat{H} \ket{\psi(t)}

:math:`\hat{H}` is a Hermitian operator known as the *Hamiltonian* of the system.

The system is *closed* as long as the system does not undergo any obervation,
i.e. has no interaction with its environment.

This evolution is described by a
:ref:`unitary transformation <stories/background/unitary:Unitary Operators>`.

.. ---------------------------------------------------------------------------

Superposition
-------------

The state of a quantum system is described by a vector in an abstract space:
a Hilbert space, that may be of finite or infinite dimension.
A way to describe a measurement is to associate it to one particular basis of this space,
e.g. :math:`\{ \ket{\psi_1}, \dots, \ket{\psi_n} \}`,
such that the different outcomes of the measurement correspond to the projection
onto one of the elements of the basis.

The relation between a measurement and the concept of superposition
is that any state vector can be expressed in the measurement's basis,
and that this expression is basically a weighted sum of the basis' vectors:
e.g. :math:`\ket{\psi} = c_1 \ket{\psi_1} + \dots + c_n \ket{\psi_n}`.
This sum is a superposition of the states :math:`\psi_\alpha`.

Thus the state of a quantum system can be expressed in an infinite number of different superpositions,
each of it associated to a basis of the Hilbert space.

-----

**References:**

- The Postulates: section 5.5 :cite:`Basdevant2005`, section 2.2 :cite:`Nielsen2010`
