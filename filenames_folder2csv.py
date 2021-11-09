import os, csv

# f = open('path/text.csv', mode = 'r, w, r+, a') 
# r : only read
# w : only write (an existing file with the same name will be erased)
# r+ : both read and write
# a : write at the end of file (an existing file with the same name will not be erased)
f=open("path/file.csv",'r+', newline = '')
w=csv.writer(f)
for path, dirs, files in os.walk("path/folder"):
    for filename in files:
        w.writerow([filename])
print("...Done")