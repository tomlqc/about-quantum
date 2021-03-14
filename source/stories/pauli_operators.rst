
Pauli Operators
===============

.. include:: ../qutex.rst

.. ---------------------------------------------------------------------------

In :ref:`Angular Momentum<stories/angular_momentum:Fundamentals>`
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

.. EOF -----------------------------------------------------------------------
