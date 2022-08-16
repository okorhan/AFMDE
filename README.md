SUMMARY:

The A Fair Materials Discovery Engine (AFMDE)  is an early version of collection of routines for corrective post-processing approaches
for materials discovery.

TECHNICAL DETAILS:
	
	VERSIONS:

		- Python 3.8.10
		- Numpy 1.20.2
		- Pandas 1.2.4
		- Openpyxl 3.0.9

TASKS:

	1) SRO_Cor

		This routine is to obtain the coefficients for the short-ranged order correction to the multi-principal elements solids
		(MPES), simulated at the disordered mean-field limit within the virtual crystal approximation.

		It uses the properties of the subsystems of a given multi-principal-elements solid as corrective terms, weighted by
		a set of coefficients , which are calculated using the particle-swarm optimization algorithm.

		Please see [CITE] for further details.


		RUN DETAILS:

    			- Input files
            			1) Input.in : Initialization parameters in text format
            			2) Data.xlsx : Materials data for MPES, and its subsystems
    			- To run:
            			$ python3 main.py Input.in Output.out
    			- Output file:
            			- Output.out : Summary of the simulation
            			- *.xlsx : XLSX file, containing the coefficients, and SRO-corrected materials properties


		INPUT STRUCTURES:
	
		   	& TaskInfo
        			Task = SRO_Cor                                  	--> Task type
        			Prefix = String		 		        	--> Prefix for *.xlsx output
        			Elements = A, B, C, D, E				--> List of atomic symbols in MPES
        			MolarFrac = 0.2, 0.2, 0.2, 0.2, 0.2			--> List of molar fractions of principal elements ( Total[MolarFrac] = 1.0 )

    			& FilesInfo
        			XLSXFile = *.xlsx					--> Path/*.xlsx input file
        			Units = J/eV/Ry/Ha, m/Angtrom/Bohr, bar/PA/GGPa		--> Energy, length, pressure units in XLSXFile

    			& OptimizationInfo                                       
        			MaxRun = 10						--> Max number of PSO run 
        			MaxIt = 1000						--> Max iteration of each PSO run
        			PopSize = 100						--> Population size of swarm
        			OptHistory = T						--> If T, writing the global best for each improved iterations during PSO
        			ObjIndex =  1, 2, 3, 4					--> List of the objective index (see below)
        			FixedObjWeight = T					--> If T, the realtive weight of each objective is fixed as given in the next line
        			ObjWeight = 0.25, 0.25, 0.25, 0.25			--> List of the realtive objective weights ( Total[ObjWeight] = 1.0 )
        			ConsIndex = 1, 2					--> List of the constraint index (see below)





		OBJECTIVES:

        		O1 : Gibbs free energy - requiring Gibbs free energies in a column in XLS file, named "Obj 1"
        		O2 : Lattice misfit parameter - requiring lattice parameters in a column in XLS file, named "Obj 2"
        		O3 : Valence electron density mismatch parameter - requiring VEC in a column in XLS file, named "Obj 3"
        		O4 : Mulliken electronegativity mismatch parameters, requiring el.neg. in a column in XLS file, named "Obj 4"

		CONSTRAINTS:

        		C1 : beta_i^m <= 1/ (m M)               --> M: Number of principal metals, m: Number of sub-principal metals
        		C2 : sum_{mj}^{Sub_mj} beta_j^m         --> Sub_mj : Set of sub-system, including metal m






