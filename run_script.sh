echo "Script that runs all the code for Final Project - MCSC 6040"
echo "Written by Darryen Sands"

icc ProjectCode.c -o sim.x -O3 -lm
rm -rf flowdata.txt

python3 plotroaddata.py

for i in $(seq 0 0.0005 0.12); do
    density=$(printf "%.4f" $i)
    echo $density
    ./sim.x $density 0.5 10000 100 0
done

for i in $(seq 0.12 0.01 0.8); do
    density=$(printf "%.4f" $i)
    echo $density
    ./sim.x $density 0.5 10000 100 0
done

echo "10^6 Timesteps"
for i in $(seq 0 0.01 0.8); do
    density=$(printf "%.4f" $i)
    echo $density
    ./sim.x $density 0.5 10000 100000 0
done

python3 plotproject.py