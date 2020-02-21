lmp_serial -in diff.lmp -l none -var l 2.8712 -var t 1300 && lmp_serial -in restart_to_data.lmp -l none -var l 2.8712 -var t 1300 && python read_and_shift.py 2.8712 1300

# `mpirun -np 16 ../../tools/lammps/src/lmp_mpi -in

# sbatch -J diff700 --exclusive -p RT -N 3 -n 48 --wrap="mpirun -np 48 ~/tools/lammps/src/lmp_mpi -in diff.lmp -l none -var l 2.8712 -var t 700"

# sbatch -J diff150012 --comment t1500l12Time10e5ps -p RT -N 3 -n 48 --wrap="mpirun -np 48 ~/tools/lammps/src/lmp_mpi -in diff.lmp -l none -var l 2.9044 -var t 1500"
# sbatch -J r2d700 --comment t700l12Time10e5ps -p RT -N 1 -n 16 --wrap="mpirun -np 16 ~/tools/lammps/src/lmp_mpi -in restart_to_data.lmp -l none -var l 2.8712 -var t 700"


variable TEMP index   600    700     800     900    1000    1100    1300    1500    1700
variable period index 2.8680  2.8712   2.8746   2.8781  2.8822  2.8861  2.8947  2.9044  2.9151
                              12.9204           12.95145        12.98745 13.02615 13.0698 13.11795
