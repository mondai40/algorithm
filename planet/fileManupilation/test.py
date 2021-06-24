# open file, you need to create file object to manupilate it
fileObj = open("./test.txt", "a")


# read file open()'s mode shoud be r, r+, rb, r+
# *** you can't use read() multiple times because the pointer move to the eof and return nothing***
# return whole file content
# print(fileObj.read())
print("===============================")
# return a specfied bytes
# print(fileObj.read(5))
print("===============================")
# return a single line
# print(fileObj.readline())

# write file open()'s mode should be w, w+, wb, wb+, r+, rb+, a, a+, ab, ab+

# w, w+, wb, wb+, r+, rb+,
# *** pointer will move to start of file, so all the previous content will be overwritten ***
fileObj.write("goodbye world")

# a, a+, ab, ab+
# *** pointer will start at the eof, so all the previous content will not be overwritten ***
fileObj.write("It's Wednesday")

# close file
fileObj.close()