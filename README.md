# Camera Stream Raspberry Pi

1. Download or clone this repository
2. The "client PC" file is for PC
3. The "server Pi" file is for the Raspberry Pi


# To initiate HTTP server
1. In Raspberry Pi terminal, enter the command **ifconfig** and note down the IPv4 address of your network
2. In Raspberry Pi terminal, navigate to "server Pi" file using cd and initiate server using the command:
    **python -m http.server**, keep it running and minimize it.
3. In another Raspberry Pi terminal, cd to "server Pi", and run **python camera.py** to start camera feed.

# To stream camera feed on PC:
1. On PC, open "client PC" folder and modify **line 8** to the IPv4 address you noted earlier
2. Open an Anaconda Prompt, cd to "client PC" and run **python stream.py**
