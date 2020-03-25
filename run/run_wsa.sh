C=20
ST=100000
for T in 700 900 1100 1300
do
  sbatch -J wsa.${T}.${C} -o slurm_out/wsa.${T}.${C}.o -p RT -N 1 -n 1 --wrap={ovitos ../source/wsa.py $T}
done
