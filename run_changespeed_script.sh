echo "Script that runs all the code for Final Project (with section of road with lower speed) - MCSC 6040"
echo "Written by Darryen Sands"

icc ProjectCode.c -o sim.x -O3 -lm
rm -rf flowdata.txt
rm -rf velocitydata.txt

echo "10^5 Timesteps with no road slowing"
for i in $(seq 0 0.005 0.8); do
    density=$(printf "%.4f" $i)
    echo $density
    ./sim.x $density 0.5 10000 100000 0 0.0 0
done

echo "10^6 Timesteps with road slowing"
for i in $(seq 0 0.005 0.8); do
    density=$(printf "%.4f" $i)
    echo $density
    ./sim.x $density 0.5 10000 100000 0 0.0 1
done

python3 plotextension.py 1