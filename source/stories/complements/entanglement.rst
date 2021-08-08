
Entanglement
============

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

Photon pairs
------------

Optical experiments are among the first to illustrate entanglement of quantum states.
*These two examples are taken from* QH lecture 11 :cite:`LMUQH2021`.

Photon cascade
^^^^^^^^^^^^^^

In the early 1980s, Alain Aspect *et al.* presented a series of experiments
aiming to resolve the EPR paradox and to dismiss hidden variable theories
:cite:`Aspect_1982a` (see :ref:`stories/background/EPR_experiments:EPR Experiments`).
The work was based on the emission cascade of calcium atoms as described in 
:cite:`Aspect_1980` and :cite:`Aspect_1981` (the latter in open access).

Calcium of atoms excited in a :math:`4p^2 \, {}^1 S_0` decay towards the state :math:`4s^2 \, {}^1 S_0`
through the intermediate short-lived :math:`4s \, 4p^1 P_1`,
by emitting a cascade of two photons at frequencies :math:`\nu_1` and :math:`\nu_2`.
The two photons are correlated in polarization, one being in :math:`\sigma^+`
and the other in :math:`\sigma^-`.
The experiments revealed that the photons were in a superposition of state
:math:`\ket{\sigma^+} \ket{\sigma^-} + \ket{\sigma^-} \ket{\sigma^+}`,
and that they were well suited to test the :ref:`stories/complements/bell:Bell Inequalities`.

Parametric Down Conversion
^^^^^^^^^^^^^^^^^^^^^^^^^^

Parametric Down Conversion, type II phase matching, :cite:`Ghosh_1987`,
also :cite:`Kwiat_1995` for introduction and bibliography

Hong-Ou-Mandel Effect
^^^^^^^^^^^^^^^^^^^^^

If two identical photon enter a beam splitter, one on each input port,
they will always exit the beam splitter together on one of the output ports :cite:`Hong_1987`.
One essential requirement is that they are truely non distinguishable:
same frequency, same polarization, passing the beam splitter at the same time
i.e. within an extremely short time interval.

.. ---------------------------------------------------------------------------

Atom-photon interactions
------------------------

In QED [#QED]_ cavities, interactions between single atoms and single photons
can be precisely controlled.
The cavity's size can be adjusted such that its resonance frequency matches the atoms
energy gap getween the ground and the excited levels.
The atoms are sent through the cavity, while the precise interaction time
between atoms and photons in the cavity is controlled by an additional electric field.
This field changes the energy between the atoms energy levels,
and is used to inhibit the atom's interaction with the cavity.
As soon as this electric field is lifted, the atoms can interact with the light trapped in the cavity.
*This paragraph is inspired by chapter 5.4* :cite:`Haroche2013`.

To entangle atoms with photons, and also pairs of atoms, mediated by the photons in the cavity,
interaction times are choosen such as to define :math:`\pi/2`, :math:`\pi` or :math:`2 \pi`
Rabi pulses (see :ref:`stories/background/rabi:Rabi Oscillations`)
on individual atoms i.e. atoms will pass the cavity one by one.

To generate a :math:`\ket{\psi^+}` Bell state between two atoms :math:`1` and :math:`2`:

.. math::

    \ket{e_1, g_2, 0}
    & \xrightarrow{\text{1 passes cavity,} \, \pi / 2 \, \text{pulse}}
      (\ket{e_1, g_2, 0} + \ket{g_1, g_2, 1}) / \sqrt 2 \\
    & \xrightarrow{\text{2 passes cavity,} \, \pi \, \text{pulse}}
      (\ket{e_1, g_2, 0} - \ket{g_1, e_2, 0}) / \sqrt 2 

*Figure:* Entanglement of two atoms, mediated by a cavity,
inspired by :cite:`Haroche2013`, Fig. 5.33

*To go further:*
Photonic cats, "dispersive and resonant cats in cavity QED", sections 7.3 & 7.4 :cite:`Haroche2013`,
or how to generate a superposition of coherent states.

.. ---------------------------------------------------------------------------

Trapped Ions
------------

The :ref:`trapped ions <stories/complements/iontrap:Trapped Ions>`' internal state as well as their vibration modes can be manipulated by lasers.
*This paragraph is inspired by chapter 8* :cite:`Haroche2013`.

We consider the two internal states :math:`\ket{g}` and :math:`\ket{e}` and
the vibrational stretch modes :math:`\ket{n}`.
The corresponding energies are :math:`\hbar \omega_{eg}` (**carrier** frequency) and
:math:`\hbar \omega_z` (a **phonon**).
By setting the laser's frequency to :math:`\omega_l = \omega_{eg} - \omega_z`,
a so-called **red sideband transition** can be induced
between :math:`\ket{g, n}` and :math:`\ket{e, n-1}`,
while a **blue sideband transition** can be induced with :math:`\omega_l = \omega_{eg} + \omega_z`
between :math:`\ket{g, n}` and :math:`\ket{e, n+1}`.
By carefully applying Rabi pulses (see :ref:`stories/background/rabi:Rabi Oscillations`),
the ions can be entangled.

Consider following example for generating a :math:`\ket{\psi^+}` Bell state
between two ions denoted by 1 and 2, and mediated by stretch modes:

.. math::

    \ket{g_1, g_2, 0}
    & \xrightarrow{\text{blue} \, \pi / 2 \, \text{on 1}}
      (\ket{g_1, g_2, 0} + \ket{e_1, g_2, 1}) / \sqrt 2 \\
    & \xrightarrow{\text{carrier} \, \pi \, \text{on 2}}
      (\ket{g_1, e_2, 0} + \ket{e_1, e_2, 1}) / \sqrt 2 \\
    & \xrightarrow{\text{blue} \, \pi \, \text{on 2}}
      (\ket{g_1, e_2, 0} + \ket{e_1, g_2, 0}) / \sqrt 2 \\

While the sequence described above generates Fock states of the ion's motion,
coherent states of motion, in analogy to coherent states of light,
can be generated by applying an electric force oscillating at the ion's vibration frequency.

.. ---------------------------------------------------------------------------

Ultracold atoms in a lattice
----------------------------

Entangling collisions in a Bose-Einstein condensate,
:cite:`Haroche2013`, section 9.6

.. ---------------------------------------------------------------------------

Electron spins
--------------

Quantum dots in semiconductors.

.. ---------------------------------------------------------------------------

Quantized electrical circuits
-----------------------------

Superconducting qubits.

Quantum state tomography in a superconducting quantum computer :cite:`Mooney_2019`.

.. ---------------------------------------------------------------------------

-----

.. [#QED] **Quantum electrodynamics** is the relativistic quantum field theory of electrodynamics,
    and describes the interaction between light and matter.
    It successfully combines quantum mechanics and special relativity.
