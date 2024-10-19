# picamera
pip3 install flask picamera

sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-picamera2

If you are having problems getting the packages installed use the following parameters
pip install --break-system-packages requests
pip3 install picamera2

## Running the app
python3 camera.py
After running the server, you can access the video stream by navigating to http://<raspberry_pi_ip>:5000/video_feed in a browser. Replace <raspberry_pi_ip> with the actual IP address of your Raspberry Pi.

Set Up Chromium to Open the Stream Automatically

Create a script (start_viewer.sh) that launches Chromium in kiosk mode and points to the local video feed:
I Created it on the desktop to execute from a click

```
nano /home/pi/start_viewer.sh
```
Add the following content:


```
#!/bin/bash
# Start the Chromium browser in kiosk mode and point to the local Flask app
chromium-browser --kiosk --app=http://localhost:5000/video_feed
```

Make the script executable:

```
chmod +x /home/pi/start_viewer.sh
```
