END=37
for ((i = 0; i <= END; i++)); do
    java Hilldescent < $i.in > $i.ans
done 
