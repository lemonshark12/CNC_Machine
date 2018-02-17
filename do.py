from sys import argv
import re

script, data_file = argv


#def read_file(data_file):
#    print data_file.read()
    
#def data_start(data_file):
#    data_file.seek(0)


#def print_data_line(data_line, data_file):
 #   print data_line, data_file.readline()

    
def run():
    find_data_start()
    
data = open(data_file, 'a')

#with open(data,'r') as f:
 #   read_data_file = f.readlines()

#initial parameters
a = "Y"
data_line = 25
coordinate_start = 'MS' #this is 

def print_lines(data_line, f):
    print data_line, f.readline()

def find_data_start():
    """Provides starting line of G-Code txt file where actual coordinates begin"""
    
    with data as f:
        for i, line in enumerate(f):
            if coordinate_start in line:

                print i+1, line
           # if i == 4:
            #    f.writelines("Fuck yeah!")
            #else:
                f.writelines(line)
                #f.seek(int(line))
                #print_lines (data_line, line)
                #for num in range(20):
                #print data_line, f.readline(30) 
                

                
#for data in range(20):
 #   data.print line
  #  line += 1
            

# index won't work for files, only tuples
#print (data.index('2.350049'))


    
    
#print_data_line = do (x, y, z)


run()