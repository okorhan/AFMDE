#=============================================================================#
#                                                                             #
#                     The main initialisation module.                         #
#                                                                             #
#-----------------------------------------------------------------------------#
# This module is the main initialisation module setting task parameters.      #
#-----------------------------------------------------------------------------#
# Original version: March 2022 by Okan K. Orhan                               #
#=============================================================================#

#!/bin/python3


import numpy as np
from Modulus.input_info import keywords
from Modulus.output_info import out_write
from Modulus.atomic_info import atom
from Modulus.units_info import units


def input_check(fileinp, fileout):

    # Reading the input file
    inp_lines = []
    with open(fileinp) as fp:
        for line in fp.readlines():
            if line.strip():
                inp_lines.append(line.strip())
    inp_lines = np.array(inp_lines)

    # Checking the task type
    while True:
        try:
            task = inp_lines[1].split("=")[1].lstrip()
            if task not in keywords.task_name:
                out_write.error(fileout, 'Unrecognized task!')
            break
        except IndexError:
            out_write.error(fileout, 'Input file error!')

    if task == 'SRO_Cor':
        out_write.info(fileout, 'Short-ranged order correction to the mean-field disorderliness limit')


    # Checking the task-specific blocks
    for i in range(3):
        if not np.any(inp_lines == keywords(task).inp_blocks[i]):
            out_write.error(fileout,'Missing input block!')

    tind = []
    for i in range(len(inp_lines)):
        if '&' in inp_lines[i]:
            tind.append(i)
    inp_lines = np.delete(inp_lines, tind, None)

    # Checking the task-specific input keywords
    if not len(inp_lines) == keywords(task).inp_keys_num:
        out_write.error(fileout, 'Missing input parameter! ')
    else:
        for i in range(keywords(task).inp_keys_num):
            if inp_lines[i].split("=")[0].rstrip() != keywords(task).inp_keys[i]:
                print(inp_lines[i].split("=")[0].rstrip())
                out_write.error(fileout, 'Bad input keywords! ')

    inp_par =[]
    if task == 'SRO_Cor':
        for i in range(keywords(task).inp_keys_num):
            while True:
                try:
                    tval = inp_lines[i].split("=")[1].lstrip()

                    if i == 0:
                        inp_par.append(tval)

                    if i == 1:
                        if type(tval) == str and 0 < len(tval) < 20:
                            inp_par.append(tval)
                        else:
                            out_write.error(fileout, 'Bad prefix!')

                    if i == 2:
                        tval = tval.split(",")
                        if len(tval) > 1:
                            for j in range(len(tval)):
                                tval[j] = tval[j].strip()
                                if tval[j] not in atom().symbol:
                                    out_write.error(fileout, 'Bad atomic symbol!')
                            inp_par.append(tval)
                        else:
                            out_write.error(fileout, '2 or more principal constituents required!')
                    if i == 3:
                        tval = tval.split(",")
                        if len(inp_par[i-1]) != len(tval):
                            out_write.error(fileout, 'Mismatched number of constituents and molar fractions!')
                        else:
                            for j in range(len(tval)):
                                tval[j] = float(tval[j].strip())
                                if tval[j] < 0  or tval[j] >= 1.0:
                                    out_write.error(fileout, 'Bad molar fraction!')
                        if sum(tval) < 0.95 or sum(tval) > 1.05:
                            out_write.error(fileout, 'Bad molar fraction!')
                        else:
                            tnorm = sum(tval)
                            for j in range(len(tval)):
                                tval[j] = tval[j] / tnorm
                        inp_par.append(tval)

                    if i == 4:
                        tval = tval.strip()
                        if len(tval) < 5 or not tval.endswith(".xlsx"):
                            out_write.error(fileout, 'Bad XLSX file name!')
                        else:inp_par.append(tval)

                    if i == 5:
                        tval = tval.split(",")
                        for j in range(len(tval)):
                            tval[j] = tval[j].strip()
                            if tval[j] not in units().symbol:
                                out_write.error(fileout, 'Bad units!')
                        inp_par.append(tval)

                    if i == 6:
                        tval = int(tval)
                        if tval <=0:
                            out_write.error(fileout, 'Bad MaxRun number!')
                        if tval > 10:
                            out_write.warning(fileout, 'Recommended MaxRun --> 1 - 10 !')
                        inp_par.append(tval)

                    if i == 7:
                        tval = int(tval)
                        if tval <= 0:
                            out_write.error(fileout, 'Bad MaxIt number!')
                        if tval < 100 or tval > 1000:
                            out_write.warning(fileout, 'Recommended MaxIt --> 100 - 10000 !')
                        inp_par.append(tval)

                    if i == 8:
                        tval = int(tval)
                        if tval <= 0:
                            out_write.error(fileout, 'Bad PopSize number!')
                        if tval < 100 or tval > 1000:
                            out_write.warning(fileout, 'Recommended PopSize --> 100 - 1000 !')
                        inp_par.append(tval)

                    if i == 9:
                        if tval == 'T':
                            tval = True
                        elif tval == 'F':
                            tval = False
                        else:
                            out_write.error(fileout, 'Bad logical condition in the input file!')
                        inp_par.append(tval)


                    if i == 10:
                        tval = tval.split(",")
                        if len(tval) < 1 or len(tval) > 4:
                            out_write.error(fileout, 'Bad Obj index!')
                        for j in range(len(tval)):
                            tval[j] = int(tval[j])
                            if not tval[j] in [1, 2, 3, 4]:
                                out_write.error(fileout, 'Bad Obj index!')
                        for j in range(len(tval)):
                            if tval.count(tval[j]) > 1:
                                out_write.error(fileout, 'Repeated Obj index!')
                        inp_par.append(tval)

                    if i == 11:
                        if tval == 'T':
                            tval = True
                        elif tval == 'F':
                            tval = False
                        else:
                            out_write.error(fileout, 'Bad logical condition in the input file!')
                        inp_par.append(tval)

                    if i == 12:
                        tval = tval.split(",")
                        if len(tval) != len(inp_par[i-2]):
                            out_write.error(fileout, 'Mismatched number of ObjIndex and ObjWeight!')
                        for j in range(len(tval)):
                            tval[j] = float(tval[j])
                            if tval[j] < 0 or tval[j] > 1:
                                out_write.error(fileout, 'Bad ObjWeight!')
                        if sum(tval) != 1.0:
                            out_write.error(fileout, 'Bad ObjWeight!')
                        else:
                            inp_par.append(tval)

                    if i == 13:
                        tval = tval.split(",")
                        if len(tval) < 1 or len(tval) > 3:
                            out_write.error(fileout, 'Bad Cons index!')
                        for j in range(len(tval)):
                            tval[j] = int(tval[j])
                            if not tval[j] in [1,2,3]:
                                out_write.error(fileout, 'Bad Cons index!')
                        for j in range(len(tval)):
                            if tval.count(tval[j]) > 1:
                                out_write.error(fileout, 'Repeated Cons index!')
                        inp_par.append(tval)

                    break
                except ValueError:
                    out_write.error(fileout, 'Input value error!')

    return (inp_par)



