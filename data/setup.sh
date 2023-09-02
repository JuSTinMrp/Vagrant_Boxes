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


#removing unwanted user

sudo deluser ubuntu
rm -rf /home/ubuntu

sudo systemctl restart ssh

cp /data/us3r.png /home/cyberrav/us3r.png

