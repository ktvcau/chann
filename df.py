# Óc chó thì dùng ít thôi, mục đích là trải nghiệm
# Cao Tiến Thành (Mai Cửu)

try:

   import os

   import sys

   import time

   import random

   import os.path

   import requests

   import threading

except ImportError:

   exit("Hãy cài đặt >pip install requests< và thử lại.")

os.system("git pull")

os.system("clear")

red    = "\033[31m"

blue   = "\033[34m"

bold   = "\033[1m"

reset  = "\033[0m"

green  = "\033[32m"

yellow = "\033[33m"

colors = [

    "\033[38;5;226m",

    "\033[38;5;227m",

    "\033[38;5;229m",

    "\033[38;5;230m",

    "\033[38;5;190m",

    "\033[38;5;191m",

    "\033[38;5;220m",

    "\033[38;5;221m",

    "\033[38;5;142m",

    "\033[38;5;214m",

]

color1, color2, color3, color4, color5 = random.sample(colors, 5)

banner = f"""
\n\033[36m┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓\t
\033[31m  ● The function of the tool : Edit files, web content\t
\033[36m┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛\t
\n\033[31m>Warning<\t\033[1mChỉ mạng tính chất giải trí\t
\n\033[0mChỉ là chỉnh sửa được web lỏ thôi, mục đích gọi là sống ảo!
"""+reset+blue

def animate():

    text = "Vui lòng đợi, nó đang được tải lên website..."

    while True:

        for i in range(len(text)):

            print(text[:i] + "_" + text[i+1:], end="\r")

            time.sleep(0.1)

def eagle(tetew):

   ipt = ''

   if sys.version_info.major > 2:

      ipt = input(tetew)

   else:

      ipt = raw_input(tetew)   

   return str(ipt)

def white(script, target_file="targets.txt"):

    op = open(script, "r").read()

    with open(target_file, "r") as target:

        target = target.readlines()

        s = requests.Session()

        print(" ")

        print(green+bold+"« Cao Tien Thanh »\033[0m \033[34mĐang được tải lên %d website...." % (len(target)), end="", flush=True)

        print(" ")

        t = threading.Thread(target=animate)

        t.daemon = True 

        t.start()                

        for web in target:

            try:

                site = web.strip()

                if site.startswith("http://") is False:

                    site = "http://" + site

                req = s.put(site + "/index.html", data=op)

                if req.status_code < 200 or req.status_code >= 250:

                    print(red + " « Cao Tien Thanh » " + bold + " Không thể lại lên được   \033[0m     " + red + " ! %s/%s" % (site, script))

                else:

                    print(green + " « Cao Tien Thanh » " + bold + " Thành công  \033[0m" + green + " ! %s/%s" % (site, script))

            except requests.exceptions.RequestException:

                continue

            except KeyboardInterrupt:

                print;

                exit()

def main(__bn__):

   print(__bn__)

   while True:

      try:

         print(green+'Vui lòng để script /.html trong cùng thư mục và nhập tên của nó bên dưới'+reset+blue)

         print(' ')

         a = eagle(green+" « Cao Tien Thanh » \033[0m \033[34mNhập tên file /.html của bạn\n\033[33mVí dụ: script.html\033[0m \033[34m> ")

         if not os.path.isfile(a):

            print(' ')

            print(red+bold+"	file '%s' không tìm thấy trong thư mục này !"%(a))

            print(" ")

            continue

         else:

            break

      except KeyboardInterrupt:

         print; exit()

   white(a)

if __name__ == "__main__":

    main(banner)
