C=20
ST=100000
for T in 800 1000 1200 1400 1600 1800
do
  sbatch -J com.${T}.${C} -o slurm_out/comp.${T}.${C}.o -p RT -N 1 -n 1 --wrap='mpirun -np 1 python ../source/compute_diff.py $T'
done
