#=============================================================================#
#                                                                             #
#                     The external database module.                      #
#                                                                             #
#-----------------------------------------------------------------------------#
# This module reads the external database (if applicable).                    #
#-----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
#=============================================================================#

#!/bin/python3

import numpy as np
import pandas as pd
from Modulus.output_info import out_write

def raw_data(inp_par, fileout):

    fout = open(fileout, "a")

    # Reading XLSX file if task = SRO_Cor
    if inp_par[0] == 'SRO_Cor':
        tdata =[]

        # Checking XLSX file existence
        while True:
            try:
                xlsxfile = pd.ExcelFile(inp_par[4]).parse(0)
                break
            except FileNotFoundError:
                out_write.error(fileout, 'XLSX file not found!')

        # Checking for molar fractions

        xlsx_col_name = []
        for i in range(len(xlsxfile.columns)):
            xlsx_col_name.append(xlsxfile.columns[i])
        xlsx_col_name = pd.Series(xlsx_col_name)


        for ttag in inp_par[2]:
            if xlsx_col_name.str.contains(ttag).any():
                tind = np.where(xlsx_col_name.str.contains(ttag))[0]
                if len(tind) == 1:
                    tdata.append(xlsxfile[xlsxfile.columns[tind[0]]])
                else:
                    out_write.error(fileout, 'Repeated columns in XLSX file!')
            else:
                out_write.error(fileout, 'Missing molar fractions in XLSX file!')

        tdata = pd.DataFrame(tdata).T

        # Determining indices of main system and sub-systems
        sys_ind = []
        for i in range(len(tdata)):
            a1 = np.around(np.array(inp_par[3]), decimals = 3)
            a2 = np.around(tdata.iloc[i], decimals = 3)
            if (np.array_equal(a1, a2)):
                sys_ind.append(i)

        if len(sys_ind) == 0:
            out_write.error(fileout, +inp_par[1]+' data is missing in XLSX data!')


        sub_sys_ind = tdata.sum(axis = 1)[round(tdata.sum(axis = 1),1) == 1.0].index
        sub_sys_ind = sub_sys_ind.drop(sys_ind)
        tdata = pd.concat([xlsxfile.iloc[sys_ind],xlsxfile.iloc[sub_sys_ind]])
        num_sys = len(sub_sys_ind) + 1

        # Collecting the data of the relevant systems
        ext_data = []
            # Molar fractions
        for ttag in inp_par[2]:
            ext_data.append(tdata[ttag])
        ext_data = pd.DataFrame(ext_data).T

        xlsx_col_name = xlsx_col_name.str.lower()
            # Name tags
        if xlsx_col_name.str.contains('name').any():
            if sum(xlsx_col_name.str.count('name')) == 1:
                tind = np.where(xlsx_col_name.str.contains('name'))[0]
                ext_data['Name'] = tdata[tdata.columns[tind[0]]]
            else:
                out_write.error(fileout, 'Repeated columns in XLSX file!')
        else:
            out_write.warning(fileout, 'Missing name tags in XLSX file! System generated tag names will be used.')
            tlist = []
            for i in range(num_sys):
                tname = ''
                for j in range(len(inp_par[2])):
                    tname = tname + inp_par[2][j] + '_' + '%.2f' % ext_data[inp_par[2][j]].iloc[i]
                tlist.append(tname)
            ext_data['Name'] = pd.Series(tlist, index = ext_data.index)

            # Bravais index
        if xlsx_col_name.str.contains('bravais').any():
            if sum(xlsx_col_name.str.count('bravais')) == 1:
                tind = np.where(xlsx_col_name.str.contains('bravais'))[0]
                ext_data['Bravais'] = tdata[tdata.columns[tind[0]]]
            else:
                out_write.error(fileout, 'Repeated columns in XLSX file!')
        else:
            out_write.warning(fileout, 'Missing Bravais indices in XLSX file! '
                           'Simple-cubic structure is assumed.')
            tlist = []
            for i in range(num_sys):
                tlist.append(int(1))
            ext_data['Bravais'] = pd.Series(tlist, index=ext_data.index)

            # Bravais index
        if xlsx_col_name.str.contains('bravais').any():
            if sum(xlsx_col_name.str.count('bravais')) == 1:
                tind = np.where(xlsx_col_name.str.contains('bravais'))[0]
                ext_data['Bravais'] = tdata[tdata.columns[tind[0]]]
            else:
                out_write.error(fileout, 'Repeated columns in XLSX file!')
        else:
            out_write.warning(fileout, 'Missing Bravais indices in XLSX file! '
                           'Simple-cubic structure is assumed.')
            tlist = []
            for i in range(num_sys):
                tlist.append(int(1))
            ext_data['Bravais'] = pd.Series(tlist, index=ext_data.index)

            # Objectives 1 or 2 --> Lattice parameters
        if 1 in inp_par[10] or 2 in inp_par[10]:
            if xlsx_col_name.str.contains('celldm').any():
                if sum(xlsx_col_name.str.count('celldm')) <= 6:
                    tind = np.where(xlsx_col_name.str.contains('celldm'))
                    for i in range(len(tind[0])):
                        ext_data['Celldm ' + str(i+1)] = tdata[tdata.columns[tind[0][i]]]
                else:
                    out_write.error(fileout, 'Repeated lattice parameters in XLSX file!')
            else:
                out_write.error(fileout, 'Missing lattice parameters in XLSX file!')

            # Objective 1 -->
        if 1 in inp_par[10]:
                # Free energy
            if xlsx_col_name.str.contains('energy').any():
                if sum(xlsx_col_name.str.count('energy')) == 1:
                    tind = np.where(xlsx_col_name.str.contains('energy'))[0]
                    ext_data['Energy'] = tdata[tdata.columns[tind[0]]]
                else:
                    out_write.error(fileout, 'Repeated columns in XLSX file!')
            else:
                out_write.error(fileout, 'Missing free energies in XLSX file!')

                # Bulk modulus
            if xlsx_col_name.str.contains('bulk').any():
                if sum(xlsx_col_name.str.count('bulk')) == 1:
                    tind = np.where(xlsx_col_name.str.contains('bulk'))[0]
                    ext_data['Bulk modulus'] = tdata[tdata.columns[tind[0]]]
                else:
                    out_write.error(fileout, 'Repeated columns in XLSX file!')
            else:
                out_write.warning(fileout, 'Missing bulk modulus in XLSX file! '
                           'Elastic energy correction will be ignored')

            # Objective 3 --> Valence electron density
        if 3 in inp_par[10]:
            if xlsx_col_name.str.contains('valence').any():
                if sum(xlsx_col_name.str.count('valence')) == 1:
                    tind = np.where(xlsx_col_name.str.contains('valence'))[0]
                    ext_data['VEC'] = tdata[tdata.columns[tind[0]]]
                else:
                    out_write.error(fileout, 'Repeated columns in XLSX file!')
            else:
                out_write.error(fileout, 'Missing valence electron concentrations in XLSX file!')

            # Objective 4 --> Electronegativity
        if 4 in inp_par[10]:
            if xlsx_col_name.str.contains('electronegativity').any():
                if sum(xlsx_col_name.str.count('electronegativity')) == 1:
                    tind = np.where(xlsx_col_name.str.contains('electronegativity'))[0]
                    ext_data['Electronegativity'] = tdata[tdata.columns[tind[0]]]
                else:
                    out_write.error(fileout, 'Repeated columns in XLSX file!')
            else:
                out_write.error(fileout, 'Missing electronegativities in XLSX file!')

    return ext_data.reset_index(drop=True)


