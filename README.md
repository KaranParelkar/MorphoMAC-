# MorphoMAC-
The provided Python script is a command-line tool called "MorphoMAC" designed to change the MAC address of network interfaces (eth0 or wlan0) on a Linux system. It utilizes the subprocess module to interact with system commands and the requests module for handling HTTP requests.
The tool displays a banner with the title "MorphoMAC" and developer information. It then prompts the user to choose their network connection type (eth0, wlan0) or exit the tool. After selecting the network interface, the tool retrieves the current MAC address, prompts the user to input a new MAC address, and proceeds to change the MAC address using the ifconfig command.


Steps for Using the Tool:

1.Ensure Python 3 is installed on your system.
2.Clone or download the script from GitHub.
3.Open a terminal and navigate to the directory containing the script.
3.Make the script executable using the command: chmod +x morphomac.py.
4.Run the script using the command: ./morphomac.py.
5.Follow the on-screen instructions to choose the network interface and input the new MAC address.
6.The tool will display messages indicating the MAC address change process.
7.Verify the MAC address change using the ifconfig command.


Installation:

Clone the Repository: Clone the repository containing the "MorphoMAC" tool to your local machine. You can do this using the following command:

    git clone https://github.com/YourUsername/MorphoMAC.git

Navigate to the Directory: Enter the directory where the tool is located:

    cd MorphoMAC

Make the Script Executable: Make sure the script is executable by changing its permissions:

    chmod +x MorphoMAC.py

Change to the Root user: Change from normal user to root user to gain the root access:

    sudo su

Install Dependencies: Ensure that Python 3 is installed on your system. If the requests module is not installed, you can install it using pip:

    pip install requests


Usage:

Run the Script: Execute the script by running the following command:

    ./morphomac.py

Follow On-Screen Instructions: The tool will display a banner with information about the developer and instructions. Follow the on-screen prompts to select your network connection type (eth0, wlan0) or exit the tool.

Input New MAC Address: After selecting the network interface, you will be prompted to input the new MAC address you want to assign to the interface.

MAC Address Change: The tool will display messages indicating the MAC address change process. It will use the ifconfig command to bring down the interface, assign the new MAC address, and bring the interface back up.

Verify Changes: You can verify that the MAC address has been changed successfully by using the ifconfig command or any other network interface management tool.



Contributions:

Contributions to the "MorphoMAC" tool are welcome! You can contribute by:

Reporting bugs or suggesting improvements by opening an issue on GitHub.
Forking the repository, making your changes, and submitting a pull request.

Make sure to include a clear description of your changes when submitting a pull request. Happy hacking!!!
