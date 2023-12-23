fo = open("/root/.aws/credentials", "r")
str = fo.read(100)
print ("Read String is : " + str)
fo.close()