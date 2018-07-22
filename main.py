import network
import wifi_config
from umqtt_simple import MQTTClient
import mqtt_config
from machine import Pin, UART
from time import sleep
from micropyGPS import MicropyGPS

wifi = network.WLAN(network.STA_IF)

if not wifi.isconnected():
	wifi.active(True)
	wifi.connect(wifi_config.NAME, wifi_config.PASSWORD)
	while not wifi.isconnected():
		sleep(1)

mqtt = MQTTClient(mqtt_config.CLIENT_ID, mqtt_config.SERVER)
# mqtt.set_last_will(b"sensors/status/" + mqtt_config.CLIENT_ID, "OFFLINE")
mqtt.connect()
mqtt.publish(b"sensors/status/" + mqtt_config.CLIENT_ID, b"ONLINE")

uart = UART(2, 9600)
uart.init(9600, bits=8, parity=None, stop=1)

gps = MicropyGPS(location_formatting = "dd")

while True:
        data = uart.read()
        if data != None:
                for c in str(data):
                        gps.update(c)

                # 1 = no fix, 2 = 2D fix, 3 = 3D fix                        
                if gps.fix_type != 1 and gps.satellite_data_updated() and gps.time_since_fix() < 1000:
                        lat, ns = gps.latitude
                        lat *= 1 if ns == 'N' else -1
                        lon, ew = gps.longitude
                        lon *= 1 if ew == 'E' else -1
                        s = "%.6f,%.6f,%.1f,%d" % (lat, lon, gps.pdop, gps.satellites_in_use)
                        print(s)
                        mqtt.publish(b"sensors/gps/" + mqtt_config.CLIENT_ID, s)
                        # Dilution of Precision (DOP) values close to 1.0 indicate excellent quality position data
                        sleep(int(120 / gps.hdop))
