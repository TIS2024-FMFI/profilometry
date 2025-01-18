import os
import cv2
import numpy as np
from PIL import Image
from datetime import datetime
from tkinter import filedialog
import json
from config import LAST_PROJECT_FILE

class Project:
    def __init__(self, project_name, base_dir=None):
        self.project_name = project_name
        self.project_dir = None
        self.set_dir(base_dir)

    def set_dir(self, base_dir=None):
        if base_dir is None:
            base_dir = filedialog.askdirectory(title="Select Folder")

            if not base_dir and self.project_dir is None:
                base_dir = os.path.normpath(os.getcwd())
                self.project_dir = os.path.join(base_dir, self.project_name)
            elif not base_dir:
                return

        self.project_dir = os.path.join(base_dir, self.project_name)

    def save_last_project(self):
        """Save the current project as the last opened project."""
        summary_path = LAST_PROJECT_FILE['name']

        normalized_project_dir = os.path.normpath(self.project_dir)

        with open(summary_path, 'w') as file:
            file.write(f"{normalized_project_dir}\n{self.project_name}")

    def create_project(self):
        """Create all required directories and files for the project."""
        required_dirs = [
            'scans',
            'calibration',
            'movement_parameters'
        ]

        for directory in required_dirs:
            dir_path = os.path.join(self.project_dir, directory)
            os.makedirs(dir_path, exist_ok=True)

        summary_file = os.path.join(self.project_dir, 'project_summary.txt')
        if not os.path.exists(summary_file):
            open(summary_file, 'w').close()

        self.save_last_project()

        # Print details of the created project
        print(f"Project '{self.project_name}' created successfully at '{self.project_dir}'.")
        print("Subdirectories and files created:")
        for directory in required_dirs:
            print(f" - {directory}/")
        print(f" - project_summary.txt")

    def open_project(self):
        """Validate the project structure and create missing components."""
        if not os.path.exists(self.project_dir):
            raise FileNotFoundError(f"Project directory {self.project_dir} does not exist.")

        # Check and create required directories and files
        self.create_project()

        # extra_files = self._check_for_extra_files()
        # if extra_files:
        #     raise ValueError(f"Unexpected files found in project: {extra_files}")

    def _check_for_extra_files(self):
        """Check for unexpected files in the main project directory."""
        allowed_files = {'scans', 'calibration', 'movement_parameters', 'project_summary.txt'}
        current_files = set(os.listdir(self.project_dir))
        return current_files - allowed_files

    def create_scan_folders(self, view_name):
        """Create subfolders for each scan (raw and processed)."""
        view_dir = os.path.join(self.project_dir, 'scans', view_name)
        raw_dir = os.path.join(view_dir, 'raw')
        processed_dir = os.path.join(view_dir, 'processed')
        os.makedirs(raw_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)

    def create_calibration_folders(self, view_name):
        """Create subfolders for each calibration."""
        calibration_dir = os.path.join(self.project_dir, 'calibration', view_name)
        raw_dir = os.path.join(calibration_dir, 'raw')
        processed_dir = os.path.join(calibration_dir, 'processed')
        os.makedirs(raw_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)
        calibration_data_file = os.path.join(calibration_dir, 'calibration_data.txt')
        if not os.path.exists(calibration_data_file):
            open(calibration_data_file, 'w').close()

    def save_scan(self, view_name, scan_image, is_processed=False):
        """Save scan image in the appropriate directory."""
        self.create_scan_folders(view_name)
        folder = 'processed' if is_processed else 'raw'
        target_dir = os.path.join(self.project_dir, 'scans', view_name, folder)
        scan_count = len(os.listdir(target_dir)) + 1
        scan_path = os.path.join(target_dir, f"scan{scan_count}.png")
        scan_image.save(scan_path)

    def save_calibration(self, view_name, calibration_image, is_processed=False):
        """Save calibration image in the appropriate directory."""
        self.create_calibration_folders(view_name)
        folder = 'processed' if is_processed else 'raw'
        target_dir = os.path.join(self.project_dir, 'calibration', view_name, folder)
        cal_count = len(os.listdir(target_dir)) + 1
        cal_path = os.path.join(target_dir, f"cal{cal_count}_scan{cal_count}.png")
        calibration_image.save(cal_path)
    
    def get_raw_path(self, view_name):
        """Get the path to the raw folder for a specific scan view."""
        return os.path.join(self.project_dir, 'scans', view_name, 'raw')
    
    def get_processed_path(self, view_name):
        """Get the path to the processed folder for a specific scan view."""
        return os.path.join(self.project_dir, 'scans', view_name, 'processed')

    def save_movement_parameters(self, view_name, movement_data):
        """Save movement parameters in a text file."""
        movement_dir = os.path.join(self.project_dir, 'movement_parameters')
        os.makedirs(movement_dir, exist_ok=True)
        movement_file = os.path.join(movement_dir, f"movement_{view_name}.txt")
        with open(movement_file, 'w') as file:
            file.write(movement_data)

    def update_project_summary(self):
        """Update the project summary file."""
        summary_path = os.path.join(self.project_dir, 'project_summary.txt')
        with open(summary_path, 'a') as file:
            file.write(f"Project Name: {self.project_name}\n")
            file.write(f"Scans saved: {len(os.listdir(os.path.join(self.project_dir, 'scans')))}\n")
            file.write(f"Calibration data saved in: {os.path.join(self.project_dir, 'calibration')}\n")
            file.write(f"Movement parameters saved in: {os.path.join(self.project_dir, 'movement_parameters')}\n")
            file.write("\n")
