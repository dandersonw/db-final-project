if [ -f $RDLIST_CONFIG_PATH/db_config ]
then
   echo "User config found!"
   exit
fi

mkdir -p $RDLIST_CONFIG_PATH

read -p "Enter username for app [readinglist]: " username
username=${username:-readinglist}

pass=$(openssl rand -base64 32)
mkdir -p $RDLIST_CONFIG_PATH

read -p "Enter database hostname [localhost]: " hostname
hostname=${hostname:-localhost}

read -p "Enter database port [3306]: " port
port=${port:-3306}

echo "[DEFAULT]" > $RDLIST_CONFIG_PATH/db_config
echo "username=$username" >> $RDLIST_CONFIG_PATH/db_config
echo "pass=$pass" >> $RDLIST_CONFIG_PATH/db_config
echo "hostname=$hostname" >> $RDLIST_CONFIG_PATH/db_config
echo "port=$port" >> $RDLIST_CONFIG_PATH/db_config

echo "Enter MySQL root password"
echo "CREATE USER '$username'@'$hostname' IDENTIFIED BY '$pass';" \
    | mysql --host="$hostname" --port="$port" -uroot -p
echo "GRANT ALL PRIVILEGES ON *.* TO '$username'@'$hostname';" \
    | mysql --host="$hostname" --port="$port" -uroot -p
