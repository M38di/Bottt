import zipfile
import os

def extract_zip(zip_file_path, extract_to='.'):
    """Extracts a ZIP file to the specified directory.

    Args:
        zip_file_path (str): The path to the zip file.
        extract_to (str): The directory to extract to. Default is the current directory.
    """
    try:
        # Check if the file exists
        if not os.path.exists(zip_file_path):
            print(f"Error: The file {zip_file_path} does not exist.")
            return
        
        # Open the zip file
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Extract all contents into the specified directory
            zip_ref.extractall(extract_to)
            print(f"Successfully extracted {zip_file_path} to {extract_to}")
    
    except zipfile.BadZipFile:
        print(f"Error: {zip_file_path} is not a valid zip file.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    zip_file = 'iconscout_downloader-main.zip'  # Replace with your zip file
    output_dir = '/'  # Replace with your desired extraction directory
    extract_zip(zip_file, output_dir)
