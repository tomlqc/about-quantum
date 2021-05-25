
Rabi Oscillations
=================

.. include:: ../../qutex.rst

By applying a superposition of a fixed magnetic field and an weak oscillating field,
the spins of particles can be controlled and their flip be triggered.
This can in particular be used to measure very accurately the energy gap
between the ground and the excited states.
This technique is due to
`Rabi <https://www.nobelprize.org/prizes/physics/1944/rabi/facts/>`_,
who invented it in the 1930s.

The Hamiltonian of this system is:

.. math::

    \hat{H}
    = - \hatb{\mu} \cdot \bm{B}
    = - \mu_0 B_0 \hatsub{\sigma}{z}
      - \mu_0 B_1 \cos \omega t \, \hatsub{\sigma}{x}
      - \mu_0 B_1 \sin \omega t \, \hatsub{\sigma}{y}

and in the :math:`\hatsub{\sigma}{z}` eigenbasis:

.. math::

    \hat{H}
    & =
    - \begin{bmatrix}
    \mu_0 B_0 & \mu_0 B_1 e^{-i \omega t} \\
    \mu_0 B_1 e^{+i \omega t} & \mu_0 B_0
    \end{bmatrix} \\
    & =
    - \frac{\hbar}{2} \begin{bmatrix}
    \omega_0 & \omega_1 e^{-i \omega t} \\
    \omega_1 e^{+i \omega t} & \omega_0
    \end{bmatrix}

where we have defined :math:`\hbar \omega_0 /2 = \mu_0 B_0` and :math:`\hbar \omega_1 /2 = \mu_0 B_1`.

Thus the Schrödinger equation reduces to a system of two coupled differential equations.
In the reference frame of the rotating field (:ref:`stories/background/rwa:Rotating Wave Approximation`),
the Hamiltonian is time independent:

.. math::

    \hat{H}
    & =
    - \frac{\hbar}{2} \begin{bmatrix}
    \omega_0 - \omega & \omega_1 \\
    \omega_1 & \omega - \omega_0 
    \end{bmatrix}

It can be shown that, if the spin is initially in the state :math:`\ket{0}`,
the probability to find the spin in :math:`\ket{1}` is:

.. math::

    P_1 (t) =
    \left( \frac{\omega_1}{\Omega} \right)^2
    \sin^2 \left( \frac{\Omega t}{2} \right)

with :math:`\Omega^2 = (\omega - \omega_0)^2 + \omega_1^2`.

In the resonant case :math:`\omega = \omega_0`, the spin will flip with a probability one
at times given by the period :math:`\pi / \omega_1`.

In other words, if the applied oscillating field's frequency :math:`\omega`
matches the energy difference between the spin levels :math:`\hbar \omega_0`
(that is determined by the amplitude :math:`B_0` of the constant magnetic field),
we will observe an oscillation of the spin between the two levels,
but at a frequency given by the oscillating field's amplitude,
that corresponds to the energy :math:`\hbar \omega_1`.
So, by applying :math:`B_1`, we can trigger the spin flips,
and the stronger this amplitude, the faster these flips will occur.

*More about Rabi oscillation collapses and revivals soon...*

-----

**References:**
inspired by section 12.5.2 :cite:`Basdevant2005`.
