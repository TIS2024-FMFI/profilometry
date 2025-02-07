# Profilometry

Application for measuring using profilometry.

This application uses computer vision techniques to analyze and measure features from images, such as finding and visualizing specific line patterns.

## Features
- Line detection using advanced algorithms.
- Visualization of detected features.
- Compatibility with image folders for batch processing.

## Fixes
The following issues have been identified for improvement:
- **3D Model Background:** A background should be added to the 3D model visualization for better contrast and visibility.
- **Board Inclusion in 3D Model:** The scanning board should be added beneath the object in the 3D visualization to provide a solid base, ensuring the model is not displayed as hollow while keeping other areas clear.
- **Export Options for 3D Models:** Ensure exported 3D models include all necessary data for rendering in external applications and accurately associate the exported files with the corresponding object.
- **Calibration Improvements:** If the object is shifted in different scans, the calibration should account for this to ensure accurate measurements.
- **Exposition Control Toggle:** Add a switch button that allows the user to toggle between automatic and fixed exposition settings, enabling greater control over image brightness and consistency during scanning.
- **Exposition Adjustment Buttons:** Implement **+** and **-** buttons to allow manual exposition settings, giving users precise control over exposition levels during scanning.
- **Implementing a Stepper Motor:** Implement a Stepper Motor in the scan_profile function according to requirements catalog in *3.1.3 paragraph. The stepper motor will be controlled via a microcontroller, with movement commands sent through serial communication (e.g., using pyserial). Suggested implementation steps:
1. Initialize serial communication with the microcontroller – A communication object will be added to the Scanner class. 
2. Move the stepper motor before each scan – The scan_profile function will trigger a movement command.
3. Wait for movement completion – Using time.sleep() or waiting for confirmation from the microcontroller.
4. Capture an image – The existing scan_profile functionality will execute after movement is finished.
5. Repeat the process – The cycle continues until all scans are completed.


The following Python libraries are required:
- `opencv-python>=4.5.0`
- `numpy>=1.19.0`
- `Pillow>=8.0.0`
- `matplotlib>=3.3.0`
- `numpy-stl>=2.16.0`
- `trimesh>=3.9.0`
- `pygltflib>=1.2.0`
- `scipy>=0.9.0`
- `pygrabber`

These are listed in the `requirements.txt` file and will be automatically installed when running the application.

## Getting Started
### Prerequisites
Ensure you have Python 3.6 or higher installed on your system.

### Running the Application
1. Clone the repository or download the source code.
2. Open a terminal and navigate to the directory containing `main.py`.
3. Run the following command to start the application:

   ```bash
   ./main.py
