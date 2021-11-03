def run_serial(self, com):
    # BLOQUE SERIAL
    global ser
    ser = serial
    try:
        ser = serial.Serial(com, 115200, timeout=1)  # ojito con la ruta
        # ser = serial.Serial("/dev/ttyUSB0", 115200, timeout=1)
        serial_port = "Open"
        print("The port is available")

    except serial.serialutil.SerialException:
        print("The port is at use")
        ser.close()
        ser.open()
    # BLOQUE SERIAL