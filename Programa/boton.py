#boton.py
from time import sleep
import os
import sys

from time import sleep
from pyA20.gpio import gpio
from pyA20.gpio import port
rele = port.PA6
clk = port.PA12
dt = port.PA11
gpio.init()
gpio.setcfg(clk, gpio.INPUT)
gpio.setcfg(dt, gpio.INPUT)
gpio.pullup(clk, 1)
gpio.pullup(dt, 1)

counter = 0
clkLastState = gpio.input(clk)
dtstate= gpio.input(dt)
try:
   while True:
      clkState = gpio.input(clk)
      #dtState = gpio.input(dt)
      if clkState == 0:
         counter += 1
      if counter >=6 :
         counter=1
      if (counter== 1) and (clkState==0) :
         print("Antena 1")

      if (counter== 2) and (clkState==0) :
         print("Antena 2")

      if (counter== 3) and (clkState==0) :
         print("Antena 3")

      if (counter== 4) and (clkState==0) :
         print("Antena 4")

      if (counter== 5) and (clkState==0) :
         print("Antena 5")


      clkLastState = clkState
      sleep(0.3)
finally:
        #GPIO.cleanup()
        gpio.cleanup()

