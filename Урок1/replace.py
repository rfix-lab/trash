import re
import os
path = "replace"
fileList = os.listdir(path)
for file in fileList:
    with open (os.path.join('replace/'+file),'r') as f:
        for line in f:
            for part in line.split('$'):
                with open ('out_'+file,'a') as k:
                    if "Temperature=" in part:
                        dig=int(re.search(r'\d+', part).group(0))
                        my_dig=int(dig)-400
                        k.write('crs:Temperature="'+str(my_dig)+'"'+'\n')
                    else:
                        k.write(part)