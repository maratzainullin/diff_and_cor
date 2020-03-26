C=20
ST=100000
for T in 800 1000 1200 1400 1600 1800
do
  sbatch -J wsa.${T}.${C} -o slurm_out/wsa.${T}.${C}.o -p RT -N 1 -n 1 --wrap='mpirun -np 1 ovitos ../source/wsa.py $T'
done
