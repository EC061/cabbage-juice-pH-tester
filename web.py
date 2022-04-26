import network
import env
import json
import time
sta_if = network.WLAN(network.STA_IF)

# Connect to Wi-Fi with:
#     1. Stored Wi-Fi information(ssid, password) in environmental variable
#     2. User inputted information(ssid, password)
# Print network config after network connection established
# Due to hardware limitation, ESP8266 might not be able to connect to router without legacy Wi-Fi protocal support
def connect():
    if not sta_if.isconnected():
        env_decision = input("Use saved setting? (Y or N) \n")
        ssid = ""
        password = ""
        while not ssid or not password:
            if env_decision.lower() == "y":
                ssid = env.ssid
                password = env.password
            elif env_decision.lower() == "n":
                ssid = input("Wi-Fi name: ")
                password = input("Password: ")
            else:
                print("Invalid input, please try again.")
                env_decision = input("Use saved setting? (Y or N) \n")
        print("connecting to " + ssid + " ...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print("network config: " + str(sta_if.ifconfig()) + "\nConnection established.")
    
# Send inputted data with post method to thingspeak API
# Requires API key obtained from thingspeak stored in environmental variable
def sendData(date, d1, d2, d3):
    if not sta_if.isconnected():
        print("Please connect to a network before uploading data.")
    else:
        import urequests   
        
        HTTP_HEADERS = {'Content-Type': 'application/json'} 

        data = {'field1':date, 'field2':d1, 'field3':d2, 'field4':d3}
        
        status_code = 0
        
        while status_code != 200:
            request = urequests.post('http://api.thingspeak.com/update?api_key=' +  
            env.WRITE_API_KEY, json = data, headers = HTTP_HEADERS)
            status_code = request.status_code
            if status_code != 200:
                print(request.status_code)
                print(request.reason)
                time.sleep_ms(2000)
            
        print(status_code)
        request.close()

# Close active connection to the router
def close():
    sta_if.active(0)
    