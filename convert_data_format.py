#read data file
# They are score for the rectification process.  There are
#five features used (right eye, left eye, nose, right corner of mouth,
#left corner of mouth).

readin = open('train.txt', 'r')
#write data file
output = open('libsvm_train.txt', 'w')
try:
    the_line = readin.readline()
    while the_line:
        # delete the \n
        the_line = the_line.strip('\n')
        index = 0;
        output_line = ''
        for sub_line in the_line.split('\t'):
                # 1 means male and 0 means female
            if index == 0:
                output_line=str(1)+' '+str(0)+':'+sub_line

            if sub_line != 'NULL' and index != 0:
                the_text = ' ' + str(index) + ':' + sub_line
                output_line = output_line + the_text
            index = index + 1
        output_line = output_line + '\n'
        output.write(output_line)
        the_line = readin.readline()
finally:
    readin.close()
