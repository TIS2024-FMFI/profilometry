import os
from tkinter import filedialog
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

        self.save_last_project()

        # Print details of the created project
        print(f"Project '{self.project_name}' created successfully at '{self.project_dir}'.")
        print("Subdirectories and files created:")
        for directory in required_dirs:
            print(f" - {directory}/")

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
        allowed_files = {'scans', 'calibration', 'movement_parameters'}
        current_files = set(os.listdir(self.project_dir))
        return current_files - allowed_files

    def create_scan_folders(self, view_name):
        """Create subfolders for each scan (raw and processed)."""
        view_dir = os.path.join(self.project_dir, 'scans', view_name)
        raw_dir = os.path.join(view_dir, 'raw')
        processed_dir = os.path.join(view_dir, 'processed')
        os.makedirs(raw_dir, exist_ok=True)
        os.makedirs(processed_dir, exist_ok=True)


