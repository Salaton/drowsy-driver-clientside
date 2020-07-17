import datetime
import json
import os
import threading

import africastalking

import cv2
import dlib
import numpy
import pyglet
import requests
from imutils import face_utils
from scipy.spatial import distance

from driver_stats.models import Stats
from users.models import DrowsyDriverUser
from decouple import config


def vid(user):
    current_user = json.loads(user[0])

    """ Function that raises alarm"""

    def raise_alarm():
        alarm = pyglet.resource.media("utilities/watch.wav")
        alarm.play()

        pyglet.app.run()

    """Function that sends an alert to next of kin"""

    def send_alert(nextofkin_number):
        # Initialize SDK
        username = config("AFRICASTALKING_USERNAME")
        api_key = config("AFRICASTALKING_SECRET_KEY")
        africastalking.initialize(username, api_key)

        # Initialize a service e.g. SMS
        sms = africastalking.SMS

        # Use the service synchronously
        # response = sms.send("Wassup broskii", ["+254719158559"])
        # print(response)

        # Or use it asynchronously
        def on_finish(error, response):
            if error is not None:
                raise error
            print(response)

        getTime = datetime.datetime.now()
        currentTime = getTime.strftime("%H:%M")
        receiver = current_user["next_of_kin_name"]
        driver = current_user["first_name"]
        message = f"Hello there {receiver}, driver {driver} has been reported to be asleep at exactly {currentTime}"
        sms.send(
            message, [nextofkin_number], callback=on_finish,
        )

    """Computing the EYE ASPECT RATIO to determine blinking.."""

    def eyeAspectRatio(eyelandmark):
        # Computing the vertical parts
        p1 = distance.euclidean(eyelandmark[1], eyelandmark[5])
        p2 = distance.euclidean(eyelandmark[2], eyelandmark[4])
        # Computing the horizontal parts
        p3 = distance.euclidean(eyelandmark[0], eyelandmark[3])
        # Eye aspect ratio
        ear = (p1 + p2) / (2.0 * p3)

        return ear

    """
    Get the current time that the alarm was raised to indicate drowsiness,
    might be useful to provide insights..
    """

    def getTimeAlarmWasRaised(ear):
        getTime = datetime.datetime.now()
        currentTime = getTime.strftime("%H:%M")
        print(f"The alarm was raised at: {currentTime},with an eye threshold of: {ear}")

        # Later on, the time will be written to a file (idea is to create a dataset) for analysis and predictions..

    # Function to post details to the Database...
    def post_details_toDB(eye_aspect):
        # statistics = Stats(
        #     # user=user,
        #     first_name=user["first_name"],
        #     username=user["username"],
        #     last_name=user["last_name"],
        #     eye_aspect_ratio=eye_aspect,
        #     # time_alarm_raised = time_alarm_raised
        #     car_registration_number=user["car_registration_number"],
        # )
        statistics = Stats(
            user=DrowsyDriverUser.objects.get(username=current_user["username"]),
            eye_aspect_ratio=eye_aspect,
        )
        # statistics = Stats(
        #     user=current_user,
        # )
        # statistics.user = DrowsyDriverUser()

        statistics.save()

    """
    # EAR to show a blink. If EAR falls below the threshold and then rises, that's a blink
    """
    EYE_EAR_THRESH = 0.15
    # no of consecutive frames that the eye must be below the threshold
    EYE_AR_CONSEC_FRAMES = 5

    WARNING_COUNTER = 0
    RAISED_ALARM = False
    TOTAL = 0
    """Getting the coordinates of the left and right eye"""
    (left_eye_start, left_eye_end) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
    (right_eye_start, right_eye_end) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

    # load XML classifier
    face_cascade = cv2.CascadeClassifier(
        "utilities/haarcascade_frontalface_default.xml"
    )

    # load eye classifier
    eye_cascade = cv2.CascadeClassifier("utilities/haarcascade_eye_tree_eyeglasses.xml")
    # check if classifier is loaded for error handling..
    loaded = cv2.CascadeClassifier.empty(face_cascade)
    print(f"{loaded}: The classifier is loaded correctly, ready to identify the face")
    if loaded == True:
        print("You need to load the classifier")

    # Start the video stream
    # capture = cv2.VideoCapture('https://192.168.100.7:8080/video')
    capture = cv2.VideoCapture(0)

    eye_predictor_path = "utilities/shape_predictor_68_face_landmarks.dat"
    # Detector model
    faceDetector = dlib.get_frontal_face_detector()
    # predictor model
    eye_predictor = dlib.shape_predictor(eye_predictor_path)


    # Start looping over the frames
    while True:

        # capture frame by frame (returns true or false)
        ret, frame = capture.read()

        if ret == False:
            print("Camera Failed to start...")

        # operation on the frames
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        for face in faces:
            # print(x, y, w, h)
            x1, y1, w, h = face
            x2 = x1 + w
            y2 = y1 + h
            # rectangle(img, pt1, pt2, color, thickness=None, lineType=None, shift=None, /)
            img = cv2.rectangle(gray, (x1, y1), (x2, y2), (0, 255, 239), 2, 4)
            # convert faces from np.array to dlib rectangle (For compatibility)
            faces_dlib = dlib.rectangle(x1, y1, x2, y2)
            # print(faces_dlib)
            landmarks = eye_predictor(gray, faces_dlib)
            # convert the face coordinates to Numpy Array
            landmark = face_utils.shape_to_np(landmarks)
            # print(landmark)
            # landmarks = face_utils.shape_to_np(landmarks)

            """Applying landmarks to the face.."""
            for n in range(0, 68):
                x = landmarks.part(n).x
                y = landmarks.part(n).y
                cv2.circle(gray, (x, y), 4, (36, 36, 246), -1)

            leftEye = landmark[left_eye_start:left_eye_end]
            rightEye = landmark[right_eye_start:right_eye_end]

            left_eye_aspect_ratio = eyeAspectRatio(leftEye)
            right_eye_aspect_ratio = eyeAspectRatio(rightEye)

            # EAR for combined eyes
            eyeaspect_ratio = (left_eye_aspect_ratio + right_eye_aspect_ratio) / 2.0
            print(eyeaspect_ratio)
            # Output EAR  to the screen
            cv2.putText(
                img,
                "EAR: {:.3f}".format(eyeaspect_ratio),
                (300, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                2,
            )
            """Raising the alarm logic!"""
            if eyeaspect_ratio < EYE_EAR_THRESH:
                WARNING_COUNTER += 1

                if WARNING_COUNTER > EYE_EAR_THRESH:
                    if not RAISED_ALARM:
                        RAISED_ALARM = True

                        # We get the time the alarm was raised...
                        getTimeAlarmWasRaised(eyeaspect_ratio)
                        # os.system(
                        #     'spd-say "Drowsiness levels detected! You might need to take a break"')

                        # raise_alarm()
                        # Having the alarm function running as a thread
                        alarmThread = threading.Thread(target=raise_alarm)
                        alarmThread.daemon = True
                        alarmThread.start()

                        cv2.putText(
                            img,
                            "Drowsiness Detected!!!!",
                            (5, 30),
                            cv2.FONT_HERSHEY_SIMPLEX,
                            1,
                            (0, 0, 255),
                            2,
                        )
                        posting_db_thread = threading.Thread(
                            target=post_details_toDB, args=(eyeaspect_ratio,)
                        )
                        posting_db_thread.daemon = True
                        posting_db_thread.start()

                        sending_alert_thread = threading.Thread(
                            target=send_alert, args=(user["next_of_kin_number"],)
                        )
                        sending_alert_thread.daemon = True
                        sending_alert_thread.start()

            else:
                WARNING_COUNTER = 0
                RAISED_ALARM = False
            # ROI for the face so that eyes can be detected
            roi_gray = gray[y1:y2, x1:x2]
            roi_color = gray[y1:y2, x1:x2]
            # detecting the eye..
            eyes = eye_cascade.detectMultiScale(roi_gray)
            # iterate over all eyes found on face
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

            font = cv2.FONT_HERSHEY_SIMPLEX
            bottomLeftCornerOfText = (x, y + h + 30)
            fontScale = 1
            fontColor = (255, 255, 255)
            lineType = 2

            cv2.putText(
                img,
                current_user["first_name"],
                (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 255, 0),
                2,
            )
            # cv2.putText(img, driverprofile.regNo, (x, y+h+60),
            #             font, fontScale, fontColor, lineType)
            # # cv2.putText(img, driverprofile.email, (x, y+h+90),
            # #             font, fontScale, fontColor, lineType)
            # cv2.putText(img, driverprofile.phoneNumber, (x, y+h+120),
            #             font, fontScale, fontColor, lineType)
            # cv2.putText(img, driverprofile.nextOfKin, (x, y+h+150),
            #             font, fontScale, fontColor, lineType)
        cv2.imshow("gray", gray)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # when everything is dones, release the capture
    capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    vid()
