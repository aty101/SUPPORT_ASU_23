read -p "username:" usrname
read -s -p "password:" passwrd

if [ $usrname != "Support" ]
then 
printf "\n"
echo "wrong username"
elif [ ${#passwrd} -lt 8 ]
then
printf "\n"
echo "password must be more than 8 characters " 
fi 

