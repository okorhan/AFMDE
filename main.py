#=============================================================================#
#                                                                             #
#                           Main routine of AFMDE                             #
#                                                                             #
#-----------------------------------------------------------------------------#
# This code is written by Okan K. Orhan                                       #
#-----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
#=============================================================================#

#!/bin/python3


# Libraries
import sys
from Modulus.initialisation import input_check
from Modulus.output_info import out_write

# Arguments for executable
fexe, fileinp, fileout=sys.argv

# Writing header in output file
out_write(fileout)

# Checking the input file and collecting input parameters
out_write.process_init(fileout, 'Checking the input file')
inp_par = input_check(fileinp, fileout)
out_write.process_end(fileout)

if inp_par[0] == 'SRO_Cor':
    from Modulus.external_database import raw_data
    from Modulus.SRO_UAPSO import UAPSO

    # Reading the XLS file
    out_write.process_init(fileout,'Checking the XLSX file for short-ranged order correction')
    ext_data = raw_data(inp_par, fileout)
    out_write.process_end(fileout)

    # Performing UAPSO
    out_write.process_init(fileout,'Running the unique adaptive particle-swarm optimization (UAPSO)')
    UAPSO(fileout, inp_par, ext_data)
    out_write.process_end(fileout)











