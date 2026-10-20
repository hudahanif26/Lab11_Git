# Storage Estimator Program
def calculate_storage(files, size_per_file_gb):
    total_gb = files * size_per_file_gb
    return total_gb

if __name__ == "__main__":
    print("--- Simple Storage Estimator ---")
    num_files = 10
    file_size = 2.5
    total = calculate_storage(num_files, file_size)
    print(f"Total estimated storage for {num_files} files: {total} GB")
    print(f"In Megabytes: {total * 1024} MB")

print("meow")