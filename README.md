# EAD-XML-Conversion-Scripts-Cross-Platform

# Purpose
This guide documents the creation of encoding new finding aids using the EAD XML Conversion Script at the SWC/SCL.

# Rights Statement
The contents of this repository are the intellectual property of Micheal Stephenson, Sarah Stephenson, and the Southwest Collection/Special Collections Library. 




# EAD-XML-Conversion-Scripts-Cross-Platform

This repository is based on another repository called [EAD-XML-Conversion-Scripts](https://github.com/RWTTU/EAD-XML-Conversion-Scripts), which was originally written in PowerShell and was largely limited to windows Machines. The aim of this repository is to provide a cross-platform solution by rewriting the **NewEADXMLCreationScript** in Python.

The Python script has been compiled into an exe file using `pyinstaller`, making it executable on Windows machines without requiring a Python installation. However, the source files can be used on any platform with Python installed. The script can also be run without being compiled into a binary on any system running Python 3.8 or later.

# Installation

1. Download the exe file from the latest release on the [releases page](https://github.com/mrstephenson2142/EAD-XML-Conversion-Scripts-Cross-Platform/releases).
2. Extract the downloaded zip file to a desired location.

# Usage

1. Double-click `EAD-XML-Conversion-Scripts.exe` to execute the script.

# Compile the Executable from Source

## Requirements

- Tested on Python 3.8

## Steps

1.  Navigate to the directory that contains your Python script.  
`cd /path/to/your/script`

2. Install pyinstaller.  
`pip install pyinstaller`

3. Create a standalone executable file using pyinstaller.  
`pyinstaller --onefile your_script_name.py`

4. The executable file will be created in a dist directory in the same location as your script





