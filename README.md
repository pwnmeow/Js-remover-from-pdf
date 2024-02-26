# JavaScript Remover from PDF

This Python script is designed to enhance the security of your PDF files by removing JavaScript code that could potentially be harmful or execute unwanted actions when the PDF is opened. It's a straightforward tool for users who need to clean their PDFs from embedded JavaScript, ensuring safer document sharing and storage.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you begin, ensure you have Python installed on your system. This script has been tested with Python 3.x. You will also need `PyPDF2`, a Python library for reading and writing PDF files.

You can install `PyPDF2` using pip:

```bash
pip install PyPDF2
```

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/pwnmeow/Js-remover-from-pdf.git
```

2. Navigate to the cloned repository:

```bash
cd Js-remover-from-pdf
```

3. Run the script with the path to the PDF file you wish to clean:

```bash
python js_remover.py <path_to_your_pdf> <output_pdf>
```
![image](https://github.com/pwnmeow/Js-remover-from-pdf/assets/10785234/8ce70047-76d3-4f75-86ce-d0f8a76aa937)

Replace `<path_to_your_pdf>` with the actual path to the PDF file you want to process.

## How It Works

The script loads the PDF file specified by the user, scans through its objects, and removes any objects containing JavaScript. It then saves the cleaned version of the PDF without altering the original content, layout, or formatting, ensuring that the document remains intact minus the potentially harmful scripts.


## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- Thanks to the `PyPDF2` library for making PDF manipulation possible in Python.
- This project is inspired by the need for safer PDF documents in an era where document-based malware is a growing concern.

---

