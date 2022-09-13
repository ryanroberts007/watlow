import watlow
import sys, getopt

def main(argv):
    setpoint = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["setpoint="])
    except getopt.GetoptError:
        print('test.py -s <setpoint_value>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--setpoint"):
            setpoint = arg
    print('Input arg is ', setpoint)

    if (setpoint != ''):
        tc = watlow.TemperatureController('/dev/ttyUSB0')
        try:
            try:
                tc.set(setpoint)
            except IOError as e:
                print(e)
        except KeyboardInterrupt:
            pass
        finally:
            tc.close()

if __name__ == "__main__":
   main(sys.argv[1:])