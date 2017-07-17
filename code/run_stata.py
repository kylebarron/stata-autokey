# Enter script code
import time
shortdelay = 0.05

current = window.get_active_title()

if re.search(r"Atom", current) and re.search(r"^[\w\-\. ]+\.do", current):
    keyboard.send_keys("<ctrl>+l")
    window.activate("Stata/")

    cmd = clipboard.get_selection()
    orig_cmd = cmd
    
    # There may be elements of code that are unreadable in Stata console
    # Try to adjust those commands to not have comments:
    
    # If ///, paste but do not run everything before ///
    # If //, paste everything before // and then also run
    # If /*, delete everthing until */ and then also run
        # It's hard to deal with multi-line comments when running line-by-line

    if re.search(r"///", cmd):
        cmd = re.sub(r"\s*(///).*\n\s*", " ", cmd)
        cmd = re.sub(r"[\t ]+", " ", cmd)
        time.sleep(shortdelay)

    if re.search(r"//",  cmd):
        cmd = re.sub(r"\s*//.*\n", " \n", cmd)
        cmd = re.sub(r"[\t ]+", " ", cmd)
        time.sleep(shortdelay)

    if re.search(r"/\*.*?\*/", cmd):
        cmd = re.sub(r"/\*.*\*/", " ", cmd)
        cmd = re.sub(r"[\t ]+", " ", cmd)
        time.sleep(shortdelay)
        
    if re.search(r"///", orig_cmd):
        time.sleep(shortdelay)
        keyboard.send_keys(cmd)
    else:
        time.sleep(shortdelay)
        keyboard.send_keys(cmd)
        keyboard.send_keys("<enter>")
    
    time.sleep(shortdelay)
    window.activate(current)

    keyboard.send_keys("<down>")
    keyboard.send_keys("<up>")

else:
    keyboard.send_keys("<ctrl>+r")
