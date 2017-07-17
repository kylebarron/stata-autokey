# Enter script code
import time
import re
shortdelay = 0.2
shorterdelay = 0.1

current = window.get_active_title()

if re.search(r"Atom", current) and re.search(r"^[\w\-\. ]+\.do", current):
    window.activate("Stata/")

    cmd = clipboard.get_selection()

    if re.search(r"(//|///|/\*.*\*/)", cmd):
        
        time.sleep(shortdelay)
        # Open up a new do-file editor
        keyboard.send_keys("<ctrl>+9")
        time.sleep(shortdelay)
        # Paste text
        keyboard.send_keys(cmd)
        time.sleep(shortdelay)
        # Run the file
        keyboard.send_keys("<ctrl>+d")
        # Undo the paste
        time.sleep(shortdelay)
        keyboard.send_keys("<ctrl>+z")
        # Close the do-file editor
        time.sleep(shortdelay)
        keyboard.send_keys("<ctrl>+w")
        # # Don't save changes
        # keyboard.send_keys("<left>")
        # time.sleep(shorterdelay)
        # keyboard.send_keys("<left>")
        # time.sleep(shorterdelay)
        # keyboard.send_keys("<enter>")
        # time.sleep(shorterdelay)
        time.sleep(shortdelay)
        window.close("Do-file Editor:")

        time.sleep(shortdelay)
        window.activate(current)
        # keyboard.send_keys("<escape>")

    else:
        time.sleep(shortdelay)
        keyboard.send_keys(cmd)
        keyboard.send_keys("<enter>")

        time.sleep(shortdelay)
        window.activate(current)
        keyboard.send_keys("<escape>")

else:
    keyboard.send_keys("<ctrl>+r")



# cmd = clipboard.get_selection()
#
# time.sleep(shortdelay)
# keyboard.send_keys(cmd)
# keyboard.send_keys("<enter>")
#
# time.sleep(shortdelay)
# window.activate(current)
# keyboard.send_keys("<escape>")
#


#Stiuplations
# only go through dofile editor when necessary (///)
# make new dofile editor with ctrl-9



# If ///, the delete spaces and the \n
# If //, delete spaces and text up to but not including the \n
# If /*, delete everthing until */







# if re.search(r"Atom", current) and re.search(r"^[\w\-\. ]+\.do", current):
#     window.activate("Stata")
#
#     cmd = clipboard.get_selection()
#
#     if re.search(r"(//|///|/\*.*\*/)", cmd):
#         time.sleep(shortdelay)
#         # Open up a new do-file editor
#         keyboard.send_keys("<ctrl>+9")
#         time.sleep(shortdelay)
#         # Paste text
#         keyboard.send_keys(cmd)
#         time.sleep(shortdelay)
#         # Run the file
#         keyboard.send_keys("<ctrl>+d")
#         # Undo the paste
#         time.sleep(shortdelay)
#         keyboard.send_keys("<ctrl>+z")
#         # Close the do-file editor
#         time.sleep(shortdelay)
#         keyboard.send_keys("<ctrl>+w")
#         # # Don't save changes
#         # keyboard.send_keys("<left>")
#         # time.sleep(shorterdelay)
#         # keyboard.send_keys("<left>")
#         # time.sleep(shorterdelay)
#         # keyboard.send_keys("<enter>")
#         # time.sleep(shorterdelay)
#         time.sleep(shortdelay)
#         window.close("Do-file Editor:")
#
#         time.sleep(shortdelay)
#         window.activate(current)
#         # keyboard.send_keys("<escape>")
#
#     else:
#         time.sleep(shortdelay)
#         keyboard.send_keys(cmd)
#         keyboard.send_keys("<enter>")
#
#         time.sleep(shortdelay)
#         window.activate(current)
#         keyboard.send_keys("<escape>")
#
# else:
#     keyboard.send_keys("<ctrl>+r")
