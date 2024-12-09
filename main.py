import argparse
import os
import shutil
import time

def synchronisation(source, destination):
    for root, dirs, files in os.walk(source):
        for dir in dirs:
            src_dir = os.path.join(root, dir)
            rel_path = os.path.relpath(src_dir, source)
            dest_dir = os.path.join(destination, rel_path)
            os.makedirs(dest_dir, exist_ok=True)

        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, source)
            dest_file = os.path.join(destination, rel_path)
            os.makedirs(os.path.dirname(dest_file), exist_ok=True) 
            shutil.copy2(src_file, dest_file)

    for root, dirs, files in os.walk(destination, topdown=False):
        for file in files:
            replica_file = os.path.join(root, file)
            rel_path = os.path.relpath(replica_file, destination)
            source_file = os.path.join(source, rel_path)
            if not os.path.exists(source_file):
                print(f"Removing file: {replica_file}")
                os.remove(replica_file)

        for dir in dirs:
            replica_dir = os.path.join(root, dir)
            rel_path = os.path.relpath(replica_dir, destination)
            source_dir = os.path.join(source, rel_path)
            if not os.path.exists(source_dir):
                print(f"Removing directory: {replica_dir}")
                shutil.rmtree(replica_dir)

def main():
    parser = argparse.ArgumentParser(description="Synchronize two folders (source -> replica).")
    parser.add_argument("--source_folder", required=True, help="Path to the source folder.")
    parser.add_argument("--replica_folder", required=True, help="Path to the replica folder.")
    parser.add_argument("--interval", type=int, required=True, help="Synchronization interval in seconds.")
    args = parser.parse_args()

    source = args.source_folder
    destination = args.replica_folder
    interval = args.interval

    if not os.path.exists(source):
        print(f"Error: Source folder '{source}' does not exist.")
        return
    if not os.path.exists(destination):
        print(f"Replica folder '{destination}' does not exist. Creating it.")
        os.makedirs(destination)

    if interval <= 0:
        print("Error: Interval must be a positive number.")
        return

    print(f"Starting synchronization: {source} -> {destination}")
    print(f"Synchronization interval: {interval} seconds")
    
    try:
        while True:
            synchronisation(source, destination)
            print("Synchronization completed. Waiting for next cycle...")
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\nSynchronization interrupted by user.")

if __name__ == "__main__":
    main()
