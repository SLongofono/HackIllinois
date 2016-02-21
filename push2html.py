import os
import subprocess
import paragraph as para
import sys

target = ''
if sys.argv[1] == 1:
	print "FOUND A ONE"
	target = 'target1.html'
else:
	print "FOUND A TWO"
	target = 'target2.html'

#command = "python paragraph.py . ./p1.txt 4"
#output = subprocess.Popen(command, close_fds=True, shell=True, stdout=subprocess.PIPE).communicate()[0]
quote1, nil = para.genCopy(os.getcwd(), os.getcwd() + "quote1.txt")
quote2, nil = para.genCopy(os.getcwd(), os.getcwd()+"quote2.txt")
quote3, nil = para.genCopy(os.getcwd(), os.getcwd() +"../quote1.txt")
body, nil = para.genCopy(os.getcwd(), os.getcwd() + "/b1.txt")
copy, name = para.genCopy(os.getcwd(), os.getcwd() + "/p1.txt")

os.system('cp template1.html target1.html')
os.system('cp template2.html target2.html')

#aaaaa for about
command1 = 'sed -i s/aaaaa/' + '\"' + copy + '\"' + '/g ' + target

#bbbbb for body
command2 = 'sed -i s/bbbbb/' + '\"' + body + '\"' + '/g ' + target

#ttttt for name
command3 = 'sed -i s/ttttt/' + '\"' + name + '\"' + '/g ' + target

#rrrrr for quote1
command4 = 'sed -i s/rrrrr/' + '\"' + quote1 + '\"' + '/g ' + target

#sssss for quote2
command5 = 'sed -i s/sssss/' + '\"' + quote2 + '\"' + '/g ' + target

#uuuuu for quote3
command4 = 'sed -i s/uuuuu/' + '\"' + qoute3 + '\"' + '/g ' + target


os.system(command1)
os.system(command2)
os.system(command3)
os.system(command4)
os.system(command5)
