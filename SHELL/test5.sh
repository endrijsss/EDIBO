#!/bin/bash  
echo "Ebter the first ip"
read ip1
echo "Enter the second ip"
read ip2

a=`echo "obase=2;$ip1" | bc`
b=`echo "obase=2;$ip2" | bc`
echo $a
echo $b  
