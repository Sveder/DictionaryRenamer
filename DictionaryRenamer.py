#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#                               Dictionary Renamer                             #
#                             ----------------------                           #
#                                                                              #
#   Author:                                                                    #
#           Michael Sverdlin                                                   #
#   Date:                                                                      #
#           11.07                                                              #
#   Purpose:                                                                   #
#           Rename files from a dictionay.                                     #
#                                                                              # 
#   TODO:                                                                      #
#                                                                              #
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
#------------------------------IMPORTS-----------------------------------------#

import os
import sys
import shutil

#------------------------------GLOBALS-----------------------------------------#

#------------------------------CLASSES-----------------------------------------#

#------------------------------FUNCTIONS---------------------------------------#

def new_name(dic, file):
    for i in dic.keys():
        #print i
        file = file.replace(i, dic[i])
    return file

#------------------------------MAIN--------------------------------------------#

def main():
    try:
        try:
            dictionary_file = sys.argv[1]
            base_dir = sys.argv[2]
        except Exception, error:
            print "USAGE: %s dictionary_file dir_to_rename" % (os.path.basename(sys.argv[0]))
            os.exit(0)
        
        dic = {}
        txt = open(dictionary_file).read()
        txt = txt.split("\n")
        txt[0] = txt[0]
        
        for line in txt:
            src, dst = line.split("->")
            dic[src.replace("\xef\xbb\xbf", '').decode("utf-8")] = dst.decode("utf-8")
        
        for base, dirs, files in os.walk(unicode(base_dir)):
            for file in files:
                new_file = new_name(dic, file)
                #print new_file
                os.rename(os.path.join(base, file), os.path.join(base, new_file))
    
    
    except Exception, error:
        print "Program failed, here's a detailed explanation:"
        import traceback
        print traceback.print_exc()




if "__main__" == __name__:
    #Remove the python CL arg, cause it sucks...
    if "python" in sys.argv[0]:
        sys.argv = sys.argv[1:]
    main()