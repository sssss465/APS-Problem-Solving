END=46
for ((i = 0; i <= END; i++)); do
    ./a.out < $i.in > $i.ans
done 
