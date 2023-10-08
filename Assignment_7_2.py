# Use the file name mbox-short.txt as the file name
#fname = input("Enter file name: ")
import os

def read_file(file_name):
    file_handle = open(file_name)
#    print file_handle.read()
    file_handle.close()

file_dir = os.path.dirname(os.path.realpath('__file__'))
print(file_dir)

#For accessing the file in the same folder
file_name = "mbox-short.txt.rtf"
read_file(file_name)

for line in file_name:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    line = line.rstrip()
    confidence = str(line.find(":    0"))
    number = confidence[19:]
    print(line)
print("Done")
