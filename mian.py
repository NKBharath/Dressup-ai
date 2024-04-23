import cv2
import cv2 as cv
import mediapipe as mp
import cvzone
import pyautogui
import numpy as np

import mediapipe as mp

# Initialize drawing utilities
mpdraw = mp.solutions.drawing_utils

# Initialize pose estimation module
mpPose = mp.solutions.pose
pose = mpPose.Pose()




a = int(input("enter 1 to capture    current image or enter 2 to load the image"))

if a == 1:
    print("working")

elif a == 2:

    top_bottom_full = (input("You need to change top or bottom")).lower()

    if top_bottom_full == "top":
        # receiving the persons image
        print("assure that the image is in necessary folder")
        path = input("enter the name of the image")
        image = cv.imread('photos/' + path + '.jpg')
        image_display = image

        # cal screen size
        screen_width, screen_height = pyautogui.size()

        # changing the size
        image_height = 643
        image_width = 474

        # implementing
        image = cv.resize(image, (image_width, image_height))
        # pose detecting
        k = 1
        while k < 2:
            imgrgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = pose.process(imgrgb)

            # print(results.pose_landmarks)
            k += 1
            if results.pose_landmarks:
                pathimage = mpdraw.draw_landmarks(image, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
                landmarks_display = pathimage
                # detecting the specific coordinates
                left_shoulder = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_SHOULDER]
                right_shoulder = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_SHOULDER]
                right_hip = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_HIP]

                # Convert normalized coordinates to image coordinates
                h, w, _ = image.shape
                left_shoulder_x, left_shoulder_y = int(left_shoulder.x * w), int(left_shoulder.y * h)
                right_shoulder_x, right_shoulder_y = int(right_shoulder.x * w), int(right_shoulder.y * h)
                right_hip_x, right_hip_y = int(right_hip.x * w), int(right_hip.y * h)

                # Store coordinates in variables
                left_shoulder_coords = (left_shoulder_x, left_shoulder_y)
                right_shoulder_coords = (right_shoulder_x, right_shoulder_y)
                right_hip_coords = (right_hip_x, right_hip_y)

                # storing coordinates into individual variable
                image_front_x, image_front_y = right_shoulder_coords

        # converting coordinates to distance
        def calculate_distance_bw_coords(coord1, coord2):
            return np.linalg.norm(np.array(coord2) - np.array(coord1))


        width = int(calculate_distance_bw_coords(right_shoulder_coords, left_shoulder_coords))
        height = int(calculate_distance_bw_coords(right_shoulder_coords, right_hip_coords))

        # receiving the dress name
        top_dress = input("enter the name of the dress")
        top_dress_display = top_dress

        # to display the image
        cv2.imshow("persons image",image_display)
        cv2.waitKey(0)
        #cv2.imshow("dress image",top_dress)
        #cv2.waitKey(0)
        def dispimg(a, b):
            # to increment the back image name
            i = 0
            image_back = image + i
            image_backi = image_back

            image_front = cv.imread('dress/'+top_dress+'.png', cv.IMREAD_UNCHANGED)
            image_front = cv.resize(image_front, (1023, 1000))
            # resizing the dress to body type
            image_front = cv.resize(image_front, (width + int(width * 0.7), height + int(height * 0.3)))
            image_overlay = cvzone.overlayPNG(image_backi, image_front, [image_front_x - a, image_front_y - b])
            final_image = cv.resize(image_overlay, (int(screen_width / 2), int(screen_height)))

            # displaying the image
            cv.imshow("img", final_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
            i += 1
            return final_image

        def dispimg1(a, b):
            # to increment the back image name
            i = 0
            image_back = image + i
            image_backi = image_back

            image_front = cv.imread('dress/'+top_dress+'.png', cv.IMREAD_UNCHANGED)
            image_front = cv.resize(image_front, (1023, 1000))
            # resizing the dress to body type
            image_front = cv.resize(image_front, (width + int(width * 0.7), height + int(height * 0.3)))
            image_overlay = cvzone.overlayPNG(image_backi, image_front, [image_front_x - a, image_front_y - b])
            final_image = cv.resize(image_overlay, (int(screen_width / 2), int(screen_height)))

            # displaying the image
            cv.imshow("img", final_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
            i += 1
            return final_image

        a1 = 60
        b1 = 60
        save_image1 = dispimg(a1, b1)
        # to change the position of the image
        for _ in range(50):
            entry = input("Enter Y if image is ok \nEnter N if you want to move the dress")

            # to change
            if entry == 'N' or entry == 'n':
                x_move = input("To move the dress up press U \nTo move the dress down press D\nTo move the dress left "
                               "press l\nTo move the dress right press r")

                # this condition works to move the image upwards
                if x_move == 'U' or x_move == 'u':
                    y_change = 60
                    for move in range(100):
                        save_image = dispimg(a1, y_change)
                        y_change += 10
                        move += 1
                        break_point = input("Enter Y if dress is ok \nEnter N if you want to move the dress")
                        if break_point == 'y':
                            # asking whether to move the image in some other directions
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")
                            if second_move == 'y' or second_move == 'Y':
                                # this condition works if the user is ok with the image
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break

                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input("To move the image towards left press L\nTo move the image towards right press R")
                                if x_move_1 == 'r' or x_move_1 == 'R':
                                    a1_1 = a1
                                    b1_1 = y_change
                                    y_change = -10

                                    # to move the image towards right in second move
                                    for move in range(100):
                                        save_image = dispimg1((50 - (-y_change)), b1_1)
                                        y_change += -10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \n enter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break

                                elif x_move_1 == 'l' or x_move_1 == 'L':
                                    a1_1 = a1
                                    b1_1 = y_change
                                    y_change = 60

                                    # to move the image towards left for the second move
                                    for move in range(100):
                                        save_image = dispimg(y_change, b1_1)
                                        y_change += 5
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                break

                # this condition works to move the image towards down
                elif x_move == 'D' or x_move == 'd':
                    y_change1 = -10
                    for move in range(100):
                        save_image = dispimg1(a=a1, b=(50-(-y_change1)))
                        y_change1 += -5
                        move += 1
                        break_point = input("Enter Y if dress is ok \nEnter N if you want to move the dress")
                        if break_point == 'y':
                            # asking whether to move the image in some other directions
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")
                            if second_move == 'y' or second_move == 'Y':
                                # this condition works if the user is ok with the image
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break
                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards left press L\nTo move the image towards right press R")
                                if x_move_1 == 'r' or x_move_1 == 'R':
                                    a1_1 = a1
                                    b1_1 = y_change1
                                    y_change = -10

                                    # to move the image towards right after moving down
                                    for move in range(100):
                                        save_image = dispimg1((50 - (-y_change)), 50 -(-b1_1))
                                        y_change += -10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \n enter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break

                                elif x_move_1 == 'l' or x_move_1 == 'L':
                                    a1_1 = a1
                                    b1_1 = y_change1
                                    y_change = 60

                                    # to move the image towards left after moving down
                                    for move in range(100):
                                        save_image = dispimg(y_change, 50 - (-b1_1))
                                        y_change += 5
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                break

                # this condition works to move the image towards left
                elif x_move == 'L' or x_move == 'l':
                    y_change = 60
                    for move in range(100):
                        save_image = dispimg(y_change, b1)
                        y_change += 5
                        move += 1
                        break_point = input("Enter Y if dress is ok \nEnter N if you want to move the dress")
                        if break_point == 'y':
                            # asking whether to move the image in some other directions
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")
                            if second_move == 'y' or second_move == 'Y':
                                # this condition works if the user is ok with the image
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break

                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards up press U\nTo move the image towards down press D")

                                if x_move_1 == 'u' or x_move_1 == 'U':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change = 60

                                    # to move the image up after moving the image  left
                                    for move in range(100):
                                        save_image = dispimg(a1_1, y_change)
                                        y_change += 10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break

                                elif x_move_1 == 'd' or x_move_1 == 'D':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change1 = -10

                                    # to move the image down after moving it left
                                    for move in range(100):
                                        save_image = dispimg1(a=a1_1, b=(50 - (-y_change1)))
                                        y_change1 += -5
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                break

                # this condition works to move the image towards right
                elif x_move == 'R' or x_move == 'r':
                    y_change = -10
                    for move in range(100):
                        save_image = dispimg1((50-(-y_change)), b1)
                        y_change += -10
                        move += 1
                        break_point = input("Enter Y if dress is ok \n enter N if you want to move the dress")
                        if break_point == 'y':
                            # asking whether to move the image in some other directions
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")
                            if second_move == 'y' or second_move == 'Y':
                                # this condition works if the user is ok with the image
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break

                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards up press U\nTo move the image towards down press D")

                                if x_move_1 == 'u' or x_move_1 == 'U':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change = 60

                                    # to move the image up after moving it right
                                    for move in range(100):
                                        save_image = dispimg(a1_1, y_change)
                                        y_change += 10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break

                                elif x_move_1 == 'd' or x_move_1 == 'D':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change1 = -10

                                    # to move the image down after moving it right
                                    for move in range(100):
                                        save_image = dispimg1(a=a1_1, b=(50 - (-y_change1)))
                                        y_change1 += -5
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                break


            else:
                name_person = input("enter your name")
                save_image = cv2.imwrite("saved images/"+name_person+".jpg", save_image1)
                break
            break

    elif top_bottom_full == "bottom":
        # receiving the persons image
        print("assure that the image is in necessary folder")
        path = input("enter the name of the image")
        image = cv.imread('photos/' + path + '.jpg')


        # cal screen size
        screen_width, screen_height = pyautogui.size()

        # changing the size
        image_height = 643
        image_width = 474

        # implementing
        image = cv.resize(image, (image_width, image_height))
        image_disp = image
        k = 1
        while k < 2:
            imgrgb = cv.cvtColor(image, cv.COLOR_BGR2RGB)
            results = pose.process(imgrgb)
            # print(results.pose_landmarks)
            k += 1
            if results.pose_landmarks:
                # pathimage = mpdraw.draw_landmarks(image, results.pose_landmarks, mpPose.POSE_CONNECTIONS)

                # detecting the specific coordinates
                left_hip = results.pose_landmarks.landmark[mpPose.PoseLandmark.LEFT_HIP]
                right_hip = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_HIP]
                right_heel = results.pose_landmarks.landmark[mpPose.PoseLandmark.RIGHT_HEEL]

                # Convert normalized coordinates to image coordinates
                h, w, _ = image.shape
                left_hip_x, left_hip_y = int(left_hip.x * w), int(left_hip.y * h)
                right_hip_x, right_hip_y = int(right_hip.x * w), int(right_hip.y * h)
                right_heel_x, right_heel_y = int(right_heel.x * w), int(right_heel.y * h)

                # Store coordinates in variables
                left_hip_coords = (left_hip_x, left_hip_y)
                right_hip_coords = (right_hip_x, right_hip_y)
                right_heel_coords = (right_heel_x, right_heel_y)

                # storing coordinates into individual variable
                image_front_x, image_front_y = right_hip_coords


        cv2.imshow("persons image",image_disp)
        # converting coordinates to distance
        def calculate_distance_bw_coords(coord1, coord2):
            return np.linalg.norm(np.array(coord2) - np.array(coord1))


        width = int(calculate_distance_bw_coords(right_hip_coords, left_hip_coords))
        height = int(calculate_distance_bw_coords(right_hip_coords, right_heel_coords))
        #print(width, height)

        # receiving dress from the user
        bottom_dress = input("Enter the dress name")
        def dispimg(a, b):
            # to increment the back image name
            i = 0
            image_back = image + i
            image_backi = image_back

            image_front = cv.imread('dress/'+bottom_dress+'.png', cv.IMREAD_UNCHANGED)

            # resizing the dress to body type
            image_front = cv.resize(image_front, (width + int(width * 1.5), height+int(height * 0.2)))
            image_overlay = cvzone.overlayPNG(image_backi, image_front, [image_front_x - a, image_front_y - b])
            final_image = cv.resize(image_overlay, (int(screen_width / 2), int(screen_height)))

            # displaying the image
            cv.imshow("img", final_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
            i += 1
            return final_image

        def dispimg1(a, b):
            # to increment the back image name
            i = 0
            image_back = image + i
            image_backi = image_back

            image_front = cv.imread('dress/'+bottom_dress+'.png', cv.IMREAD_UNCHANGED)

            # resizing the dress to body type
            image_front = cv.resize(image_front, (width + int(width * 1.5), height+int(height * 0.2)))
            image_overlay = cvzone.overlayPNG(image_backi, image_front, [image_front_x - a, image_front_y - b])
            final_image = cv.resize(image_overlay, (int(screen_width / 2), int(screen_height)))

            # displaying the image
            cv.imshow("img", final_image)
            cv.waitKey(0)
            cv.destroyAllWindows()
            i += 1
            return final_image


        a1 = 70
        b1 = 50
        save_image1 = dispimg(a1, b1)
        # to change the position of the image
        for _ in range(50):
            entry = input("Enter Y if image is ok \nEnter N if you want to move the dress")

            # to change
            if entry == 'N' or entry == 'n':
                x_move = input("To move the dress up press U \nTo move the dress down press D\nTo move the dress left "
                               "press l\nTo move the dress right press r")
                if x_move == 'U' or x_move == 'u':
                    y_change = 60
                    for move in range(100):
                        save_image = dispimg(a1, y_change)
                        y_change += 10
                        move += 1
                        break_point = input("Enter Y if dress is ok \nEnter N if you want to move the dress")
                        if break_point == 'y':
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")

                            if second_move == 'y' or second_move == 'Y':
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break

                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards left press L\nTo move the image towards right press R")
                                if x_move_1 == 'r' or x_move_1 == 'R':
                                    a1_1 = a1
                                    b1_1 = y_change
                                    y_change = 60
                                    for move in range(100):
                                        save_image = dispimg(y_change, b1_1)
                                        y_change += 1
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                elif x_move_1 == 'L' or x_move_1 == 'l':
                                    a1_1 = a1
                                    b1_1 = y_change
                                    y_change = -10
                                    for move in range(100):
                                        save_image = dispimg1((50 - (-y_change)), b1_1)
                                        y_change += -10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \n enter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break

                                break
                elif x_move == 'D' or x_move == 'd':
                    y_change1 = -10
                    for move in range(100):
                        save_image = dispimg1(a=a1, b=(50 - (-y_change1)))
                        y_change1 += -5
                        move += 1
                        break_point = input("Enter Y if dress is ok \nEnter N if you want to move the dress")
                        if break_point == 'y':
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")

                            if second_move == 'y' or second_move == 'Y':
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break
                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards left press L\nTo move the image towards right press R")
                                if x_move_1 == 'l' or x_move_1 == 'L':
                                    a1_1 = a1
                                    b1_1 = y_change1
                                    y_change = 60
                                    for move in range(100):
                                        save_image = dispimg(y_change,(50-(- b1_1)))
                                        y_change += 1
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                elif x_move_1 == 'R' or x_move_1 == 'r':
                                    a1_1 = a1
                                    b1_1 = y_change1
                                    y_change = -10
                                    for move in range(100):
                                        save_image = dispimg1((50 - (-y_change)), b1_1)
                                        y_change += -10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \n enter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break

                                break
                elif x_move == 'L' or x_move == 'l':
                    y_change = 60
                    for move in range(100):
                        save_image = dispimg(y_change, b1)
                        y_change += 1
                        move += 1
                        break_point = input("Enter Y if dress is ok \nEnter N if you want to move the dress")
                        if break_point == 'y':
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")

                            if second_move == 'y' or second_move == 'Y':
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break
                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards up press U\nTo move the image towards down press D")

                                if x_move_1 == 'U' or x_move_1 == 'u':
                                    a1_1 =y_change
                                    b1_1 = b1
                                    y_change = 60
                                    for move in range(100):
                                        save_image = dispimg(a1_1, y_change)
                                        y_change += 10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                elif x_move_1 == 'D' or x_move_1 == 'd':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change1 = -10
                                    for move in range(100):
                                        save_image = dispimg1(a=a1_1, b=(50 - (-y_change1)))
                                        y_change1 += -5
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                break
                elif x_move == 'R' or x_move == 'r':
                    y_change = -10
                    for move in range(100):
                        save_image = dispimg1((50 - (-y_change)), b1)
                        y_change += -10
                        move += 1
                        break_point = input("Enter Y if dress is ok \n enter N if you want to move the dress")
                        if break_point == 'y':
                            second_move = input("Enter N if you want to the images in some other directions\nEnter Y"
                                                "if you are ok with the image")

                            if second_move == 'y' or second_move == 'Y':
                                name_person = input("enter your name")
                                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                break
                            elif second_move == 'n' or second_move == 'N':
                                # this condition works if the user wants to move the dress in some other direction
                                x_move_1 = input(
                                    "To move the image towards up press U\nTo move the image towards down press D")

                                if x_move_1 == 'U' or x_move_1 == 'u':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change = 60
                                    for move in range(100):
                                        save_image = dispimg((50-(-a1_1)), y_change)
                                        y_change += 10
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                elif x_move_1 == 'D' or x_move_1 == 'd':
                                    a1_1 = y_change
                                    b1_1 = b1
                                    y_change1 = -10
                                    for move in range(100):
                                        save_image = dispimg1(a=a1_1, b=(50 - (-y_change1)))
                                        y_change1 += -5
                                        move += 1
                                        break_point = input(
                                            "Enter Y if dress is ok \nEnter N if you want to move the dress")
                                        if break_point == 'y':
                                            name_person = input("enter your name")
                                            save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image)
                                            break
                                break

            else:
                name_person = input("enter your name")
                save_image = cv2.imwrite("saved images/" + name_person + ".jpg", save_image1)
                break
            break

else:
    print("invalid input")