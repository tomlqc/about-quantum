
Pauli Operators
===============

.. include:: ../../qutex.rst

.. ---------------------------------------------------------------------------

Definitions
-----------

In :ref:`Angular Momentum<stories/background/angular_momentum:Fundamentals>`
we defined **angular-momentum
observables** :math:`\hatb J` by their commutation relations:

.. math:: \hatb{J} \times \hatb{J} = i \hbar \hatb{J}

In order to interpret the outcomes of experiments related to the **spin** of particles,
three operators, denoted by :math:`\hat \sigma_i`, were formulated, that:

- act in a 2-dimensional Hilbert space i.e. describe a two-level quantum system ;
- obey a commutation relations very similar to the above mentioned ;
- have eigenvalues :math:`\pm 1`.

These operators called Pauli operators are defined as

.. math::
    \hat \sigma_X =
    \begin{pmatrix}
    0 & 1 \\
    1 & 0
    \end{pmatrix}
    \, ; \quad
    \hat \sigma_Y =
    \begin{pmatrix}
    0 & -i \\
    i & 0
    \end{pmatrix}
    \, ; \quad
    \hat \sigma_Z =
    \begin{pmatrix}
    1 & 0 \\
    0 & -1
    \end{pmatrix}

and they obey the commutation relation

.. math:: \hatb{\sigma} \times \hatb{\sigma} = 2 i \hatb{\sigma}

Together with the identity operator :math:`\hat I`, they form a basis of the
space of operators acting in a 2-dimensional Hilbert space :math:`\mathcal H`,
i.e. any operator of :math:`\mathcal H` can be expressed as linear combination of
:math:`\hat I` and the :math:`\hat \sigma_i`.

An operator :math:`\hat a`,
that is defined as a linear combination of the :math:`\hat \sigma_i`,
can be written using a vector :math:`\bm n`:

.. math::
    \hat a 
    & = \bm{n} \cdot \hatb{\sigma} \\
    & = n_X \hat \sigma_X + n_Y \hat \sigma_Y  + n_Z \hat \sigma_Z

The action of an operator :math:`\exp(-i \theta \, \bm{n} \cdot \hatb{\sigma})`
on any state vector can be described in the Bloch sphere as a rotation of this vector
around the axis defined by :math:`\bm n`.

.. ---------------------------------------------------------------------------

References
----------

* :cite:`Haroche2013`, section 2.1.1


.. EOF -----------------------------------------------------------------------
