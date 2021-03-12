
Bloch Sphere
============

.. toctree::
    :hidden:
    
    ../code/bloch_sphere.rst

.. include:: ../qutex.rst

The Bloch sphere is used to represent the state of two-level systems.

It is, in fact, the visualization of vectors of a complex Hilbert space
of dimension 2 (:math:`\mathbb C^2` space),
in contrast to real spaces, that we are familiar with and easy to interpret.

.. jupyter-execute::
    :hide-code:

    %matplotlib inline
    import matplotlib
    import matplotlib.pyplot as plt

    import numpy as np
    
    import qutip
    from qutip import basis
    from qutip.bloch import Bloch

    # to avoid a distorted sphere
    box_aspect = (1, 1, 1)

The two vectors :math:`\ket{0}` and :math:`\ket{1}` of a chosen basis
are represented on the z-axis.

.. jupyter-execute::
    :hide-code:

    bloch = Bloch()

    up = basis(2, 0)
    down = basis(2, 1)
    bloch.add_states([up, down])
    bloch.show()
    bloch.axes.set_box_aspect(box_aspect)

While the x- and y-axis represent the following superpositions of the basis vectors:

- x-axis: :math:`\ket{0} \pm \ket{1}`
- y-axis: :math:`\ket{0} \pm i \ket{1}`


.. ---------------------------------------------------------------------------



.. ---------------------------------------------------------------------------

.. rubric:: Complements

* :ref:`code/bloch_sphere:Bloch Sphere in QuTiP and Qiskit`.

.. ---------------------------------------------------------------------------
