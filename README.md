# CNC_Machine
Create a cheap, yet effective CNC machine for DIY/hobby/light-industrial use

The goal of this project is to manufacture a computer numerical control machine using everyday items only that are salvagable from materials around the house (excluding the processor that will e running the machine).

Framework and languages as follows:

Python:
• import G-Code file, read, and interpret coordinates (x,y,z) provided
• zero machine to home coordinates
• run start-up script to determine function to run (utilize raw_input for now, will transfer over to momentary switches in final design)

Java/C++ (on Arduino):
<!--anticipate processing power of Arduino Uno to be sufficient for initial testing but further expansion will require RaspberryPi for processing-->
• conductive zero-ing sequence for z-direction
• limit-switch zero-ing for x & y directions
• pause button
• set safe z-height using potentiometer live-feedback or numerical input (keypad)
