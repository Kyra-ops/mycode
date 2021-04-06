# parse keystone.common.wsgi and return number of successful login attempts
loginsuccess = 0 # counter for success

# open the file for reading
keystone_file = open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r")

# loop over the file
for line in keystone_file:

    # if this 'success pattern' appears in the line...
    if "-] Authorization failed" or "- - - - -] Loaded 2" in line:
        loginsuccess += 1 # this is the same as loginsuccess = loginsuccess + 1

print("The number of successful log in attempts is", loginsuccess)
keystone_file.close() # close the open file
