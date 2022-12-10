import os
import mysql.connector
import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD  
GPIO.setup(24, GPIO.OUT)           # set GPIO24 as an output
gpio23 = GPIO.setup(23, GPIO.IN)           # set GPIO24 as an output

#SELECT (VAR1) FROM `test_pi` WHERE (NAME)='GIMLI'
#UPDATE `test_pi` SET `VAR2`=1 WHERE (NAME)='GIMLI'

state = 2
gpiostate = 2

GPIO.add_event_detect(23, GPIO.BOTH, bouncetime=100)

while True:
    try:
        mydb = mysql.connector.connect(
                host="94.73.151.62",
                user="u9737940_r_pi_4",
                database="u9737940_pi4",
                password="TZaq04G4HKdl53G"
        )
            
        if (mydb):
            # Carry out normal procedure
            print ('Connection successful')
            break
        else:
            # Terminate
            print ('Connection unsuccessful')
            mydb = mysql.connector.connect(
                host="94.73.151.62",
                user="u9737940_r_pi_4",
                database="u9737940_pi4",
                password="TZaq04G4HKdl53G"
            )
            
    except Exception as e:
#        os.system('clear')
        sleep(1)
        print(e)

db_cursor = mydb.cursor()

while True:
    try:
        
        db_cursor.execute("SELECT (VAR1) FROM `test_pi` WHERE (NAME)='GIMLI'")
        
#        os.system('clear')
        
        for db in db_cursor:
            if not state == db[0]:
                if db[0] == 1:
                    GPIO.output(24, 1)         # set GPIO24 to 1/GPIO.HIGH/True 
                    print ('LED just about to switch on')
                elif db[0] == 0:
                    GPIO.output(24, 0)         # set GPIO24 to 0/GPIO.LOW/False 
                    print ('LED just about to switch off')
            state = db[0]
            
        if GPIO.event_detected(23):
            print ('TEST')
            if GPIO.input(23):
                print ('TEST1')
                db_cursor.execute("INSERT INTO `industry4`(`START_TIME`, `STOP_TIME`) VALUES (NOW(),0)")
            elif GPIO.input(23) == 0:
                print ('TEST2')
                db_cursor.execute("UPDATE `industry4` SET `STOP_TIME`=NOW(), `MIN_SUM`=TIMESTAMPDIFF(MINUTE,`START_TIME`,NOW()) WHERE (STOP_TIME)=0")
            
    except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
        GPIO.cleanup()    