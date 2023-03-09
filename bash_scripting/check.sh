num=1

while [ $num -lt 21 ]
do
if [ $num -lt 10 ]
then 
echo "this is num $num"
cat 0x0$num.sh
else
echo "this is num $num"
cat 0x$num.sh
fi
num=`expr $num + 1`
done
