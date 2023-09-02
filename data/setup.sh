#!/bin/bash

# updating packages
sudo apt-get update -y

# # setting up banner 
# sudo apt-get install figlet -y && sudo apt install lolcat -y
# echo "figlet -f slant "! CyberraV !" -c | lolcat" >> ~/.bashrc
# source ~/.bashrc

# installing ssh
sudo apt-get install ssh -y
sudo systemctl restart ssh

# setup xclip for easy usage
sudo apt install xclip -y

# installing python
sudo apt install python -y
sudo apt install python3-pip -y
sudo apt-get install python3-pip python-dev -y
sudo pip install --upgrade pip
sudo pip3 install pycrypto
sudo pip3 install pycryptodome
sudo pip3 install cryptography

# installing exiftool
sudo apt install exiftool -y

#setting up users and permissions
sudo deluser cyberrav
sudo delgroup cyberrav

sudo useradd cyberrav
sudo mkdir -p /home/cyberrav
sudo chown cyberrav:cyberrav /home/cyberrav
sudo bash -c "echo 'cyberrav:g0t_my_a1ms' | chpasswd"

#another one user (root)
sudo deluser justin
sudo delgroup justin

sudo useradd justin
sudo mkdir -p /home/justin
sudo chown justin:justin /home/justin
sudo bash -c "echo 'justin:h33l_up_th1ng577' | chpasswd"

#change passwd for vagrant user
sudo bash -c "echo 'vagrant:things_you_will_never_know' | chpasswd"




#removing unwanted user

sudo deluser ubuntu
sudo rm -rf /home/ubuntu

sudo cp /data/new_sshd_config /etc/ssh/sshd_config
sudo systemctl restart ssh
#sudo service ssh restart

# setting up flag_1
sudo rm /home/cyberrav/us3r.png
sudo cp /data/us3r.png /home/cyberrav/us3r.png
sudo chmod 400 /home/cyberrav/us3r.png
sudo chown cyberrav /home/cyberrav/us3r.png


# setting up flag_2 clue
sudo rm /home/cyberrav/Flag2.txt
sudo cp /data/Flag2.txt /home/cyberrav/Flag2.txt
sudo chmod 400 /home/cyberrav/Flag2.txt
sudo chmod 400 /home/cyberrav
sudo chown cyberrav /home/cyberrav/Flag2.txt
sudo chown cyberrav /home/cyberrav



# setting up flag_2
#cp /data/ r00t.txt  /home/justin/
cp /data/ r00t.txt  /home/justin/get_the_flag/
sudo chmod 400 /home/justin/ r00t.txt 
sudo chmod 400 /home/justin
sudo chown justin /home/justin/ r00t.txt 
sudo chown justin /home/justin

# generating root flag
echo "THM{M45T3R_3V3RYTH1NG}" > $(printf "\u2000r00t.txt\u2000")



