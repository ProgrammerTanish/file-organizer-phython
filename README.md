# File Organizer Python

**💼 Hire me: I build practical Python automation tools to save time and solve real problems.**

A Python tool that automatically organizes files into folders by type, with logging, safety checks, and support for both relative and absolute paths—perfect for automating file management efficiently.

---

## Table of Contents
- [Why This Project Exists](#why-this-project-exists)
- [Features](#features)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [License](#license)

---

## Why This Project Exists

Cluttered folders can slow down work and make finding files frustrating. This script provides a fast, reliable, and automated way to organize your files into categorized folders, keeping your system neat while maintaining safety and logging.

---

## Features

- Organizes files into folders based on file type (Documents, Images, Music, etc.)
- Supports both absolute and relative paths
- Prevents overwriting existing files
- Logs all actions for traceability
- Easy to use from the command line

---

## How It Works

1. Provide a folder path to the script.
2. The script scans all files in the folder.
3. Files are sorted and moved into type-specific folders.
4. All actions are logged in a separate log file for review.

---

## Installation

1. Make sure you have **Python 3.x** installed.
2. Clone this repository:

```bash
git clone https://github.com/ProgrammerTanish/file-organizer-python.git
```
3.Navigate into the project directory:

```
cd file-organizer-python
```

(No external dependencies are required.)

## Usage

You can run the script from the command line (CLI) as follows:
```
python organizer.py /path/to/your/folder
```

For the current directory, you can use:
```
python organizer.py .
```

For relative paths:
```
python organizer.py ../Downloads
```
After running, check your folder: files will be neatly organized, and a log file will track all actions.

## Example
Before running the script:

Downloads/
- image.png
- song.mp3
- doc.pdf


After running the script:

Downloads/
- Images/image.png
- Music/song.mp3
- Documents/doc.pdf
- log.txt
# License

This project is licensed under the MIT License - see the LICENSE file for details.
