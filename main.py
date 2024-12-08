import argparse
import os


# def synchronization(source_folder, replica_folder, interval):

# Python program to explain shutil.copy() method 

# importing shutil module 
# import shutil 

# source = "/home/fortytwo/Desktop/source/main.py"
# destination ="/home/fortytwo/Desktop/replica/main2.py"

# # Copy the content of 
# # source to destination 
# dest = shutil.copy(source, destination) 

# # Print path of newly 
# # created file 
# print("Destination path:", dest) 

# Python program to explain shutil.copy2() method 
	
# importing os module 
import os 

# importing shutil module 
import shutil 

# path 
path = '/home/fortytwo/Desktop/source/'

# List files and directories 
# in '/home/User/Documents' 


# Source path 
source = "/home/fortytwo/Desktop/source/"

# Print the metadeta 
# of source file 
# metadata = os.stat(source) 
# print("Metadata:", metadata, "\n") 

# Destination path 
destination = "/home/fortytwo/Desktop/replica/"

print("Before copying file:") 
print(os.listdir(destination)) 
for root, dirs, files in os.walk(source):
    # print(f"root {root}")
    # print(f"dirs {dirs}")
    # print(f"files {files}")
    for dir in dirs:
        src_dir = os.path.join(root, dir)
        rel_path = os.path.relpath(src_dir, source)
        dest_dir = os.path.join(destination, rel_path)
        os.makedirs(dest_dir, exist_ok = True)
    for file in files:
        src_file = os.path.join(root, file)
        # print(f"print src {src_file}")
        rel_path = os.path.relpath(src_file, source)
        # print(rel_path)
        dest_file = os.path.join(destination, rel_path)

        os.makedirs(os.path.dirname(dest_file), exist_ok=True)
        shutil.copy2(src_file,dest_file)
    
    for root, dirs, files in os.walk(destination, topdown=False):
        for file in files:
            replica_file = os.path.join(root, file)
            rel_path = os.path.relpath(replica_file, destination)
            source_file = os.path.join(source, rel_path)
            if not os.path.exists(source_file):
                os.remove(replica_file)

        for dir in dirs:
            replica_dir = os.path.join(root, dir)
            rel_path = os.path.relpath(replica_dir, destination)
            source_dir = os.path.join(source, rel_path)
            if not os.path.exists(source_dir):
                shutil.rmtree(replica_dir)
print("After copying file source:") 
print(os.listdir(source))
print("After copying file destin:") 
print(os.listdir(destination))
        # shutil.copytree()
# # Copy the content of 
# # source to destination 
# dest = shutil.copytree(source, destination) 

# # List files and directories 
# # in "/home / User / Documents" 
# print("After copying file:") 
# print(os.listdir(path)) 

# # Print the metadata 
# # of the destination file 
# # matadata = os.stat(destination) 
# # print("Metadata:", metadata) 

# # Print path of newly 
# # created file 
# print("Destination path:", dest) 


# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--source_folder", help = "pls enter --s and than name of source folder", action="store")
#     parser.add_argument("--replica_folder", help = "pls enter --r and than name of replica folder", action="store")
#     parser.add_argument("--interval", help = "pls enter --i and than interval time(in second)", type=int, action="store")
#     args = parser.parse_args()
# # source_folder = args.source_folder
# # replica_folder = args.replica_folder
# # interval = args.interval

# if __name__ == "__main__":
#     main()