read -p "enter the file name:"  file_name

tr -d [:space:] < $file_name | cat
