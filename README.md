# 3L3Y3

Spelled _Eli_, is a port scanner to scan the network. Ranging from individual IP addresses to scanning the whole website for open ports, _eli_ can be pretty efficient at this. Feel free to use and modify the tool under MIT License.

## About
__Important__: The main reason for me to create this tool was frustration...That of nmap pings getting blocked everytime I went to test a website. So I thought to create a private tool which instead of sending packets with NMAP signature on them, will send a blank requests to ports which will not get blocked by the server. Plus point: This is less suspicious than nmapping the host. Below is some more about the tool

  - It's light-weight, easy to use, compact, can be easily installed in _termux_ awa _Nethunter_.
  - Cleanly Maintained (with colored outputs)
  - Support to output in a file ( greppable format )
  - Automatic HostName Resolution
  
I tried to customize this scanner as much as possible, and made it very detailed as well. But one issue you will notice is... It is kinda slow, honestly it might take you about 10 minutes to scan the top200 ports. I countered that with threading, which reduced it by 3 more minutes. Honestly, I am trying to reduce it even further, will update the tool as soon as I get the solution. If you could help me, improve the tool feel free to mail your ideas/code snippet [here](mailto:theprojax@protonmail.com). 

## Installation

Installing it is pretty simple... Just copy the steps down into your terminal in order to install this script.

- ```git clone https://github.com/belikeParamjot/3L3Y3.git```
- ```cd 3L3Y3/```
- ```pip install -r requirements.txt```
- ```sudo cp eli.py /usr/bin/eli```
- ```sudo chmod +x /usr/bin/eli```
- ```cd ..```
- ```sudo rm -r 3L3Y3/```

This is it you've made a clean installation of the script. Run the script by just typing ```eli --help```.

## Usage and Features
