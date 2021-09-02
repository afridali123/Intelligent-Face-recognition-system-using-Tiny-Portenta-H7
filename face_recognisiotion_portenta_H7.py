#Welcome to Intelligent face recognition system on Arduino Portenta H7


import sensor, time, image

# Reset sensor
sensor.reset()
sensor.set_contrast(3)
sensor.set_gainceiling(16)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((320, 240))
sensor.set_pixformat(sensor.GRAYSCALE)

# Skip a few frames to allow the sensor settle down
sensor.skip_frames(time = 2000)


print("Welcome to Intelligent face recognition")
img = sensor.snapshot()
img.draw_string(0, 0, "Welcome to Intelligent face recognition", scale =2)
# Load Haar Cascade
# By default this will use all stages, lower satges is faster but less accurate.
face_cascade = image.HaarCascade("frontalface", stages=30)
print(face_cascade)

# First set of keypoints
kpts1 = None

# Find a face!
while (kpts1 == None):
    img = sensor.snapshot()
    img.draw_string(0, 0, "Looking for a face..." , scale =2)
    # Find faces
    objects = img.find_features(face_cascade, threshold=0.5, scale=1.25)
    if objects:
        # Expand the ROI by 31 pixels in every direction
        face = (objects[0][0]-31, objects[0][1]-31,objects[0][2]+31*2, objects[0][3]+31*2)
        # Extract keypoints using the detect face size as the ROI
        kpts1 = img.find_keypoints(threshold=10, scale_factor=1.1, max_keypoints=100, roi=face)
        # Draw a rectangle around the first face
        img.draw_rectangle(objects[0])

# Draw keypoints
#print(kpts1)
img.draw_keypoints(kpts1, size=24)
img = sensor.snapshot()
time.sleep_ms(2000)

# FPS clock
clock = time.clock()

while (True):
    clock.tick()
    img = sensor.snapshot()
    # Extract keypoints from the whole frame
    kpts2 = img.find_keypoints(threshold=10, scale_factor=1.1, max_keypoints=100, normalized=True)

    if (kpts2):
        # Match the first set of keypoints with the second one
        c=image.match_descriptor(kpts1, kpts2, threshold=85)
        match = c[6] # C[6] contains the number of matches.
        if (match>5):
            img.draw_rectangle(c[2:6])
            img.draw_cross(c[0], c[1], size=10)
            print("matched Features and face :%d dt:%d"%(match, c[7]))
            img.draw_string(0,50,"Afrid",scale = 2)
            #print(kpts2, "matched:%d dt:%d"%(match, c[7]))

    # Draw FPS
    img.draw_string(0, 0, "FPS:%.2f"%(clock.fps()), scale =2)



### thank you for visiting.

### Project link https://github.com/afridali123/Intelligent-Face-recognition-system-using-Tiny-Portenta-H7

### Demo video link https://www.youtube.com/watch?v=76tyOp6IdfQ


