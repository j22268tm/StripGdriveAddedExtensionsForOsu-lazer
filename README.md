# StripGdriveAddedExtensionsForOsu-lazer

## Overview

When downloading files from Google Drive as ZIPs, it has a *"helpful"* habit of guessing MIME types and slapping extensions onto files that never asked for them.\
This Python script hunts down these unwanted extensions in your directory (and subdirectories), stripping them off to restore files to their glorious extension-free selves.

## This script was born out of a personal troubleshooting

1. Backed up `osu!(lazer)`’s `files` dir + `client.realm` to Google Drive.  
2. Downloaded them on a new PC via Google Drive Web.  
3. Launched `osu!(lazer)`—music silent, backgrounds gone. Error logs screamed: _"MP3/PNG not found!"_  
4. After investigation:  
   🔍 **Culprit**: Google Drive had "generously" appended extensions like `.mp3`/`.png` to extensionless files.  
   🤖 **Google Drive**<_"No extension? No problem! I peeked at the binary, guessed from magic numbers, and added one for you! 😊👌"_  
5. Script executed. Files restored. `osu!(lazer)` lived happily ever after. The end. 🦸‍♂️

## Features

- Recursively scans directories/subdirectories.  
- Detects and **murders** unwanted extensions (anything after the last `.`).  
  - `annoying.txt` → `annoying`  
  - `archive.tar.gz` → `archive.tar` (only last extension removed)  
- **Dry-run mode**: Previews the carnage before committing.  
- Skips renaming if a filename conflict occurs (no overwriting!).

## Usage

1. **Prerequisite**: Python 3.x installed.  
2. **Download**: Clone repo or grab the script (`stripExtensions.py`).  
3. **Run**:  
   ```bash
   python stripExtensions.py
   ```
   - **Step 1**: Enter the target directory’s full path (e.g., `C:\Users\You\AppData\Roaming\osu\files`).  
   - **Step 2**: Dry-run first? **YES** (seriously, do this unless you love chaos).  
   - **Step 3**: Review dry-run results. Run again → choose **real execution** if satisfied.  

⚠️ **WARNING**: This script **permanently renames files**. Backup your data or risk eternal regret. You’ve been warned! ⚠️

## Important Notes

- Targets the **last dot + extension** only. Triple-check your directory first!  
- Built for `osu!(lazer)`’s `files` dir, but may work elsewhere (no promises though).  

## License

[MIT License](LICENSE) - Use at your own risk.
