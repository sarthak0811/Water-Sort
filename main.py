from image_process import colour_array
from water_sort import *

# image_path="Test_Cases/test_625.PNG"
# image_path="Test_Cases/test_627.jpeg"
# image_path="Test_Cases/test_630.jpeg"
# image_path="Test_Cases/test_631.jpeg"
# image_path="Test_Cases/test_633.jpeg"
# image_path="Test_Cases/test_634.jpeg"
# image_path="Test_Cases/test_637.jpeg"
# image_path="Test_Cases/test_648.jpeg"
# image_path="Test_Cases/test_649.jpeg"
            
# empty_tubes=2

image_path=str(input("Enter the path of the image: "))
empty_tubes=int(input("Enter the number of empty tubes: "))

initial_state=colour_array(image_path,empty_tubes)
path=best_first_search(initial_state)
moves(path)