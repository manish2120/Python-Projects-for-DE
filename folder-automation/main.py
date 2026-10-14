from pathlib import Path
import shutil

# Define the target path
target_path = Path(r'TARGET_PATH')

# Handle scanned files
def move_scanned_files(file, folder):
  destination = target_path / folder
  destination.mkdir(exist_ok=True)
  filename = destination / file.name
  try:
    # Moves the file into the destination folder
    shutil.move(file, filename)
    print(f"Moved: {file.name} --> {folder}/")
  except PermissionError:
    print(f"Permission denied, skipping: {file.name}")

# Scan the target path
for file in target_path.iterdir():
  if file.is_file():

    # Images
    if file.suffix in (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"):
      move_scanned_files(file, "images")

    # Videos
    elif file.suffix in (".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"):
      move_scanned_files(file, "videos")

    # Documents
    elif file.suffix in (".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".txt"):
      move_scanned_files(file, "documents")

    # Data Files
    elif file.suffix in (".csv", ".json", ".xml", ".sql"):
      move_scanned_files(file, "data")

    # Audio
    elif file.suffix in (".mp3", ".wav", ".aac", ".flac", ".ogg"):
      move_scanned_files(file, "audio")

    # Code
    elif file.suffix in (".py", ".js", ".html", ".css", ".ts", ".java", ".cpp", ".c"):
      move_scanned_files(file, "code")

    # Others
    else:
      move_scanned_files(file, "others")