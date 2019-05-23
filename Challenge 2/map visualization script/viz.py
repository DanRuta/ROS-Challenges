import os
import numpy as np
import cv2 as cv

MAP_FILE_NAME = "map_not_explored.txt"
# MAP_FILE_NAME = "map_half_done.txt"

def main():

    with open(MAP_FILE_NAME, "r") as file:

        lines = file.read().split("\n")

        HEIGHT = 1056
        WIDTH = 1216

        UPDATE_BOUNDS = False
        firstX = 0
        firstY = 0
        endX = 0
        endY = 0

        if not UPDATE_BOUNDS:
            firstX = 226
            firstY = 167
            endX = 847
            endY = 795

        img = cv.UMat(np.array(np.zeros((HEIGHT,WIDTH,3), np.uint8)))

        for r in range(HEIGHT):
            for c in range(WIDTH):

                mapVal = float(lines[r * WIDTH + c])

                if mapVal>=0:
                    if UPDATE_BOUNDS and firstX==0 and firstY==0 and mapVal>=0:
                        firstX = c
                        firstY = r

                    firstX = min(firstX, c)
                    firstY = min(firstY, r)

                    val = int(float(lines[r * WIDTH + c]) * 1.55) + 100
                    cv.circle(img, (c, r), 1, (val, val, val), thickness=-1, lineType=cv.FILLED)

                    if UPDATE_BOUNDS:
                        endX = c
                        endY = r

        cv.circle(img, (firstX, firstY), 5, (100, 200, 100), thickness=-1, lineType=cv.FILLED)
        cv.circle(img, (endX, endY), 5, (200, 100, 100), thickness=-1, lineType=cv.FILLED)


        # cv.imshow("Frame", img)
        # while True:
        #     if cv.waitKey(1) & 0xFF == ord('q'):
        #         break


        cv.imwrite("{}_frame.png".format(MAP_FILE_NAME[0:len(MAP_FILE_NAME)-4]), img)
        cv.destroyAllWindows()


        totalArea = (endX-firstX) * (endY-firstY)
        totalFound = 0

        print("firstX: {}".format(firstX))
        print("firstY: {}".format(firstY))
        print("endX: {}".format(endX))
        print("endY: {}".format(endY))

        for r in range(endY-firstY):
            for c in range(endX-firstX):

                mapVal = float(lines[(r+firstY) * WIDTH + (c + firstX)])

                if mapVal != -1:
                    totalFound += 1

        # for r in range(HEIGHT):
        #     for c in range(WIDTH):
        #         if r > firstY and r < endY and c > firstX and c < endX:
        #             mapVal = float(lines[r * WIDTH + c])
        #             if mapVal:
        #                 totalFound += 1




        print("totalFound: {}".format(totalFound))
        print("totalArea: {}".format(totalArea))
        print("Found: {}%".format(round(totalFound/totalArea*100 * 100)/100))







if __name__ == "__main__":
    main()