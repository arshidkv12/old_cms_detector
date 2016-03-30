import os
import pprint

print "-------------------------------------------------"
print "-------------------------------------------------"
print "--------- WordPress Current Version ------------"
print "-------------------------------------------------"
print "-------------------- 4.4.2 ----------------------"
print "-------------------------------------------------"
print "----------------- STARTED -----------------------"

# Author: Arshid 
# www.cipherCoin.com
#email: arshidkv12@gmail.com
#

file_name = open("oldCMS.txt", "a")

for dirname, dirnames, filenames in os.walk('.'):

    for subdirname in dirnames:

        if "wp-include" in subdirname:

            path = os.path.join(dirname, subdirname)+"/version.php"
            for line in open(path) :
                if "wp_version =" in line:
                    i = line.strip("$wp_version = '")
                    tmp_var_k = i.replace("';",'')
                    k = tmp_var_k.replace('\n','')
                    k = k.replace('.','')
                   
                    j = float(k)
                    if j < 442:
                        file_name.write("Old version:"+ tmp_var_k+"\n" + path + "\n"+ "\n")
                        print "Old version:"+ tmp_var_k+"\n" + path + "\n"+ "\n"


print "--------- COMPLETED ------------"
                     
                    
                         
                    
