# PC-LEGO-SPIKE-Simulator
Unofficial PC based LEGO SPIKE simulator in python environment

1.Introduction

  LEGO SPIKE is a great educational system for kids to learn the secrets of programming and robot building. The shortcoming of the system is that the program code cannot be tested conveniently. In order to test the written code, it is always necessary to build the complete hardware and the robot's behaviour is the only way to deduce the correct operation. This is what the LEGO SPIKE simulator is trying to help you with. The code written in the LEGO SPIKE environment can be tested without modification, without having a single LEGO hardware element, additional sensor or motor. The results of the simulator can be read on the console. The behaviour of the simulated peripherals can be pre-programmed. You can use a random number generator, but you can also cycle through increasing and decreasing values, or you can enter a value through the console. The program is open source. Some functionalities are not fully implemented.

2.Installation

  Required running environment:
  - PC with Windows 10 operating system. Theoretically, it can also be run under Linux and MAC. This description has been tested with Windows at the moment.
  
  Download the latest version of the python development environment and install it. E.g: python-3.10.0-amd64.exe
	https://www.python.org/downloads/
  Download the PC LEGO SPIKE Simulator (PC-LEGO-SPIKE-Simulator-main.zip) and unzip it to the directory where you want to work with it. E.g.: D:\PC-LEGO-SPIKE-Simulator-main\ 
	https://github.com/rundhall/PC-LEGO-SPIKE-Simulator 
  Find the lib directory of python. This is usually here: 
	C:\Users\<user name>\AppData\Local\Programs\Python\Python39\Lib\
  Copy the simulator directory under the Lib directory. 
	D:\PC-LEGO-SPIKE-Simulator-main\spike -> 
	C:\Users\<user name>\AppData\Local\Programs\Python\Python39\Lib\spike

3.Use

  Launch IDLE, the built-in development environment for python. In the Start menu, type IDLE and click on it. Now you can open LEGO SPIKE program codes and test it. For example open this file: D:\PC-LEGO-SPIKE-Simulator-main\example\1.Getting_started\getting_started.part1_simple_output.py
  The program can be run by pressing F5. The result can be read in another window in the IDLE Shell console.  
  You can control how the simulator works by editing the module files in the spike directory. Use IDLE Shell to open the .py file for each module, which can be found here:  
	C:\Users\<user name>\AppData\Local\Programs\Python\Python39\Lib\spike
  By default, the debug function is enabled, i.e. all events are printed to the console to help debugging, but this can be disabled at every module file by setting the ISDEBUG variable to False. 
  Simulator can operate in three modes: 
  - Circular: the simulated value will increase with time, then after reaching the maximum, it will decrease until it reaches the minimum value, from where it will increase again. The cycle alternates forever.  
  - Random: Returns a random number within the possible range. 
  - Console: The simulated value is entered on the console by you. The program will not run further until you have entered a value.
  The simulator operation can be set separately in each module using the SIMULATORTYPE variable.
  The following parameters can be set in the simulator:
  - Time between changes: SIMULATORTIME 
  - the rate of value modification during a change: SIMULATORCHANGE 
  - The maximum value simulated: SIMULATORSWITCHMAX 
  - Simulated minimum value: SIMULATORSWITCHMAX 

4.  Summary

  The PC-LEGO SPIKE simulator written in python language allows you to test the code written for the LEGO SPIKE robot without having a LEGO SPIKE robot, and it is suitable to create a special test environment that would be difficult to do with the real LEGO robot. The code for the simulator program is far from ready. Many functions are only partially implemented. There is still a lot of room for improvement on the simulator.



