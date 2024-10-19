from picamera2 import Picamera2
from flask import Flask, Response
import io
from PIL import Image

app = Flask(__name__)
picam2 = Picamera2()

def generate_frames():
    # Check if the camera is already configured
    if picam2.camera_config is not None:
        picam2.stop()  # Stop the camera if it's already running
    picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
    picam2.start()

    try:
        while True:
            # Capture the frame as a numpy array
            frame = picam2.capture_array()
            # Convert the numpy array to a PIL image
            image = Image.fromarray(frame).convert('RGB')  # Convert to RGB
            # Save the PIL image to a BytesIO stream as JPEG
            image_stream = io.BytesIO()
            image.save(image_stream, 'JPEG')
            image_stream.seek(0)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + image_stream.read() + b'\r\n')
    finally:
        picam2.stop()

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True)
