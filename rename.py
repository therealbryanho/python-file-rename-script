# Python 3 code to rename multiple
# files in a directory or folder
 
# importing os module
import os
 
# Function to rename multiple files 
def main():
    #src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
    folder = "number" #assuming the files are in a folder called number
    for count, filename in enumerate(os.listdir(folder)):
        #scenario - change ".png" to "_99.png"
        #filename[:-4] means to take the last 4 chars from the filename
        
        newfilename = filename[:-4] + "_99.png"

        src =f"{folder}/{filename}"
        dst = f"{folder}/{newfilename}"
        #print(newfilename)
        # rename() function will
        # rename all the files
        os.rename(src, dst)
     
    # Calling main() function
main()
