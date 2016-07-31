from datetime import datetime

class run:
    """
    Created By: Thomas Osgood
    Date Created: 2015 07 20

    Purpose:
        Creates A Run Object
            - Contains:
                Distance
                Time
                Speed
            - Writes To Specified Logfile
    """
    def __init__(self):
        self.dist = "0"
        self.hr = "00"
        self.min = "00"
        self.sec = "00"
        self.tottime = "{0}:{1}:{2}".format(self.hr,self.min,self.sec)
        self.speed = "00:00"
        self.speedTen = 0.0
        self.today = True

    # Method To Get Run Distance
    def getDistance(self):
        """
        Gets Run Distance From User.

        Distance Is Asked For In Miles
        """

        self.dist = float(raw_input("\nDistance Run [miles] : "))
        
        return

    # Method To Get Run Time From User
    # And Assign It To Object Vars
    def getTime(self):
        """
        Gets How Fast The User Did The Run In.

        Acquires:
            - hours
            - minutes
            - seconds

        Formats The Total Time Variable [HH:MM:SS]
        """

        self.hr = int(raw_input("Hours : "))
        self.min = int(raw_input("Minutes : "))
        self.sec = int(raw_input("Seconds : "))
        self.tottime = "{0:02d}:{1:02d}:{2:02d}".format(self.hr,self.min,self.sec)
        print "\n"
        
        return

    # Method To Calculate Run Speed After
    # Getting Run Times
    def calcSpeed(self):
        """
        Calculates The Speed Of The Run.

        Results Are In Both X.XX Format & MM:SS Format
        """
        
        # Calculate Total Time In Min & Secs Run Took
        min = self.min + (self.hr * 60)
        dec = float(self.sec / 60.0)
        total = float(min + dec)

        # Calculate Speed Min.DecimalVal
        self.speedTen = total / self.dist
        
        # Split X.XX Into Min and Decimal (ie: [Min,Decimal])
        strSpeedTen = str(self.speedTen).split(".")
        
        # Get Minute Value
        min = strSpeedTen[0]
        
        # Prepare Decimal Value For Conversion
        sec = float(".{0}".format(strSpeedTen[1]))

        # Convert Decimal Val To Secs
        sec1 = int(float(sec)*60)

        # Put It All Together
        self.speed = " {0} : {1:02d}".format(min,sec1)

        return

    # Method To Save Relevant Data To 
    # Running Log Specified By User
    def saveInDB(self,filename):

        """
        Saves The Run Information In A Specified Database

        Appends The Information To End Of The File.

        If The File Does Not Already Exist, A New File Is Created

        Call :: object.saveInDB(filename)
        """

        dateNow = datetime.now().date()
        now = "Run :: {0}".format(dateNow)
        d = "Distance [miles]: {0}".format(self.dist)
        tot = "Ran In:  {0}".format(self.tottime)
        s = "\tSpeed: {0}".format(self.speed)
        sten = "\tRan: {0}".format(self.speedTen)
        file = open(filename,"a")
        file.write(("\n{0}\n{1}\n{2}\n{3}\n{4}\n").format(now,d,tot,s,sten))
        file.close()

        return


