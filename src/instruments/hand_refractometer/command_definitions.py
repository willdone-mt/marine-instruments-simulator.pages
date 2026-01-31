'''

'''
import value_generator as vg

# global variables, as they were a real not used instrument yet
closedLid = True  
calibrated = False
wiped = False
sampled = False
value = 0

# Actions
def open_lid():
    global closedLid
    if closedLid == False:
        print(f"closedLid:{closedLid}")
        message = "Lid is already opened"
        print(message)
        return message, closedLid
    else:
        closedLid = False
        print(f"closedLid:{closedLid}")
        message = "Lid is opened"
        print(message)
        return message, closedLid 

def close_lid():
    global closedLid
    if closedLid == True:
        print(f"closedLid:{closedLid}")
        message = "Lid is already closed"
        print(message)
        return message, closedLid
    else:
        closedLid = True
        print(f"closedLid:{closedLid}")
        message = "Lid is closed"
        print(message)
        return message, closedLid

def calibrate():
    global closedLid
    global calibrated
    global wiped
    global value
    if closedLid == True:
        print(f"closedLid:{closedLid}")
        message = "Lid is still closed"
        print(message)
        return message, closedLid, calibrated, wiped
    else:
        calibrated = True
        wiped = False
        value = 0
        print(f"calibrated:{calibrated}, wiped:{wiped}")
        message = "Instrument calibrated successfully!\nValue should be back to zero (0)"
        print(message)
        return message, closedLid, calibrated, wiped

def wipe():
    global closedLid
    global wiped
    if closedLid == True:
        message = "Lid is still closed"
        print(message)
        return message
    else:
        wiped = True
        print(f"wiped:{wiped}")
        message = "Lens wiped!"
        print(message)
        return message

def sample():
    global calibrated
    global sampled
    global wiped
    global value
    if calibrated == False:
        print(f"calibrated:{calibrated}")
        message = "Calibrate first!"
        print(message)
        return message
    elif wiped == False:
        print(f"wiped:{wiped}")
        message = "Wipe the lens first!"
        print(message)
        return message
    else:
        sampled = True
        wiped = False
        calibrated = False
        value = vg.random_value()
        print(f"sampled:{sampled}, wiped:{wiped}, calibrated:{calibrated}")
        message = "Water sampled!"
        print(message)
        return message

def peek():
    global closedLid
    global sampled
    global calibrated
    global value
    if closedLid == False:
        print(f"closedLid:{closedLid}")
        message = "Lid is still opened"
        print(message)
        return message, value
    if sampled == False and calibrated == True:
        print(f"sampled:{sampled}")
        value = 0
        message = f"Value: {value}"
        print(message)
        return message, value
    if sampled == True:
        print(f"sampled:{sampled}")
        value = value
        message = f"Value: {value}"
        print(message)
        return message, value
    else:
        message = "Sample first!"
        print(message)
        return message, value

def status():
    return closedLid, calibrated, wiped, sampled