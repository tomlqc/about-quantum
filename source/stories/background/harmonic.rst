
Harmonic Oscillator
===================

*The references that inspired this chapter are all mentioned in the*
:ref:`stories/background/harmonic:References`
*section*.

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

The harmonic oscillator is classically defined as follows :cite:`Basdevant2005`:

    A harmonic oscillator is a system consisting of a particle of mass :math:`m` elastically
    bound to a center :math:`x_0`, with a restoring force :math:`F = - K (x - x_0)` proportional to
    the distance from the center. The coefficient :math:`K` is the spring constant of the
    oscillator, and the potential energy reads :math:`V(x) = V_0 + K (x - x_0)^2 / 2`.

    The total energy (kinetic + potential) of the classical particle is then
    
    .. math:: E = \half m \dot{x}^2 + \half m \omega^2 x^2

According to the :ref:`correspondence principle <stories/background/correspondence:Correspondence Principles>`
the quantum formulation of the harmonic oscillator has the form:

.. math::
    
    \hat{H} = \frac{ \hatsubsup{p}{x}{2} }{2m} + \half m \omega^2 \hatsup{x}{2}

.. ---------------------------------------------------------------------------

Analytic solution
-----------------

The problem is to solve the eigenvalue equation

.. math::

    \left(  - \frac{\hbar^2}{2m} \frac{d^2}{dx^2} + \half m \omega^2 x^2 \right) \psi(x)
    = E \, \psi(x)

By introducing dimensionless quantities, an analytic solution involving Hermite functions
can be derived, with the quantized energies

.. math:: E_n = \left( n + \half \right) \hbar \omega

.. ---------------------------------------------------------------------------

Algebraic solution
------------------

An alternative solution due to Dirac can be obtained by introducing the observables

.. math::

    \hat{X} = \hat{x} \sqrt{ \frac{m \omega}{\hbar} } , \quad
    \hat{P} = \frac{\hat{p}}{ \sqrt{ m \hbar \omega } }

and further the *annihilation*, *creation operators*

.. math::

    \hat{a}             = \frac{1}{\sqrt{2}} \left( \hat{X} + i \hat{P} \right), \quad
    \hatsup{a}{\dagger} = \frac{1}{\sqrt{2}} \left( \hat{X} - i \hat{P} \right) \\

and the *number operator*

.. math::

    \hat{N} = \hatsup{a}{\dagger} \hat{a}

By simple considerations about these operators and their commutation relations,
it can be shown that

    The eigenvalues of :math:`\hat{N}` are the nonnegative integers only.

Recursive relations about the *creation* and *annihilation operators* such as

.. math::

    \hat{a} \ket{n} = \sqrt{n} \ket{n - 1}, \quad
    \hatsup{a}{\dagger} \ket{n} = \sqrt{n + 1} \ket{n + 1} 

allow to reconstruct the eigenfunctions of the Hamiltonian.
These operators transform a state of energy :math:`(n + 1/2) \hbar \omega` into
a state :math:`(n + 1/2 \mp 1) \hbar \omega`, hence their names.

.. ---------------------------------------------------------------------------

References
----------

- | "The One Dimensional Harmonic Oscillator", section 4.2, and
  | "Algebraic Solution", section 7.5 :cite:`Basdevant2005`

.. ---------------------------------------------------------------------------
