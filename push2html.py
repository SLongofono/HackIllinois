import os
import subprocess
import paragraph as para

#command = "python paragraph.py . ./p1.txt 4"
#black magic to fetch stdout
#output = subprocess.Popen(command, close_fds=True, shell=True, stdout=subprocess.PIPE).communicate()[0]

output = para.genCopy(os.getcwd(), os.getcwd() + "/p1.txt", 4)
os.system('cp template.html index.html')
command = 'sed -i s/qqqqq/' + '\"' + output[0] + '\"' + '/g index.html'
os.system(command)

#print output[0]
#print output[1]
