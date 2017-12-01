# Enter script code
import time
import re
shortdelay = 0.2

current = window.get_active_title()

if re.search(r"Atom", current) and re.search(r"^[\w\-\. ]+\.(a)?do", current):
    window.activate("Stata/")
    if window.wait_for_focus("Stata/(IC|SE|MP) 1[1-5].[0-2]", timeOut = 1):
    
        cmd = clipboard.get_selection()
    
        if re.search(r"(//|///|/\*(.*?)\*/)", cmd, flags=re.DOTALL):
            # There are commands in that chunk of code that
            #  are unreadable in Stata console
            # Try to adjust those commands to not have comments:
            
            # If ///, delete spaces and the \n
            # If //, delete spaces and text up to but not including the \n
            # If /*, delete everthing until */
            
            cmd = re.sub(r"\s*(///).*\n\s*", " ", cmd)
            cmd = re.sub(r"\s*//.*\n", " \n", cmd)
            cmd = re.sub(r"/\*(.*?)\*/", " ", cmd, flags=re.DOTALL)
            cmd = re.sub(r"[\t ]+", " ", cmd)

        time.sleep(shortdelay)
        keyboard.send_keys(cmd)
        keyboard.send_keys("<enter>")
    
        time.sleep(shortdelay)
        window.activate(current)
        keyboard.send_keys("<escape>")
else:
    keyboard.send_keys("<ctrl>+r")
