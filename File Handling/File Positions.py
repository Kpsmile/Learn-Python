fo = open("foo.txt", "r+")
str = fo.read();
print "Read String is : ", str

# Check current position
position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(1, 1);
str = fo.read(10);
print "Again read String is : ", str
# Close opend file
fo.close()