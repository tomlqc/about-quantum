
Bloch Sphere in QuTiP and Qiskit
--------------------------------

.. ---------------------------------------------------------------------------

Plotting the `Bloch sphere with QuTiP
<http://qutip.org/docs/latest/guide/guide-bloch.html>`_

.. jupyter-execute::
    :hide-code:

    %matplotlib inline
    import matplotlib
    import matplotlib.pyplot as plt

    import numpy as np
    
    import qutip
    from qutip import basis
    from qutip.operators import sigmax, sigmay, sigmaz, sigmap, sigmam
    from qutip.qip.operations import rx, ry, rz
    from qutip.bloch import Bloch
    # from qutip.bloch3d import Bloch3d  # requires mayavi

    # to avoid a distorted sphere
    box_aspect = (1, 1, 1)

.. jupyter-execute::

    bloch = Bloch()
    bloch.show()
    bloch.axes.set_box_aspect(box_aspect)

.. jupyter-execute::

    up = basis(2, 0)
    down = basis(2, 1)
    bloch.clear()
    bloch.add_states([up, down])
    bloch.show()

Apply a rotation of :math:`\frac{\pi}{2}` around the :math:`y` axis.

.. jupyter-execute::

    phi = ry(np.pi / 2) * up
    phi

.. jupyter-execute::

    bloch.clear()
    bloch.add_states([up, phi])
    bloch.show()

.. ---------------------------------------------------------------------------

Plotting the Bloch sphere with `Qiskit <https://www.qiskit.org>`_.

.. jupyter-execute::
    :hide-code:

    %matplotlib inline

    import matplotlib
    import matplotlib.pyplot as plt
    import numpy as np

    from qiskit.visualization import plot_bloch_vector

.. jupyter-execute::

    plot_bloch_vector([1,0,0], title="Bloch Sphere")

.. ---------------------------------------------------------------------------

Download this code: :jupyter-download:notebook:`bloch_sphere`.

.. EOF -----------------------------------------------------------------------
