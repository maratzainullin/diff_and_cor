#!/bin/sh
#SBATCH -J diff1700
#SBATCH --exclusive
#SBATCH -o 1700k.out
#SBATCH --comment t1700l10Time5*10e4ps
#SBATCH -p RT
#SBATCH -N 2
#SBATCH -n 32
#SBATCH
# cell_size = 10
# temperature = 1700
# lattice = 2.9151
#
# mkdir -p pp


mpirun -np 16 lmp_mpi diff.lmp -in -var cell 10 -var lattice 2.8712 -var temp 700 -var simtime 50000 &
mpirun -np 16 lmp_mpi r2d.lmp -in -var cell 10 -var lattice 2.8712 -var temp 700 -var simtime 50000

# variable TEMP index   600    700     800     900    1000    1100    1300    1500    1700
# variable period index 2.8680  2.8712   2.8746   2.8781  2.8822  2.8861  2.8947  2.9044  2.9151
#                               12.9204           12.95145        12.98745 13.02615 13.0698 13.11795





#sbatch --job-name=$RUNTYPE.$RUNNUMBER.run --output=$RUNTYPE.$RUNUMBER.txt --export=A=$A,b=$b jobscript.sbatch
