import os
import subprocess
import paragraph as para
import sys

target = ''
if sys.argv[1] == 1:
	print "FOUND A ONE"
	target = '../target1.html'
else:
	print "FOUND A TWO"
	target = '../target2.html'

#command = "python paragraph.py . ./p1.txt 4"
#black magic to fetch stdout
#output = subprocess.Popen(command, close_fds=True, shell=True, stdout=subprocess.PIPE).communicate()[0]
quote1, nil = para.genCopy('../', "../quote1.txt")
quote2, nil = para.genCopy('../', "../quote2.txt")
quote3, nil = para.genCopy('../', "../quote1.txt")
#copy, name = para.genCopy(os.getcwd(), os.getcwd() + "/p1.txt")

#TODO change one to
os.system('cp ../template1.html ../target1.html')
os.system('cp ../template1.html ../target2.html')

#qqqqq for copy
command1 = 'sed -i s/qqqqq/' + '\"' + quote1 + '\"' + '/g ' + target

#rrrrr for name
command2 = 'sed -i s/rrrrr/' + '\"' + quote2 + '\"' + '/g ' + target

#sssss for something
command3 = 'sed -i s/sssss/' + '\"' + quote3 + '\"' + '/g ' + target

#ccccc for something else
#command = 'sed -i s/nnnnn/' + '\"' + output[0] + '\"' + '/g ' + target

os.system(command1)
os.system(command2)
os.system(command3)
#print output[0]
#print output[1]
