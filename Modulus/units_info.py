# =============================================================================#
#                                                                             #
#                     The unit conversion module.                             #
#                                                                             #
# -----------------------------------------------------------------------------#
# This module contains unit conversions constants.                            #
# -----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
# =============================================================================#

# !/bin/python3

class units:

    def __init__(self):
        self.symbol = ['J', 'eV', 'Ha', \
                     'm', 'Angstrom', 'Bohr',
                     'bar', 'Pa', 'GPa']


class convert:

    def __init__(self):
        # Energy and work conversions
        self.J2eV = 6.241506363e+18
        self.eV2J = 1.0 / self.J2eV
        self.J2Ry = 4.587420897e+17
        self.Ry2J = 1.0 / self.J2Ry
        self.J2Ha = 2.293710449e+17
        self.Ha2J = 1.0 / self.J2Ha

        self.eV2Ry = 0.073498618
        self.eV2Ha = 0.036749309

    # Length, area and volume conversions

        self.a02m = 5.29177249e-11
        self.A2m = 1.0e-10
        self.a02A = 5.29177249e-1
        self.m2a0 = 1.0 / self.a02m
        self.m2A = 1.0 / self.A2m
        self.A2a0 = 1.0 / self.a02A

        self.a02m_2 = self.a02m * self.a02m
        self.A2m_2 = self.A2m * self.A2m
        self.a02A_2 = self.a02A * self.a02A

        self.a02m_3 = self.a02m * self.a02m * self.a02m
        self.A2m_3 = self.A2m * self.A2m * self.A2m
        self.a02A_3 = self.a02A * self.a02A * self.a02A

    # Pressure conversions

        self.bar2Pa = 1.0e6


