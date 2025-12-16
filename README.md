Python Program to Read and Display Sensor Data

Install pyserial:
Open terminal / CMD
1. pip install pyserial

If needed live graph:
2. pip install matplotlib

3. pip install playsound

Determination of motion of object (In this case Animals near the highways) by using simple circuit using Audino and IR sensors

Parts Required
1.	Arduino UNO / Nano
2.	Reflective IR Sensor (TCRT5000 module)
3.	USB cable (to connect Arduino → Laptop)
4.	Jumper wires
5.	Breadboard (optional)

Wiring: 
Connect IR Sensor → Arduino → Laptop

IR Reflective Sensor Pins
•	VCC → Arduino 5V
•	GND → Arduino GND
•	OUT → Arduino D2 (you can use any digital pin)

✔ Final circuit:
IR Sensor VCC  → 5V  
IR Sensor GND  → GND  
IR Sensor OUT  → D2  

<b>AI Generated Example Image:<b>

<img width="473" height="316" alt="image" src="https://github.com/user-attachments/assets/27826ba9-b1de-41ed-90a9-0b6676d0b097" />

# Electrical-Mini-Project-

Laptop Connection
•	Connect Arduino to your laptop using USB cable
•	No extra drivers needed for Arduino Uno
•	If using a clone board, install CH340 driver

NOTE:MAX DISTANCE FROM IR TO RECOGNIZE OBJECT IS 3CM 


OUTPUT FOR GUI PROGRAM:
NOTE: THE OUTPUT IS FOR WHEN BOTH SENSORS DETECT OBJECT  
<img width="501" height="328" alt="image" src="https://github.com/user-attachments/assets/4ad9857d-c999-46e0-aefb-6710ae26c306" />

OUTPUT FOR GRAPH PROGRAM:
<img width="645" height="557" alt="image" src="https://github.com/user-attachments/assets/ae3527f1-9b09-4dbb-87fe-3d269ed457d4" />

