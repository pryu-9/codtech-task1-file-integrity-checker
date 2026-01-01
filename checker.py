import hashlib
import os

print("🔍 FILE CHANGE DETECTOR - CODTECH TASK 1")
print("=" * 40)

def get_file_hash(filename):
    sha256 = hashlib.sha256()
    try:
        with open(filename, 'rb') as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except:
        return None

# User input
filename = input("File name enter karo (test.txt): ")

if not os.path.exists(filename):
    print("❌ File nahi mili! test.txt banao pehle.")
else:
    current_hash = get_file_hash(filename)
    
    if os.path.exists("saved_hashes.txt"):
        with open("saved_hashes.txt", "r") as f:
            old_hash = f.read().strip()
        
        if current_hash == old_hash:
            print("🟢 ✅ FILE SAFE - No changes!")
        else:
            print("🔴 ⚠️ ALERT! File change detected!")
            print(f"Old hash: {old_hash}")
            print(f"New hash: {current_hash}")
    else:
        # First time - save hash
        with open("saved_hashes.txt", "w") as f:
            f.write(current_hash)
        print("✅ First hash saved in saved_hashes.txt")
        print("Ab test.txt edit karo aur dobara run karo!")
