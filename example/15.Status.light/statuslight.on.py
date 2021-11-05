'''on(color='white')
Sets the color of the light.
Parameters
color
Illuminates the Hub’s Brick Status Light in the specified color.
Type:String (text)
Values:"azure","black","blue","cyan","green","orange","pink","red","violet","yellow","white"
Default:"white"
Errors
TypeError
color is not a string.
ValueError
color is not one of the allowed values.
Example
'''
from spike import PrimeHub
import time
from machine import sleep

hub = PrimeHub()
#"azure","black","blue","cyan","green","orange","pink","red","violet","yellow","white"
hub.status_light.on('azure')
sleep(1000)
hub.status_light.on('black')
sleep(1000)
hub.status_light.on('blue')
sleep(1000)
hub.status_light.on('cyan')
sleep(1000)
hub.status_light.on('green')
sleep(1000)
hub.status_light.on('orange')
sleep(1000)
hub.status_light.on('pink')
sleep(1000)
hub.status_light.on('red')
sleep(1000)
hub.status_light.on('violet')
sleep(1000)
hub.status_light.on('yellow')
sleep(1000)
hub.status_light.on('white')
sleep(1000)
hub.status_light.on('test')
sleep(1000)


