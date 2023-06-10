#!/bin/sh

 for file in `ls *.cube`
do 
echo $file
awk '{if(NR>38){print $0}}' ${file} >./temp_test/${file}_nohead 
done
