# Water-Sort
Solving the Water Sort Problem using Python.<br>

The image_process.py file is for processing the screenshot of the famous WaterSort game. It returns an array of subarrays of colours, where each number (as a string) represents a unique colour and empty strings represent blank spaces.<br>
![WhatsApp Image 2023-12-23 at 20 34 10](https://github.com/sarthak0811/Water-Sort/assets/92429357/4437e372-2b72-497b-9a0b-7a4cc1416fb9)


The code requires 2 inputs: <br>
1) file path of the image <br> 
2) number of empty tubes at the beginning.<br>

The water_sort.py takes the above array as input. It uses best first search algorithm to find the best solution.<br>
The solution is printed in the format: "Move Tube 1 to Tube 3, Move Tube 4 to Tube 2" and so on.<br>

Some sample test cases have also been provided.
