
Second Quantization
===================

*The references that inspired this chapter are all mentioned in the*
:ref:`stories/background/2ndquant:References`
*section*.

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

Quantization of the electromagnetic field
-----------------------------------------

The Maxwell equations for the electric and magnetic fields
:math:`\vec{E}` and :math:`\vec{B}` describe the evolution of electromagnetic fields.
They can also be expressed in terms of the vector and scalar potentials
:math:`\vec{A}` and :math:`\Phi` from which
:math:`\vec{E}` and :math:`\vec{B}` can be derived :cite:`Loudon2000`
(see also `wikipedia <https://en.wikipedia.org/wiki/Maxwell%27s_equations#Alternative_formulations>`_).

Assuming the Coulomb gauge condition and introducing the current density :math:`J`,
the evolution of the fields is governed by following equations for 
the *transverse* (subscript :math:`_T`) and the *longitudinal* (subscript :math:`_L`) components

.. math::

    - \nabla^2 \vec{A} +
    \frac{1}{c^2} \frac{\partial^2 \vec{A}}{\partial t^2} =
    \mu_0 \vec{J_T}
    \quad \textrm{and} \quad
    \frac{1}{c^2} \frac{\partial}{\partial t} \nabla{\Phi} =
    \mu_0 \vec{J_L}

For free electromagnetic waves, :math:`\vec{J_T} = 0`, resulting in

.. math::

    - \nabla^2 \vec{A} +
    \frac{1}{c^2} \frac{\partial^2 \vec{A}}{\partial t^2} =
    0

By expanding the vector potential as a sum of contributions from modes in a virtual cavity,
we can obtain :cite:`Loudon2000` following equation for the **contribution of an individual mode**
(characterized by their wave vector :math:`\vec{k}` and their spatial coordinate index :math:`\lambda`)
to the **total radiative energy**

.. math::

    \mathcal{E_{k \lambda}} =
    \epsilon_0 V \omega_k^2 \left(
    A_{k \lambda} A_{k \lambda}^* + A_{k \lambda}^* A_{k \lambda}
    \right)

with :math:`\epsilon_0` the permittivity of free space and :math:`V` the volume.

This equation strikingly resembles the
:ref:`algebraic formulation <stories/background/harmonic:Algebraic solution>`
of the harmonic oscillator.
By virtue of the
:ref:`correspondence principle <stories/background/correspondence:Correspondence Principles>`
we make following associations

.. math::

    A_{k \lambda} \rightarrow \left( \hbar / 2 \epsilon_0 V \omega_k \right) ^ {1/2} \hatsubsup{a}{k \lambda}{}
    \quad \textrm{and} \quad
    A_{k \lambda}^* \rightarrow \left( \hbar / 2 \epsilon_0 V \omega_k \right) ^ {1/2} \hatsubsup{a}{k \lambda}{\dagger}

and we define the corresponding Hamiltonian as

.. math::

    \hatsubsup{H}{k \lambda}{} =
    \frac{1}{2} \hbar \omega_k \left(
    \hatsubsup{a}{k \lambda}{}        \hatsubsup{a}{k \lambda}{\dagger} +
    \hatsubsup{a}{k \lambda}{\dagger} \hatsubsup{a}{k \lambda}{}
    \right)

.. ---------------------------------------------------------------------------

Quantized atom-field interaction
--------------------------------

The Hamiltonian of an atom interacting with an electromagnetic field can be expressed
as the sum of the atomic, radiative and coupling Hamiltonians
:math:`\hatsubsup{H}{A}{}, \, \hatsubsup{H}{R}{}, \, \hatsubsup{H}{AR}{}`.

The atomic Hamiltonian takes into account the atom's electronic energy levels.
It can be formulated in terms of its eigenvectors :math:`\ket{i}`
with eigenvalues :math:`\hbar \omega_i`:

.. math:: \hatsubsup{H}{A}{} = \sum\limits_i \hbar \omega_i \ket{i} \bra{i}

In case of a two-level system, e.g. by considering only two energy levels of the atom,
the **atomic Hamiltonian** involves the
:ref:`Pauli operator <stories/background/pauli_operators:Pauli Operators>`
:math:`\pauliZ` and can be rewritten in terms of the raising and lowering operators
:math:`\pauliPM = \frac{1}{2} \left( \pauliX \pm i \pauliY \right)`

.. math::
    
    \hatsubsup{H}{A}{}
    = \frac{\hbar \omega_A}{2} \pauliZ
    = \omega_A \left( \pauliP \pauliM - \frac{1}{2} \right)

This form of the Hamiltonian is known as **second quantization** :cite:`Loudon2000`.

The **field Hamiltonian** involves the creation :math:`\hatsup{a}{\dagger}` and annihilation :math:`\hat{a}`
as described above (or the number operator :math:`\hat{n}`) i.e. for one mode

.. math::

    \hatsubsup{H}{R}{} =
    \frac{1}{2} \hbar \omega_k \left(
    \hatsubsup{a}{k \lambda}{\dagger} \hatsubsup{a}{k \lambda}{} + \frac{1}{2}
    \right)

Finally the **coupling Hamiltonian** describes the atom's **electric dipole** coupling
to the electromagnetic field.
By using the :ref:`stories/background/rwa:Rotating Wave Approximation`, this Hamiltonian reduces to

.. math::
    
    \hatsubsup{H}{AR}{} =
    - i \hbar \frac{\Omega_0}{2} \left( \hat{a} \pauliP - \hatsup{a}{\dagger} \pauliM \right)
    
with the *vacuum Rabi frequency* :math:`\Omega_0` :cite:`Haroche2013`.

The complete Hamiltonian as described in this section is called the **Jaynes-Cummings Hamiltonian**,
named after Jaynes and Cummings who introduced it as an idealization of the matter-field coupling
in free space.

The eigenstates of this interaction Hamiltonian are generally entangled states
denoted by :math:`\ket{+, n}` and :math:`\ket{-, n}` and called the **dressed states**
of the atom-field system.
The dressed states are clearly distinguished from the uncoupled states at atom-field resonance.

.. ---------------------------------------------------------------------------

References
----------

- "The field oscillator", section 3.1, and the "Jaynes-Cummings model", section 3.4 :cite:`Haroche2013`
- "Quantization of the radiation field", chapter 4, sections 4.2, 4.4, 4.9 :cite:`Loudon2000`

.. ---------------------------------------------------------------------------
