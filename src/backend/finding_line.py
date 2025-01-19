import numpy as np
import cv2
import os
from config import LINE_DETECTION
from tkinter import messagebox

class LineDetection:
    """To apply a new algorithm, set in the `apply_to_folder` method. 
    To process an entire folder of images, set the `path` where the images are located 
    and the `out_path` where the processed images should be saved. Ensure the output 
    folder exists before running the program."""
    def __init__(self, path, out_path, constant, extension='jpg', raw_path = '/scans/raw/', processed_path = '/scans/processed/'):
        # Initialize parameters
        self.project_path = path
        self.raw_path = raw_path
        self.procecced_path = processed_path
        self.path = path + self.raw_path
        self.out_path = out_path
        self.extension = extension
        self.constant = constant
        self.shift_count = 1
        self.all_points = []
        self.all_points2 = []
        self.all_points2 = []

    def find_line_alg1(self, img, scanning = False):
        # Detect the line using Algorithm 1
        if isinstance(img, str):
            img = cv2.imread(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        height, width = img.shape
        largest_points = []
        first_point = 0

        high_exp = False
        answer = True

        # Find highest pixels in each column
        for col in range(width):
            column_pixels = img[:, col]
            
            if np.max(column_pixels) > LINE_DETECTION['significant_threshold_pixel_max'] and not high_exp and scanning:
                answer = messagebox.askyesno("Warning", "The laser intensity is too high. Please adjust exposition. Do you want to save the image?")
                high_exp = True
            
            if answer:
                # Check if the column has significant intensity
                if np.max(column_pixels) < LINE_DETECTION['significant_threshold_pixel']:
                    continue  # Skip columns without a significant laser signal
                
                # Mask to focus on pixels above the threshold
                laser_mask = column_pixels > LINE_DETECTION['significant_threshold_pixel']
                intensity_sum = np.sum(column_pixels[laser_mask])
                
                if intensity_sum == 0:
                    continue  # Skip if no significant points after masking
                
                # Calculate weighted centroid of laser
                indices = np.arange(height)[laser_mask]
                weighted_sum = np.sum(indices * column_pixels[laser_mask])
                centroid = int(weighted_sum / intensity_sum)

                if first_point == 0:
                    first_point = centroid
                largest_points.append((col, centroid))

        if answer:
            new_img = np.zeros((height, width, 3), dtype=np.uint8)

            reference_points = []
            avg_reference = 0
            object_points = []
            for point in largest_points:
                if abs(point[1] - first_point) < LINE_DETECTION['largest_points_threshold']:
                    reference_points.append(point)
                    avg_reference += point[1]
                else:
                    if point[1] > first_point:
                        object_points.append(point)
            
            # Draw reference line
            if len(reference_points) > 0:
                cv2.line(new_img, (0, avg_reference // len(reference_points)), 
                        (img.shape[1], avg_reference // len(reference_points)), 
                        (200, 120, 100), 3)
        
            # Draw object points
            for point in object_points:
                cv2.circle(new_img, (point[0], point[1]), radius=2, color=(0, 0, 255), thickness=-1)

            # Calculate and store points
            new_points = [(int(point[0]), int(point[1] * self.shift_count * self.constant), 
                        int(point[1] - avg_reference // len(reference_points))) 
                        for point in object_points]

            self.all_points.append(np.array(new_points, np.int32))
            
            for pnt in object_points:
                self.all_points2.append((pnt[0], pnt[1] * self.shift_count * self.constant, 
                                pnt[1] - avg_reference // len(reference_points)))
            
            self.shift_count += 1
            return new_img
        
        else:
            self.all_points = []
            self.all_points2 = []
            return None

    def display_image(self, path):
        # Display processed image
        img = self.find_line_alg1(path)
        cv2.imshow("window", img)
        cv2.waitKey(0)

    def apply_to_image(self, image_path, image, scanning = False):
        # Apply the algorithm to a single image
        
        img = self.find_line_alg1(image_path+ self.raw_path + image, scanning)
        if scanning:
            if img is not None:
                cv2.imwrite(image_path + self.procecced_path + image, img)
            else:
                os.remove(image_path+ self.raw_path + image)
        else:
            cv2.imwrite(image_path + self.procecced_path + image, img)

    def apply_to_folder(self):
        # Apply the algorithm to all images in the folder
        self.all_points = []
        self.all_points2 = []
        for filename in os.listdir(self.path):
            if filename.endswith("." + self.extension):
                file_path = os.path.join(self.path, filename)
                try:
                    output_file = os.path.join(self.out_path, filename)
                    img = self.find_line_alg1(file_path)

                    if output_file != "":
                        #print(output_file)
                        cv2.imwrite(output_file, img)
                except:
                    pass
        
        self.write_points_to_file()
        #self.vykresli_vsetky_body()

    def display_all_points(self):
        # Display all detected points in one image
        combined_img = np.zeros((1080, 1920, 3), dtype=np.uint8)

        for points in self.all_points:
            for point in points:
                cv2.circle(combined_img, (point[0] - 400, int(point[1] * 0.01 + 400)), 
                           radius=2, color=(0, 255, 0), thickness=-1)
        
        cv2.imshow("All Points", combined_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def display_all_points2(self):
        # Display all detected points in one image
        combined_img = np.zeros((1080, 1920, 3), dtype=np.uint8)

        for points in self.all_points2:
            cv2.circle(combined_img, (points[0] - 400, int(points[1] * 0.01 + 400)), 
                           radius=2, color=(0, 255, 0), thickness=-1)
        
        cv2.imshow("All Points", combined_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def get_all_points(self):
        return self.all_points
    
    
    def write_points_to_file(self):
        with open(self.project_path+'/points.txt', mode = 'w') as file:
            for i in self.all_points2:
                print(f'{i[0]} {i[1]} {i[2]}', file = file)
    
    def write_points_to_file_app(self):
        try:
            with open(self.project_path+'/points.txt', mode = 'a') as file:
                for i in self.all_points2:
                    print(f'{i[0]} {i[1]} {i[2]}', file = file)
        except:
            pass