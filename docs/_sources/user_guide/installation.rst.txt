============
Installation
============

To be able to use pitasc, make sure you :ref:`meet the system requirements <sys-req>`, then :ref:`install pitasc <install>`.

.. _sys-req:

System requirements
===================

pitasc is available for the following 64-bit versions of Ubuntu:

- Ubuntu Focal 20.04 (LTS)

pitasc comes in 2 flavors: 1) is based on `ROS <https://www.ros.org/>`_, 2) is a ROS-less version, e.g., for Reinforcement Learning applications.

For a ROS-based installation, you need to set it up first:

- `ROS Noetic <http://wiki.ros.org/noetic/Installation/Ubuntu>`_ for Ubuntu 20.04

.. _install:

The following hardware requirements have to be met when setting up industrial pcs for robot cells.

.. list-table:: Hardware requirements
   :widths: 25 25 25
   :header-rows: 1

   * - Component
     - Min
     - Recommended

   * - PC
     - PC with disabled thermal energy saving
     - IPC
   * - CPU
     - 6th Gen i5 Intel
     - 9th Gen i7 Intel
   * - RAM
     - 4 GB
     - 16 GB
   * - Hard disk
     - SSD mit minimium 32GB (SATA or NVMe)
     - SSD mit minimium 256GB (SATA or NVMe)
   * - Connectivity
     - Ethernet Switch connecting all items
     - Direct ethernet connection from robot to PC
   * - OS
     - Ubuntu 20.04 with admin rights
     - Ubuntu 20.04 with Realtime patch (included e.g. in Ubuntu Pro) and admin rights


Using the installer
===================

To install pitasc, you need to download the installer or retrieve it from the `pitasc team`_.

.. _pitasc team: pitasc@ipa.fraunhofer.de

1. Download the installer

    - `From Gitlab <https://gitlab.cc-asp.fraunhofer.de/ipa325_public/packages/-/packages/48228>`_

    - Just download the lastest (first) file `without` ``rl`` in the name, eg. ``pitasc-noetic_4.1.0-r127_2024-02-05_amd64.tar.xz``.



2. Install pitasc by extracting the archive file you just downloaded (preferably to your home folder, i.e., "~"; otherwise, adapt the following paths):

.. note::

    The "`$`" sign denotes, that the following line(s) should be executed in a terminal.

.. code-block:: console

    $ tar --directory=$HOME -xJf ~/Downloads/pitasc-VERSION_TAG.tar.xz

3. Install the dependencies according to the respective subsection

ROS-based version
-----------------

.. code-block:: console

    $ rosdep install --from-path ~/pitasc/newest -iy

.. note::

    As noetic is EOL, you need to run ``rosdep update --include-eol-distros`` first.


ROS-less (RL) version for Ubuntu 20.04 (LTS)
--------------------------------------------

.. code-block:: console

    $ sudo apt-get install xz-utils libyaml-cpp0.6 liborocos-kdl1.4 liburdfdom-world libcrypto++6 liburdfdom-model

Optionally, useful for some reinforcement learning or simulation code:

.. code-block:: console

    $ sudo apt-get install -y python3-pykdl
    $ pip3 install urdf_parser_py

Post-installation steps
=======================

Setup the PITASC_FOLDER variable, depending on the pitasc-flavor you installed (Ros-based or not):


.. code-block:: console

    $ PITASC_FOLDER=~/pitasc


and for RL:

.. code-block:: console

    $ PITASC_FOLDER=~/pitasc-rl


Recommended: Configure the newly-extracted version as the current version
-------------------------------------------------------------------------

.. code-block:: console

    $ bash ${PITASC_FOLDER}/select_version.sh

Optional: Enable pitasc by default for the current user
-------------------------------------------------------

.. code-block:: console

    $ echo "source ${PITASC_FOLDER}/current/setup.bash  #autosetup at pitasc install" >> $HOME/.bashrc
    $ source $HOME/.bashrc

Set up a license
----------------

pitasc requires a license key to run. There are two possibilities. Your contact from the pitasc team will let
you know which to use. Execute the corresponding command below in a terminal:

1. Machine specific license (preferred)

    For a machine specific license, execute the following command and follow the
    instructions:

    .. code-block:: console

        $ bash ${PITASC_FOLDER}/current/lib/pitasc/setup_license_file

2. Floating license (fallback, mainly for Docker containers)

    To use a floating license, execute the commmand below and replace ``<LICENSE_SERVER_ADDRESS>`` with the IP
    address of the license server:

    .. code-block:: console

        $ bash ${PITASC_FOLDER}/current/lib/pitasc/use_license_server <LICENSE_SERVER_ADDRESS>

Activate pitasc
===============

    If you did not enable the auto-activation of pitasc, you need to execute
    ``source ~/pitasc/current/setup.bash`` or ``source ~/pitasc-rl/current/setup.bash`` before the commands of pitasc.

Uninstall pitasc
================

1. Remove the pitasc installation folder in "~/pitasc/" and/or "~/pitasc-rl/". You can delete all versions of pitasc by deleting "~/pitasc" and/or "~/pitasc-rl".
2. Disable the automatic activation of pitasc:

.. code-block:: console

    $ echo "$(grep -v "source $HOME/pitasc/current/setup.bash  #autosetup at pitasc install" $HOME/.bashrc)" > $HOME/.bashrc
    $ echo "$(grep -v "source $HOME/pitasc-rl/current/setup.bash  #autosetup at pitasc install" $HOME/.bashrc)" > $HOME/.bashrc
