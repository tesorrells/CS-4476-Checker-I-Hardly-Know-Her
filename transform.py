import numpy as np
import cv2

def order_points(points):
    rectangle = np.zeros((4, 2), dtype = "float32")

    sum = points.sum(axis = 1)
    diff = np.diff(points, axis = 1)
    rectangle[0] = points[np.argmin(sum)]
    rectangle[1] = points[np.argmin(diff)]
    rectangle[2] = points[np.argmax(sum)]
    rectangle[3] = points[np.argmax(diff)]

    return rectangle

def four_point_transform(img, points):
    rectangle = order_points(points)
    (ul, ur, br, bl) = rectangle

    upperWidth = int(np.sqrt(((ur[0] - ul[0]) ** 2) + ((ur[1] - ul[1]) ** 2)))
    bottomWidth = int(np.sqrt(((br[0] - bl[0]) ** 2) + ((br[1] - bl[1]) ** 2)))
    maxWidth = max(bottomWidth, upperWidth)

    upperHeight = int(np.sqrt(((ur[0] - br[0]) ** 2) + ((ur[1] - br[1]) ** 2)))
    bottomHeight = int(np.sqrt(((ul[0] - bl[0]) ** 2) + ((ul[1] - bl[1]) ** 2)))
    maxHeight = max(upperHeight, bottomHeight)

    dest = np.array([[0, 0],
                    [maxWidth - 1, 0],
                    [maxWidth - 1, maxHeight - 1],
                    [0, maxHeight - 1]], dtype = "float32")

    matrix = cv2.getPerspectiveTransform(rectangle, dest)
    transformed = cv2.warpPerspective(img, matrix, (maxWidth, maxHeight))

    return transformed
