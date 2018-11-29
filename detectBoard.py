from transform import four_point_transform
import cv2
import imutils

def detectBoard(image):
    # Reshape image
    h = 500.0
    ratio = image.shape[0] / h
    orig = image.copy()
    image = imutils.resize(image, height = int(h))

    # Gray image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    # cv2.imshow("Gray", gray)

    # Canny edges
    edged = cv2.Canny(gray, 100, 200)
    # cv2.imshow("Edges", edged)

    # Find contours in image
    contours = cv2.findContours(edged.copy(), cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    contouredImage = image.copy()

    # Draw all contours
    cv2.drawContours(contouredImage, contours[1], -1, (0, 0, 255), 1)

    # Find largest contour with 4 sides which is assumed to be the board
    contours = contours[0] if imutils.is_cv2() else contours[1]
    contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
    boardContour = None
    for contour in contours:
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)

        if len(approx) == 4:
            # Found board
            boardContour = approx
            break

    if not boardContour is None:
        # Show the contours in the image
        cv2.drawContours(contouredImage, [boardContour], -1, (0, 255, 0), 2)
        # cv2.imshow("Contours", contouredImage)

        # Compute a top-down view of the image
        warped = four_point_transform(orig, boardContour.reshape(4, 2) * ratio)

        # Display the original and board found
        # cv2.imshow("Original", imutils.resize(orig, height = int(h)))
        board = imutils.resize(warped, height = int(h))
        # cv2.imshow("Board Found", board)

        board = cv2.resize(board, (int(h), int(h)))
        # cv2.imshow("Board Resized", board)
        # cv2.waitKey(0)

        cv2.imwrite("board.png", board)
        return board

    else:
        # Show the contours in the image
        # cv2.imshow("Contours", contouredImage)

        # Could not detect a board in the image.
        print("Could not detect board.")
        cv2.waitKey(0)

