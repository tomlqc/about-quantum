
Evolution of a Qubit
====================

.. include:: ../../qutex.rst

This section is to illustrate on a simple example the evolution of a quantum system.

Fundamental relation
--------------------

The Schrödinger equation rules the evolution of any isolated quantum system:

.. math:: 

    i \hbar \frac{\partial \ket{\psi(t)} }{\partial t} = \hat{H} \ket{\psi(t)}

We assume that the Hamiltonian :math:`\hat{H}` does not depend on time,
and for the sake of simplicity,
that all its eigenvalues :math:`\{ E_1, \dots, E_n \}` are nondegenerated.
All eigenvectors :math:`\{ \ket{\psi_1}, \dots, \ket{\psi_n} \}` are orthogonal.

[#principles]_ Any state vector can be expressed in this basis of eigenvectors,
thus we define the coefficients:

.. math::

    & \ket{\psi(0)} = \sum_\alpha c_\alpha \ket{\psi_\alpha} \\
    & \ket{\psi(t)} = \sum_\alpha \lambda_\alpha(t) \ket{\psi_\alpha}

The Schrödinger equation writes:

.. math::

    i \hbar \frac{\partial}{\partial t}
    \begin{bmatrix}
    \lambda_1(t) \\ \dots \\ \lambda_n(t)
    \end{bmatrix}
    = \hat{H}
    \begin{bmatrix}
    \lambda_1(t) \\ \dots \\ \lambda_n(t)
    \end{bmatrix}
    = 
    \begin{bmatrix}
    E_1 \lambda_1(t) \\ \dots \\ E_2 \lambda_n(t)
    \end{bmatrix}

i.e. for each of the (orthogonal) eigenvectors:

.. math::

    i \hbar \frac{\partial}{\partial t} \lambda_\alpha(t) = E_\alpha \lambda_\alpha(t)

and we end up with:

.. math::

    \ket{\psi(t)} = \sum_\alpha c_\alpha e^{-i E_\alpha t / \hbar} \ket{\psi_\alpha}

This means:

- If :math:`\ket{\psi(0)}` is one of the eigenvectors,
  than the state will always remain in this eigenstate!
  
- In case of an initial superposition of eigenstates, the coefficients will evolve,
  such that the amplitude of each component will stay the same, but not the phases.

Illustration
------------

Let us first imagine that after some time we measure in the eigenbasis
of the Hamiltonian: we will always get the outcomes with the same probabilities
given by :math:`| c_\alpha |^2`.

But what happens if we measure an other observable, i.e. in an other basis?

[#twolevels]_ Imagine we consider a two-level system with the energy levels :math:`E_0, \, E_1`,
with :math:`\hbar \Omega = E_0 - E_1`,
and the initial state 
:math:`\ket{\psi(t)} = \ket{+} = \frac{1}{\sqrt{2}} \left( \ket{0} + \ket{1} \right)`.

This state's evolution is given as (the absolute phase can be left out):

.. math::

    \ket{\psi(t)} = \frac{1}{\sqrt{2}} \left(
    e^{-i \Omega t / 2} \ket{0} +
    e^{+i \Omega t / 2} \ket{1}
    \right)

By rearranging the terms, we can infer what will happen if we measure in the basis
:math:`{\ket{+}, \ket{-}}` i.e. we measure an observable that has these eigenstates:

.. math::

    \ket{\psi(t)}
    & = \frac{1}{\sqrt{2}} \left(
    e^{-i \Omega t / 2} \frac{\ket{+} + \ket{-}}{2} +
    e^{+i \Omega t / 2} \frac{\ket{+} - \ket{-}}{2}
    \right) \\
    & = \frac{1}{\sqrt{2}} \left(
    \cos (\frac{\Omega}{2} t) \ket{+} + 
    \sin (\frac{\Omega}{2} t) \ket{-}
    \right)

Thus the probabilities to measure either :math:`\ket{+}` or :math:`\ket{-}`
will oscillate in time with the frequency given by the energy gap between the two levels!

-----

**References:**

.. [#principles] Fundament relation derived as in section 5.5 :cite:`Basdevant2005`.

.. [#twolevels] Inspired by the ... oscillations in ... :cite:`Haroche2013`.