from pathlib import Path
import shutil

# Get current working directory
basepath = Path(__file__).resolve()

# Define the target path
target_path = Path(rTARGET_PATH)

# iterdir() scans the folder
for file in target_path.iterdir():
  if file.is_file():
    # Images
    if file.suffix in (".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"):
      folder = "images"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

    # Videos
    elif file.suffix in (".mp4", ".mov", ".avi", ".mkv", ".wmv", ".flv"):
      folder = "videos"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

    # Documents
    elif file.suffix in (".pdf", ".docx", ".doc", ".pptx", ".ppt", ".xlsx", ".xls", ".txt"):
      folder = "documents"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

    # Data Files
    elif file.suffix in (".csv", ".json", ".xml", ".sql"):
      folder = "data"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

    # Audio
    elif file.suffix in (".mp3", ".wav", ".aac", ".flac", ".ogg"):
      folder = "audio"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

    # Code / Scripts
    elif file.suffix in (".py", ".js", ".html", ".css", ".ts", ".java", ".cpp", ".c"):
      folder = "code"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

    # Everything else
    else:
      folder = "others"
      destination = target_path / folder
      filename = destination / file.name
      move_scanned_files(destination, file, filename)

# Handle scanned files
def move_scanned_files(destination = None, file = None, filename = None):
  destination.mkdir(exist_ok=True)
  try:
    # moves the file
    shutil.move(file, filename)
  except PermissionError:
    print(f"Permission denied, skipping: {file.name}")