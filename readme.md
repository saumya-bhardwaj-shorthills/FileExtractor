## Features

- Extract plain text from a PDF.
- Extract Images and store them in directory
- Extract URLS
- Extract tables from a PDF and save them as CSV files.
- Extract all metadata of files
- Save extracted tables to an SQL database.


## Prerequisites

Ensure you have the following installed:

- Python 3.6 or higher
- `pip` (Python package installer)

## Dependencies

The project requires several Python libraries to function properly. These can be installed via `requirements.txt`.

- `PyPDF2`: To extract text from PDF files.
- `pandas`: To manipulate data and tables.
- `camelot-py[cv]`: To extract tables from PDF files.
- `sqlite3`: To store table data in a SQL database.
- `opencv-python`: Required by Camelot for image processing.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/saumya-bhardwaj-shorthills/FileExtractor.git
   cd FileExtractor
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   If `opencv-python` is not already installed, you can install it manually using:

   ```bash
   pip install opencv-python
   ```

   You may also need `ghostscript` for handling PDFs with embedded images or complex layouts. Install it using the system package manager, for example:

   - On Ubuntu:

     ```bash
     sudo apt-get install ghostscript
     ```

   - On MacOS:

     ```bash
     brew install ghostscript
     ```

## Usage

### Extracting Text and Tables from a PDF

1. Place the PDF file you want to extract data from in the `Test-resources` directory. [Create a directory]
2. Modify the path to your PDF file in the `main.py` file.
3. Run the main script:

   ```bash
   python main.py
   ```

### Example

To extract tables from `sample.pdf` and store them in an SQL database:

1. Place `sample.pdf` in the `Test-resource/` directory.[Create one]
2. Run the script:

   ```bash
   python main.py
   ```

   This will:
   - Extract tables from the PDF.
   - Store the tables in a local SQLite database.

### Storage Options

You can save extracted tables as:
- CSV Files
- SQL Database (SQLite)



