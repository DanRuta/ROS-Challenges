import os
import numpy as np
import cv2 as cv

def main():

    with open("map_not_explored.txt", "r") as file:
    # with open("map_half_done.txt", "r") as file:

        lines = file.read().split("\n")

        HEIGHT = 1056
        WIDTH = 1216

        firstX = 0
        firstY = 0
        endX = 0
        endY = 0

        img = cv.UMat(np.array(np.zeros((HEIGHT,WIDTH,3), np.uint8)))

        for r in range(HEIGHT):
            for c in range(WIDTH):

                mapVal = float(lines[r * WIDTH + c])

                if firstX==0 and firstY==0 and mapVal>=0:
                    firstX = c
                    firstY = r

                if mapVal>=0:
                    val = int(float(lines[r * WIDTH + c]) * 1.55) + 100
                    cv.circle(img, (c, r), 1, (val, val, val), thickness=-1, lineType=cv.FILLED)

                endX = c
                endY = r

        # cv.imshow("Frame", img)
        # while True:
        #     if cv.waitKey(1) & 0xFF == ord('q'):
        #         break


        cv.imwrite("frame.png", img)
        cv.destroyAllWindows()


        totalArea = endX-firstX * endY-firstY
        print(endX-firstX)
        print(endY-firstY)
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