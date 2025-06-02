# copyfile():copies content of a file
# copy():copyfile()+permission mode + destination can be a directory
# copy2(): copy() + copies metadata (files creation and modification times)

import shutil

shutil.copyfile("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt","copy.txt") #ensure source and destination you have

shutil.copy("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt","copy2.doc") #ensure source and destination you have

shutil.copyfile("C:\\Users\\Admin\\OneDrive\\Desktop\\write.txt","copy.html") #ensure source and destination you have

