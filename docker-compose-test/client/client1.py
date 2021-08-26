import os
import shutil
import time
#time.sleep(20)
#os.system("ls -a /client/")
#shutil.copyfile("/client/data.sql", "/datavolume1/data.sql")
os.system("mysql -h mysql_server -u root -pCat_1234 < /datavolume1/data.sql")
#os.system("docker exec mysql_server mysql -u root -pCat_1234 < /datavolume1/data.sql")
#os.system("ls -a /")
#os.system("echo abcdef")
#os.system("sudo -V")
#print("hello world")
