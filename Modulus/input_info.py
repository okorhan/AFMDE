#=============================================================================#
#                                                                             #
#                     The input keywords module.                              #
#                                                                             #
#-----------------------------------------------------------------------------#
# This module contains task-specific input keywords.                          #
#-----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
#=============================================================================#

#!/bin/python3

class keywords(object):

    task_name = ['SRO_Cor', "Future_Task"]

    def __init__(self, task):
        if task == 'SRO_Cor':
            self.inp_blocks = ['& TaskInfo', '& FilesInfo', '& OptimizationInfo']
            self.inp_keys = ['Task', 'Prefix', 'Elements', 'MolarFrac', \
                        'XLSXFile',  'Units', \
                        'MaxRun', 'MaxIt', 'PopSize', 'OptHistory', \
                        'ObjIndex', 'FixedObjWeight', 'ObjWeight', \
                        'ConsIndex']
            self.inp_keys_num = len(self.inp_keys)




