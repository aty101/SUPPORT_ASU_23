check=0
while [ $check -eq 0 ]
do
read -p "enter the file name:" name
if test  $name;
then
echo "the file exists"
readlink -f $name
check=1
fi
done
