# =============================================================================#
#                                                                             #
#                 The Bravais lattice information module.                     #
#                                                                             #
# -----------------------------------------------------------------------------#
# This module contains the Bravais lattice vectors, volumes for given lattice #
# parameters.                                                                 #
# -----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
# =============================================================================#

# !/bin/python3

import numpy as np
from Modulus.output_info import out_write


class bravais:
    def __init__(self, fileout, ibrav, celldm):
        if ibrav == 1:
            if len(celldm) == 1:
                a = celldm[0]
                self.lat_vec = a * np.array([[1.0, 0.0, 0.0],
                                             [0.0, 1.0, 0.0],
                                             [0.0, 0.0, 1.0]])
                self.volume = a * a * a
            else:
                out_write.error(fileout, 'Wrong lattice parameter (s) for Bravais index ' + str(ibrav))

        elif ibrav == 2:
            if len(celldm) == 1:
                a = celldm[0]
                self.lat_vec = 0.5 * a * np.array([[-1.0, 0.0, 1.0],
                                                   [0.0, 1.0, 1.0],
                                                   [-1.0, 1.0, 0.0]])
                self.volume = 0.25 * (a * a * a)
            else:
                out_write.error(fileout, 'Wrong lattice parameter (s) for Bravais index ' + str(ibrav))

        elif ibrav == 3:
            if len(celldm) == 1:
                a = celldm[0]
                self.lat_vec = 0.5 * a * np.array([[1.0, 1.0, 1.0],
                                                   [-1.0, 1.0, 1.0],
                                                   [-1.0, -1.0, 1.0]])
                self.volume = 0.25 * (a * a * a)
            else:
                out_write.error(fileout, 'Wrong lattice parameter (s) for Bravais index ' + str(ibrav))

        elif ibrav == 4:
            if len(celldm) == 2:
                a = celldm[0]
                c = celldm[1]
                self.lat_vec = a * np.array([[1.0, 0.0, 0.0],
                                             [-1.0 / 2.0, np.sqrt(3.0) / 2.0, 0.0],
                                             [0.0, 0.0, c / a]])
                self.volume = (0.5 * a * a * np.sin(np.pi * 120 / 180)) * c
            else:
                out_write.error(fileout, 'Wrong lattice parameter (s) for Bravais index ' + str(ibrav))
