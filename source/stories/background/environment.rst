
Environment
===========

*The references that inspired this chapter are all mentioned in the*
:ref:`stories/background/environment:References`
*section*.

.. ---------------------------------------------------------------------------

Quantum channels
----------------

Quantum channels, also known as
quantum maps :cite:`Haroche2013` or quantum operations :cite:`Nielsen2010`,
are a mean to describe the three different kinds of evolution
that may affect an open quantum system:

- Unitary evolution obeying the dynamics prescribed by the closed system's Hamiltonian 
- Measurement
- Erratic interaction with the environment (noise)

:draft:`Keywords:`

- Density operator, the key representation of the state of open systems
- | Quantum maps, Kraus sum representation /
  | Quantum operations, operator-sum representation

:draft:`More to investigate:`

- | *Tensor networks and graphical calculus for open quantum systems* :cite:`Wood_2015`,
  | in relation with the *Pauli Transfer Matrix (PTM) representation of a Quantum Channel*
    (see `PTM on qiskit <https://qiskit.org/documentation/stubs/qiskit.quantum_info.PTM.html>`_),
    and *completely positive trace preserving (CPTP) maps*

.. ---------------------------------------------------------------------------

Master equation
---------------

:draft:`The Lindblad master equation.`

A differential equation that formalizes the evolution of the system
under the action of its environment.
The involved :math:`L_\mu` operators describe the relaxation events which affect the system,
and can be, in many cases, guessed from a careful analysis of the system.

The evolution according to the master equation can be numerically evaluated
by Monte Carlo simulations.

.. ---------------------------------------------------------------------------

References
----------

- | Quantum maps, Kraus sum representation: section 4.2 :cite:`Haroche2013`, alias
  | "Quantum operations" incl. operator-sum representation, section 8.2 :cite:`Nielsen2010`

- "The Lindblad master equation", section 4.3 :cite:`Haroche2013`

.. ---------------------------------------------------------------------------
