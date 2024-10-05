from env import ENDPOINT, ACCESS_ID, ACCESS_KEY, USERNAME, PASSWORD, DEVICE_ID

from tuya_iot import TuyaOpenAPI, TUYA_LOGGER

# Initialization of tuya openapi
openapi = TuyaOpenAPI(ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect(USERNAME, PASSWORD, "86", 'smartlife')

# # Uncomment the following lines to see logs.
import logging

TUYA_LOGGER.setLevel(logging.DEBUG)

flag = True
while True:
    input('Hit Enter to toggle light switch.')
    flag = not flag
    commands = {'commands': [{'code': 'switch_led', 'value': flag}]}
    openapi.post('/v1.0/devices/{}/commands'.format(DEVICE_ID), commands)
	
