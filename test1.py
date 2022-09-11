from time import sleep
import watlow

tc = watlow.TemperatureController('/dev/ttyUSB0')
try:
    while True:
        try:
            print(tc.get())
        except IOError as e:
            print('disconnected')
            print(e)
        sleep(1)
except KeyboardInterrupt:
    pass
finally:
    tc.close()
