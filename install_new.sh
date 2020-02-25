cd /home/
mkdir ubuntu
cd ubuntu
sudo ufw allow 9444/tcp
sudo ufw allow 9446/udp
sudo apt update
sudo apt install haveged -y
sudo apt install openjdk-8-jdk -y
sudo apt install supervisor -y
git clone https://github.com/YanDevDe/nyzoVerifier.git
cd nyzoVerifier
./gradlew build
sudo mkdir -p /var/lib/nyzo/production
sudo cp trusted_entry_points /var/lib/nyzo/production
sudo cp nyzoVerifier.conf /etc/supervisor/conf.d
######################### args: nickname
echo $1 > /var/lib/nyzo/production/nickname
######################### track the blockchain continuously if in candidate state
echo 'always_track_blockchain=1' > /var/lib/nyzo/production/preferences
#########################
sudo supervisorctl reload
sudo supervisorctl status
echo "@reboot sudo supervisorctl reload" >> mycron
crontab mycron
rm mycron
