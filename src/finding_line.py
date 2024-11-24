import numpy as np
import cv2
import os

class LineDetection:
    """To apply a new algorithm, set `algorithm = 1` in the `apply_to_folder` method. 
    `algorithm = 2` refers to the old algorithm.
    To process an entire folder of images, set the `path` where the images are located 
    and the `out_path` where the processed images should be saved. Ensure the output 
    folder exists before running the program."""
    def __init__(self, path, out_path, constant, display=False, extension='jpg'):
        # Initialize parameters
        self.path = path
        self.out_path = out_path
        self.display = display
        self.extension = extension
        self.constant = constant
        self.shift_count = 1
        self.all_points = []

    def find_line_alg1(self, img):
        # Detect the line using Algorithm 1
        if isinstance(img, str):
            img = cv2.imread(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        height, width = img.shape
        largest_points = []
        first_point = 0

        # Find highest pixels in each column
        for col in range(width):
            column_pixels = img[:, col]
            if max(column_pixels) > 80:
                if first_point == 0:
                    first_point = np.argmax(column_pixels)
                largest_points.append((col, np.argmax(column_pixels)))

        new_img = np.zeros((height, width, 3), dtype=np.uint8)

        reference_points = []
        avg_reference = 0
        object_points = []
        for point in largest_points:
            if abs(point[1] - first_point) < 30:
                reference_points.append(point)
                avg_reference += point[1]
            else:
                if point[1] > first_point:
                    object_points.append(point)
        
        # Draw reference line
        cv2.line(new_img, (0, avg_reference // len(reference_points)), 
                 (img.shape[1], avg_reference // len(reference_points)), 
                 (200, 120, 100), 3)

        # Draw object points
        for point in object_points:
            cv2.circle(new_img, (point[0], point[1]), radius=2, color=(0, 0, 255), thickness=-1)

        # Calculate and store points
        new_points = [(point[0], point[1] * self.shift_count * self.constant, 
                       point[1] - avg_reference // len(reference_points)) 
                      for point in object_points]

        self.all_points.append(np.array(new_points, np.int32))
        self.shift_count += 1
        return new_img

    def display_image(self, path):
        # Display processed image
        img = self.find_line_alg1(path)
        cv2.imshow("window", img)
        cv2.waitKey(0)

    def apply_to_image(self, image_path):
        # Apply the algorithm to a single image
        components = image_path.split('\\')
        img = self.find_line_alg1(image_path)
        cv2.imwrite(components[0] + '_alg\\' + components[1], img)

    def apply_to_folder(self):
        # Apply the algorithm to all images in the folder
        self.all_points = []
        for filename in os.listdir(self.path):
            if filename.endswith("." + self.extension):
                file_path = os.path.join(self.path, filename)
                try:
                    output_file = os.path.join(self.out_path, filename)
                    img = self.find_line_alg1(file_path)
                    
                    if self.display:
                        cv2.imshow("window", img)
                        cv2.waitKey(0)
                    elif output_file != "":
                        #print(output_file)
                        cv2.imwrite(output_file, img)
                except:
                    pass
                
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