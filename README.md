# Water-Sort
Solving the problem Water Sort Problem using Python.<br>

The image_process.py file is for processing the screenshot of the famous WaterSort game. It returns an array of subarrays of colours, where each number (as a string) represents a unique colour and empty strings represent blank spaces.<br>

![IMG_9419](https://github.com/sarthak0811/Water-Sort/assets/92429357/f938add5-79a5-4e80-afc0-79949b7c24a9)


The code requires 2 inputs, file path of the image and number of empty tubes at the beginning.<br>

The water_sort.py takes the the above array as input. It uses best first search to find the path.<br>
The path is printed in the format: "Move Tube 1 to Tube 3, Move Tube 4 to Tube 2" and so on.<br>

Some sample test cases have also been provided.
