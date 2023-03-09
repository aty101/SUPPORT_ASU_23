echo "Please enter a number between 20 and 30"
read num


while [ $num -lt 20 -o $num -gt 30 ]
do
echo "Please enter a number between 20 and 30"
read num
done
echo "Thank you"

