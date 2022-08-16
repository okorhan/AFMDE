#=============================================================================#
#                                                                             #
#                     The output files module.                                #
#                                                                             #
#-----------------------------------------------------------------------------#
# This module produces outputs files.                                         #
#-----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
#=============================================================================#

#!/bin/python3

import sys

class out_write(object):

    def __init__(self, fileout):
        fout = open(fileout, "w")
        fout.write('#=============================================================================#\n'
                   '#                                                                             #\n'
                   '#                           The main CORRECT program.                         #\n'
                   '#                                                                             #\n'
                   '#-----------------------------------------------------------------------------#\n'
                   '# The CORRECT code is written by Okan K. Orhan, Mewael Isiet, Mauricio Ponga  #\n'
                   '#-----------------------------------------------------------------------------#\n'
                   '# Original version: March 2022 by Okan K. Orhan                               #\n'
                   '#=============================================================================#\n')
        fout.close()

    def process_init(fileout, line):
        fout=open(fileout, "a")
        fout.write('\n\n ---> ' + line + ' ...\n')
        fout.close()

    def process_end(fileout):
        fout=open(fileout, "a")
        fout.write('\n\n... DONE <---\n')
        fout.close()

    def error(fileout, line):
        fout=open(fileout, "a")
        fout.write('\n ERROR: ' + line)
        fout.write('\n\n Calculation terminated!  BYE BYE!')
        sys.exit('\n Calculation terminated!')

    def warning(fileout, line):
        fout=open(fileout, "a")
        fout.write('\n WARNING: ' + line)

    def info(fileout, line):
        fout=open(fileout, "a")
        fout.write('\n INFO: ' + line)

    def iter(fileout, indentation, case, irun, opt = ''):
        fout = open(fileout, "a")
        fout.write('\n ' + ' ' * indentation + case + str(irun) + opt)

    def misc(fileout, indentation, tag, opt = ''):
        fout = open(fileout, "a")
        fout.write('\n ' + ' ' * indentation + tag + opt)

