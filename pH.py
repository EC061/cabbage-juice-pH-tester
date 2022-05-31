def start(totalTest):
    # imports
    from machine import I2C, Pin
    from time import sleep, sleep_ms
    import urtc
    import tsl2591 
    from gc import collect
    collect()


    try:                                                                                                                                              
        open("pH_data.csv", "r")                                         
    except OSError:                                                                                                                                   
        datafile = open("pH_data.csv",'a')
        datafile.write("Time" + ',' + "Raw Data(Full Spectrum)"+ ',' + "Raw Data(Infrared)"+ ',' + "Luminosity" + '\n')
        datafile.close()

    p16 = Pin(16, Pin.IN)

    # -------------------------------------------------------------------------------
    # LEDs pin 13 for blue pin 15 for red
    # -------------------------------------------------------------------------------

    blueLED = Pin(13, Pin.OUT)
    redLED = Pin(15, Pin.OUT)
    blueLED.value(0)
    redLED.value(0)

    # -------------------------------------------------------------------------------
    # external RTC and light sensor
    # external rtc is powered by common rail 3v
    # -------------------------------------------------------------------------------
    i2c = I2C(scl = Pin(5), sda = Pin(4))   # Initalize the I2C pins
    light_sensor = tsl2591.Tsl2591(i2c) 
    rtc3231 = urtc.DS3231(i2c)              # Assign the DS3231


    # -------------------------------------------------------------------------------
    # Pump
    # -------------------------------------------------------------------------------

    # assign GPIO pin so you can turn on/off 
    relayWater = Pin(12, Pin.OUT)
    relayDye = Pin(14, Pin.OUT)
    # reset and prepare the pins for operation
    relayWater.value(0)
    relayDye.value(0)


    # n is number of times pump will run, s is length of runtime and sleeptime
    # function pump water is for pump on pin 12
    # function pump Dye is for pump on pin 14
    def pumpWater(n, s):
        for i in range(n):
            relayWater.value(1)
            sleep(s)
            relayWater.value(0)
            sleep(s)

    def pumpDye(n, s):
        for i in range(n):
            relayDye.value(1)
            sleep(s)
            relayDye.value(0)
            sleep(s)

    # -------------------------------------------------------------------------------
    # Testing cycle
    # -------------------------------------------------------------------------------   
    for i in range(totalTest):
        Pin(2,Pin.OUT).value(0)
        sleep(2)
        # Sampling data
        # Both pump runs
        pumpDye(1, 0.5)
        pumpWater(1, 1)

        blueLED.value(1)
        full_blue, ir_blue = light_sensor.get_full_luminosity()
        t_external_blue = rtc3231.datetime()

        lux_data_blue = light_sensor.calculate_lux(full_blue, ir_blue)
        timeStamp_blue = str(str(t_external_blue.year) + "-" + str(t_external_blue.month) + "-" + str(t_external_blue.day) + "-" + \
                        str(t_external_blue.hour) + "-" + str(t_external_blue.minute) + "-" + str(t_external_blue.second))
        print(timeStamp_blue, ', blue light: ',  lux_data_blue)
        blueLED.value(0)
        sleep_ms(1000)

        redLED.value(1)
        full_red, ir_red = light_sensor.get_full_luminosity()
        t_external_red = rtc3231.datetime()

        lux_data_red = light_sensor.calculate_lux(full_red, ir_red)
        timeStamp_red = str(str(t_external_red.year) + "-" + str(t_external_red.month) + "-" + str(t_external_red.day) + "-" + \
                        str(t_external_red.hour) + "-" + str(t_external_red.minute) + "-" + str(t_external_red.second))
        print(timeStamp_red, ', red light: ',  lux_data_red)
        redLED.value(0)
        sleep_ms(1000)

        # Save datafile: time, raw fullspectrum data, raw infrared data, luminosity data (still tring to figure out how they calculated that and what it means)
        datafile=open("pH_data.csv",'a')
        datafile.write(str(timeStamp_blue) + ',' + str(full_blue)+ ',' + str(ir_blue)+ ',' + str(lux_data_blue) + '\n')
        datafile.write(str(timeStamp_red) + ',' + str(full_red)+ ',' + str(ir_red)+ ',' + str(lux_data_red) + '\n')
        datafile.close()

        Pin(2,Pin.OUT).value(1)
        sleep(40)
    Pin(2,Pin.OUT).value(0)