import watlow

tc = watlow.TemperatureController('/dev/ttyUSB0')
try:
    try:
        print(tc.get())
    except IOError as e:
        print(e)
except KeyboardInterrupt:
    pass
finally:
    tc.close()