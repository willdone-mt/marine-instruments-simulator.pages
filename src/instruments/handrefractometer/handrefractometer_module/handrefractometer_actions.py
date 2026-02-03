'''

'''
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))

from generators import clocked
from generators import value_generator

# global variables, as they were a real not used instrument yet
closedLid = True  
calibrated = False
wiped = False
sampled = False
pointed = 0
peeking = False
value = 0

# Actions
def open_lid():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    if closedLid == False:
        print(f"closedLid:{closedLid}")
        message = "Lid is already opened"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    else:
        closedLid = False
        print(f"closedLid:{closedLid}")
        message = "Lid is opened"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message

def close_lid():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    if closedLid == True:
        peeking = False
        print(f"closedLid:{closedLid}")
        message = "Lid is already closed"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    else:
        closedLid = True
        peeking = False
        print(f"closedLid:{closedLid}")
        message = "Lid is closed"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message

def calibrate():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    if closedLid == True:
        peeking = False
        print(f"closedLid:{closedLid}")
        message = "Lid is still closed"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    else:
        calibrated = True
        wiped = False
        peeking = False
        value = 0
        print(f"calibrated:{calibrated}, wiped:{wiped}")
        message = "Instrument calibrated successfully!\nValue should be back to zero (0)"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message

def wipe():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    if closedLid == True:
        peeking = False
        message = "Lid is still closed"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    else:
        wiped = True
        peeking = False
        print(f"wiped:{wiped}")
        message = "Lens wiped!"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message

def sample():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    if calibrated == False:
        peeking = False
        print(f"calibrated:{calibrated}")
        message = "Calibrate first!"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    elif wiped == False:
        peeking = False
        print(f"wiped:{wiped}")
        message = "Wipe the lens first!"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    else:
        sampled = True
        wiped = False
        calibrated = False
        peeking = False
        value = value_generator.random_value()
        print(f"sampled:{sampled}, wiped:{wiped}, calibrated:{calibrated}")
        message = "Water sampled!"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message

def point_to_lightsource():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    pointed = 10
    for remaining in clocked.countdown_timer(15):
        pointed = (remaining / 15) * 10   # scale to 10
        print(f"pointed:{pointed}")
        yield pointed   # yield outward
    message = "EMPTY"
    return closedLid, calibrated, wiped, sampled, peeking, pointed, value, message

def peek():
    global closedLid, calibrated, wiped, sampled, pointed, peeking, value
    if closedLid == False:
        peeking = True
        print(f"closedLid:{closedLid}")
        message = "Lid is still opened"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    if pointed > 1:
        if sampled == False and calibrated == True:
            peeking = True
            print(f"sampled:{sampled}")
            value = 0
            message = f"Value: {value}"
            print(message)
            return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
        if sampled == True:
            peeking = True
            print(f"sampled:{sampled}")
            value = value
            message = f"Value: {value}"
            print(message)
            return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
        elif pointed <= 1:
            peeking = True
            print(f"pointed={pointed}")
            message = "point to a light source first"
            print(message)
            return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message
    else:
        peeking = True
        message = "Something Wronnk"
        print(message)
        return closedLid, calibrated, wiped, sampled, pointed, peeking, value, message

def test_run():
    print("command_defintion is running")