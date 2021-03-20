
############
AboutQuantum
############

The story
=========

I am an aerodynamics engineer, and I have been working for many years
on numerical methods in the realm of Computational Fluid Dynamics (CFD)
and High Performance Computing (HPC).

I have a passion for physics and computer science, and I decided to know more about 
quantum computing.

In January 2020, I started refreshing my Quantum Mechanics,
and by the mid of the year I was able to dive into more complex topics of Quantum Science,
see the :ref:`about/syllabus:Syllabus`.

I had precise goals in mind from the beginning.

.. rubric:: The goals for my self-studies

- Have an idea of the **physical implementations** [#exp1]_ of the various approaches
  to quantum computers and about their underlying physics.
- Understand the principles of **quantum computing**.
- Learn about quantum algorithms and about the problems that can be solved more efficiently than with classical computers.
- Know the current state of the art, and be able to read research papers.

.. rubric:: Why writing?

I have invested a lot of time in learning, in parallel to a full-time job and
to my family duties (ABaba*ba).
I did this without the perspective of getting any kind of certificate,
but I wanted to show that I took this project very seriously, and
that I learned a lot,
so I decided to write down these notes.
Writing helps to **reflect what I have learnt**, and
it is a way to conclude these self-studies.

.. rubric:: What to write?

There are several textbooks that already present and explain the physics I am talking about.
And the topics that are not yet in textbooks, are well described in research articles 
published in peer-reviewed journals, many of them freely accessible.
So it would be senseless to try to explain again these physics in details,
that experts already explained much better than I could.

But what I am missing, is an **overview of Quantum 2.0** [#exp2]_ that lies between,
on one side, introductory slide shows or 20 minute lecture series, and
on the other side, graduate level courses.

Also there are some special topics that, in my opinion,
are to shortly addressed in the textbooks and articles that I know,
and for which I want to provide some illustration.

.. rubric:: The goals for this blog?

- Provide an intermediate level introduction to quantum science.
- Expose some special topics from my personal point of view -
  the one of a nonphysicist - for illustration purposes.
- Offer a path to people with a similar background, 
  who want to learn about Quantum Science.

Finally two principle shall guide me:

- Explain *why*.
- Illustrate.

.. rubric:: Notes

.. [#exp1] This is my main motivation: Understand the background experiments and
    the models that were developed to describe them!

.. [#exp2] There are many online resources about theory and software of quantum computing,
    but I couldn't find an overview with the right level of details
    about the physical implementations and the physical models involved.
    That is the gap I would like to fill.

.. ---------------------------------------------------------------------------

Behind the scenes
=================

.. rubric:: Sphinx

To write this *blog*, I searched for a platform that allows to easily:

* write mathematical equations, preferably in *LaTeX* syntax ;
* manage a bibliography ;
* insert links to internal or external references ;
* present pieces of code and their output, also graphical elements (figures) ;
* edit the contents on my local computer, without depending on a web app ;
* use a versioning system.

Additionally I wanted the page to render nicely on large screens
as well as on mobile devices.

This is why I chose `Sphinx <https://www.sphinx-doc.org/>`_,
that was initially designed for documenting *python* code,
and has everything I was looking for.

So, finally, it looks a bit like I am building a *Quantum Science Manual*. :)

.. EOF -----------------------------------------------------------------------
