def test_camera(camera):

    switcher.select(camera)

    picam2 = Picamera2()

    config = picam2.create_preview_configuration(
        main={"size": (1280,720)}
    )

    picam2.configure(config)

    picam2.start()

    time.sleep(2)

    frame = picam2.capture_array()

    print(camera, frame.shape)

    cv2.imshow(camera, cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))
    cv2.waitKey(0)

    picam2.stop()

test_camera("A")
test_camera("B")
