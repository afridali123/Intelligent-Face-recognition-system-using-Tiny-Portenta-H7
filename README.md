# Intelligent Face recognition system using Tiny Arduino Portenta-H7

A facial recognition system is a technology capable of matching a human face from a digital image or a video frame against a database of faces. we have many algorithms and approaches are there but the challenge is optimizing and running this system on Tiny or edge computing devices.

In this project, I'm going to use Tiny Microcontroller board "Arduino Portenta H7". Its small formfactor board ; size of Small Fivestar or DiaryMilk chocolate.you can find specs of the board in this link - https://store.arduino.cc/portenta-H7

For the Proof of concept, i have trained with my own image dataset to recognise my face. without delays lets get started !!!

## Hardware Used :
	1.Arduino portenta H7
	2.Portenta Vision Shield
	3.Type C USB cable
## Software Used :
	1.Micro Python
	2.OpenMV IDE

## Project Description :

Fistly, you need basic familiar with python or any programming language. I used OpenMV libraries for this project.Firstly we have to extract key features from face like nose,eyes and other locations. i m using haar cascade filter to get this feature vectors. i'm going to store those features vectors. next i'm going to look or turnon video stream for continuos frames. i will compare the incoming faces from frames with stored feature vectors. you can fine the complete video demo link below

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/76tyOp6IdfQ/0.jpg)](https://www.youtube.com/watch?v=76tyOp6IdfQ)


you can pull or download the code from this repository. Thank you for viewing my tutorial, you can furthur develop or use this project. i m very happy to support or interact, you can reach out to me on afridali123@gmail.com.



