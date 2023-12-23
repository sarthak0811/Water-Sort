import numpy as np
import cv2

def find_color(image):
    unique_colors=[]
    k=0.2
    j= int(image.shape[1]*0.5)
    while k<1:
            i=int(k*image.shape[0])
            # Get the pixel's color
            color = tuple(image[i, j])
            unique_colors.append(color)
            k+=0.2

    return unique_colors

def similar_color(a,b):
    a = np.array(a, dtype=np.int16)
    b = np.array(b, dtype=np.int16)
    if np.all(np.abs(a - b) < 18):
        return True
    return False


def colour_array(path,empty_tubes):
    # Load the image
    image_path = path
    # crop the top and bottom 20% of the image and save it
    image = cv2.imread(image_path)
    image = image[int(image.shape[0]*0.25):int(image.shape[0]*0.8), 0:image.shape[1]]

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image
    _, thresh = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)

    # Find the contours
    contours, _ = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # fine the mean size of the contours
    mean_size = 0
    for cnt in contours:
        mean_size += cv2.contourArea(cnt)
    mean_size /= len(contours) 

    contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 0.8*mean_size]
    # Draw the contours
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    # find the colours in each contour in image. take the top left contour as the first and bottom right as last
    colours = []
    for cnt in contours[-1:(empty_tubes-1):-1]:
        x, y, w, h = cv2.boundingRect(cnt)
        cropped = image[y:y+h, x:x+w]
        arr=find_color(cropped)
        colours.append(arr)


    arr = [item for sublist in colours for item in sublist]
    arr1=[arr[0]]
    for x in arr:
        for y in arr1:
            if not similar_color(x,y):
                continue
            else:
                break
        else:
            arr1.append(x)

    del arr
    
    for i in range(len(colours)):
        for j in range(len(colours[i])):
            for k in range(len(arr1)):
                if similar_color(colours[i][j],arr1[k]):
                    colours[i][j]=str(k)
                    break
    
    for i in range(empty_tubes):
        colours.append(["","","",""])

    return colours