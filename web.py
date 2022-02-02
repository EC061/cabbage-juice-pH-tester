import network
from time import sleep
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True) 
sta_if.connect(ssid, password)
sleep(1) 
print(sta_if.isconnected()) 

def testdata(date, d1, d2, d3):
    import urequests   
    HTTP_HEADERS = {'Content-Type': 'application/json'} 

    data = {'field1':date, 'field2':d1, 'field3':d2, 'field4':d3}

    request = urequests.post('http://api.thingspeak.com/update?api_key=' +  
    WRITE_API_KEY, json = data, headers = HTTP_HEADERS) 
    request.close()

    sta_if.active (0)
    print(sta_if.isconnected())