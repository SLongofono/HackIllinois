import os
import subprocess
import paragraph as para

#command = "python paragraph.py . ./p1.txt 4"
#black magic to fetch stdout
#output = subprocess.Popen(command, close_fds=True, shell=True, stdout=subprocess.PIPE).communicate()[0]

copy, name = para.genCopy(os.getcwd(), os.getcwd() + "/p1.txt")
os.system('cp template.html index.html')
print copy, name
#qqqqq for copy
command1 = 'sed -i s/qqqqq/' + '\"' + copy + '\"' + '/g index.html'

#nnnnn for name
command2 = 'sed -i s/nnnnn/' + '\"' + name + '\"' + '/g index.html'

#bbbbb for something
#command = 'sed -i s/nnnnn/' + '\"' + output[0] + '\"' + '/g index.html'

#ccccc for something else
#command = 'sed -i s/nnnnn/' + '\"' + output[0] + '\"' + '/g index.html'

os.system(command1)
os.system(command2)
#print output[0]
#print output[1]
