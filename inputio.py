s = "Harry is a good boy"

# to open a new file use open function.w denotes write function in it.
# with open("test.txt", "w") as f:
#   f.write(s)
# here we are opening text file with write permissions and writing string s into it and then closing it
# fp = open("text.txt","w")
# fp.write(s)

# fp.close()

# to read a given file

# with open("text.txt","r") as f:
#   t = f.read()
#   print(t)

with open("text.txt","a") as f:
    f.write("you are very nice")
    

