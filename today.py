cd /home/
rm /home/URNAME.sql
rm /home/today.zip
wget http://www.blahblah.gov.mm/URNAME.sql /home/URNAME.sql
wget http://www.blahblah.gov.mm/today.zip /home/today.zip
echo "Import Database..."
mysql -u root -pYOURsecretkey URNAME < /home/URNAME.sql
echo "Restore Web..."
unzip -o /home/today.zip
sed -i 's/YOURsecretkey/YOURsecretkey/g' /home/var/www/html/index/configuration.php
sed -i 's/username/root/g' /home/var/www/html/index/configuration.php
Change dir:

/home/
