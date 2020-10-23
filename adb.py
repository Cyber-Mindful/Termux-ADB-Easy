import os, time
os.system('clear')
print '\033[32m install adb or uninstall adb\n'
print '\033[33m  By Ahmed Nassif\n\n'
print '\033[32m [1] install ADB'
print '\033[32m [2] uninstall ADB'
print ' [3] exit\n'
a = input('\033[32m# Enter number: ')
if a == 1:
 print '\033[33m'
 os.system('apt update && apt install wget && wget https://github.com/MasterDevX/Termux-ADB/raw/master/InstallTools.sh && bash InstallTools.sh')
 print '\033[0m'
elif a == 2:
 print '\033[33m'
 os.system('apt update > /dev/null 2>&1 && apt --assume-yes install wget > /dev/null 2>&1 && wget https://github.com/MasterDevX/Termux-ADB/raw/master/RemoveTools.sh -q && bash RemoveTools.sh')
 print '\033[0m'
elif a == 3:
 os.system('clear')
 print '\033[1;33m GoodBye\033[0m\n'
 os.system('exit')
else:
 print '\033[31m Erorr in inpot\n'
 time.sleep(1)
 os.system('python2 adb.py')
