import os  
import shutil  
import sys  
  
def copy_files_from_dir(src_dir, dest_dir):  
    for filename in os.listdir(src_dir):  
        if filename.endswith('.txt') or filename.endswith('.m3u'):  
            src_file = os.path.join(src_dir, filename)  
            dest_file = os.path.join(dest_dir, filename)  
              
            # Copy the file to the destination directory  
            shutil.copy2(src_file, dest_dir)  
            print(f"Copied {src_file} to {dest_dir}")  
  
if __name__ == "__main__":  
    if len(sys.argv) != 2:  
        print("Usage: python copy_files.py <private_repo_tv_directory>")  
        sys.exit(1)  
      
    private_repo_tv_dir = sys.argv[1]  
    current_dir = os.getcwd()  
      
    # Copy files from the tv directory in the private repo to the current directory  
    copy_files_from_dir(private_repo_tv_dir, current_dir)