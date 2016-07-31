from datetime import datetime
import runClass
import os

"""
Program Name: Run Logger

Created By: Thomas Osgood
Date Created: 2015 07 20

Purpose:
    - Keep Track Of Running:
        Times
        Distances
        Frequency

Customization:
    - Custom Class 'runClass'
"""

# GLOBAL Var(s)
logName = "runningLog.txt"

# Method Used To Insert A New Run
# Into The Running Log
def AddRun():
    """
    Method Used To Insert A New Run
    Into The Running Log.

    Calls runClass Custom Class.

    Creates "RUN" Object
    """

    global logName

    newrun = runClass.run()
    newrun.getDistance()
    newrun.getTime()
    newrun.calcSpeed()
    newrun.saveInDB(logName)

    return

# Method To Show User The
# Entire Running Log.
# Prints Log To "STDOUT"
def ShowLog():
    """
    Method To Show User The Entire Running Log.
    
    Prints Log To STDOUT
    """

    global logName

    if (os.path.isfile(logName)):
        logFile = open(logName, "r")
        data = logFile.read()
        logFile.close()
        print "\n\t:: Running Log ::\n{0}".format(data)
        print "\n"
    else:
        print "\nNo Running Log On Record\n"

    raw_input("Press Enter To Continue")

    return

# Method To Print Out Running Log
# Uses Default Printer
def PrintLog():
    """ 
    Method To Print The Running Log.
    
    Prints Using Default Printer.

    Note:
    Has Only Been Tested On Windows.
    """
    global logName

    if (os.path.isfile(logName)):
        os.startfile(logName,"print")
    else:
        print "\n\tRun Log Not Found\n"


    return

# Main Method For Program
def Main():
    """
    Main Program Method.

    Gets User Input And Calls The Correct Methods.
    Will Continuously Loop Until The User Enters Q.

    Acts Like A Dispatcher.
    """

    optStr = "\nOptions\n\t1 : Add Run\n\t2 : View Runs\n\t3 : Print Run Log\n\tQ : Exit"
    while True:
        print "{0}\n".format(optStr)
        sel = raw_input("\nSelection:\n-> ")
        if str(sel).upper() == "Q":
            break
        elif sel == "1":
            AddRun()
        elif sel == "2":
            ShowLog()
        elif sel == "3":
            PrintLog()
        else:
            print "\n\tInvalid Selection"

    return

# Conditional To Call MAIN Method
if __name__ == "__main__":
    print "Welcome To Tom's Run Logger"
    Main()
    raw_input("\nPress Enter To Exit")
