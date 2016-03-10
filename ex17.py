from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file) 
indata = in_file.read()

#The above can be done in a single line as:-
#indata = open(from_file).read()
#Do not add the close() function here

print "The input file is %d bytes long" % len(indata)
#Length of the file in bytes

print "Does the output file exist? %r" % exists(to_file)
#This would give out a TRUE/FALSE value
 
print "Ready, hit RETURN to continue, CTRL-C to abort." 
raw_input('?')

out_file = open(to_file, 'w') 
out_file.write(indata)

print "Alright, all done."
out_file.close() 
in_file.close()