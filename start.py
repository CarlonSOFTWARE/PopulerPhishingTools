import os
import pyfiglet

clear = lambda: os.system("clear")
restart = lambda: os.system("python x.py")

zphisher = lambda: os.system("git clone https://github.com/htr-tech/zphisher && cd && cd zphisher && bash zphisher.sh")
pyphisher= lambda: os.system("pkg install python3 && git clone https://github.com/KasRoudra/PyPhisher && cd && cd PyPhisher && pip3 install -r files/requirements.txt --break-system-packages && python3 pyphisher.py")
socialfish = lambda: os.system("pkg install python3 && git clone https://github.com/UndeadSec/SocialFish && python3 SocialFish.py")
nexphisher = lambda: os.system("apt update ; apt install git -y ; git clone git://github.com/htr-tech/nexphisher.git ; cd nexphisher ; bash setup ; bash nexphisher")

advphishing = lambda: os.system("git clone https://github.com/Ignitetch/AdvPhishing && cd && cd AdvPhishing && chmod 777* && ./Android-Setup.sh && /Linux-Setup.sh && ./AdvPhishing.sh")


clear()

def secim():
    global clear
    while True:
        question = input(f"Seçim: ").upper().replace(" ", "")
        if question == "1":
            zphisher()
            restart()
             
        if question == "2":
            pyphisher()
            restart()
        if question == "3":
            socialfish()
            restart()
        if question == "4":
            nexphisher()
            restart()
        if question == "5":
            advphishing()
            restart()
        if question == "6":
            clear()
            print("Çıkış Yapıldı! Kullandığınız İçin Teşekkür Ederim!")
            exit()
  
           
def banner():
    global clear
    
import pyfiglet

banner = pyfiglet.figlet_format("Popular Phishing Tools", font="slant")


print('\033[1;32;40m' + banner + '\n\033[1;36;40m'  '\033[0;37;40m')
print('\033[1;31;40m' + "                                                        github.com /CarlonSOFTWARE" + '\033[0;37;40m')
print('\033[1;31;40m' + "                                                        Developer: Carlon" + '\033[0;37;40m')
print('''
\033[1;33;40m1)Zphisher
\033[1;34;40m2)PyPhisher
\033[1;35;40m3)SocialFish
\033[1;36;40m4)NexPhisher
\033[1;37;40m5)AdvPhishing
\033[1;31;40m6)Çıkış
''')





secim()