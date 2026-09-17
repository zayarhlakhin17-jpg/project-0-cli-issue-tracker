from pathlib import Path

current = Path.cwd()
file_path = Path("practice.txt")

print("Current folder:", current)
print("File path:", file_path)
print("Absolute path:", file_path.resolve())
print("Exists:", file_path.exists())
print("Is file:", file_path.is_file())
