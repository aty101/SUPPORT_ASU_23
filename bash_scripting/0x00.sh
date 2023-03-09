count=1

while [ $count -le 20 ]
do
if [ $count -lt 10 ]
then 
touch 0x0$count.sh
count=`expr $count + 1`
else
touch 0x$count.sh
count=`expr $count + 1`
fi
done
