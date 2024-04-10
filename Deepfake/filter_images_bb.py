# Filtering out images with bounding box areas greater than a certain threshold.

import os
import shutil

def calculate_area(box):
    x1, y1, x2, y2 = box
    return (x2 - x1) * (y2 - y1)

def parse_annotation_line(line):
    parts = line.strip().split()
    filename = parts[0]
    boxes = [list(map(float, parts[i:i+4])) for i in range(1, len(parts), 4)]
    return filename, boxes

def filter_and_save_images(input_folder, output_folder, threshold_area):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            annotation_file = os.path.join(input_folder, filename)
            image_file = os.path.splitext(annotation_file)[0] + ".jpg" 
            if os.path.exists(image_file):
                # Read annotation file
                with open(annotation_file, 'r') as f:
                    annotations = f.readlines()

                for annotation in annotations:
                    _, boxes = parse_annotation_line(annotation)
                    print(boxes)
                    total_area = sum([calculate_area(box) for box in boxes])
                    print(total_area)

                    if total_area > threshold_area:
                        output_image_file = os.path.join(output_folder, os.path.basename(image_file))
                        shutil.copy(image_file, output_image_file)
                        break  

input_folder = "C:/College/LY/Sem 8/RS_OEA/Deepfake detection/test"
output_folder = "C:/College/LY/Sem 8/RS_OEA/Deepfake detection/output"
threshold_area = 0.05 

filter_and_save_images(input_folder, output_folder, threshold_area)

print("Filtered images saved to:", output_folder)