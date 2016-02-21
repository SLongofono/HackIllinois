import os
import subprocess
import paragraph as para

#command = "python paragraph.py . ./p1.txt 4"
#black magic to fetch stdout
#output = subprocess.Popen(command, close_fds=True, shell=True, stdout=subprocess.PIPE).communicate()[0]

quote1, nil = para.genCopy(os.getcwd(), os.getcwd() + "/quote1.txt")
quote2, nil = para.genCopy(os.getcwd(), os.getcwd() + "/quote2.txt")
quote3, nil = para.genCopy(os.getcwd(), os.getcwd() + "/quote1.txt")
#copy, name = para.genCopy(os.getcwd(), os.getcwd() + "/p1.txt")

os.system('cp template1.html index.html')

#qqqqq for copy
command1 = 'sed -i s/qqqqq/' + '\"' + quote1 + '\"' + '/g index.html'

#rrrrr for name
command2 = 'sed -i s/rrrrr/' + '\"' + quote2 + '\"' + '/g index.html'

#sssss for something
command3 = 'sed -i s/sssss/' + '\"' + quote3 + '\"' + '/g index.html'

#ccccc for something else
#command = 'sed -i s/nnnnn/' + '\"' + output[0] + '\"' + '/g index.html'

os.system(command1)
os.system(command2)
os.system(command3)
#print output[0]
#print output[1]
