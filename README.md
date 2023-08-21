# PyTex_CV
# CV Generator in Python encapsulated in a C Program

This project aims to create a command-line tool that generates a Curriculum Vitae (CV) in LaTex format from the given information and then converts it to a PDF using PDFLaTeX. The project was started on August 21, 2023, by tbimbato.

## Introduction

A Curriculum Vitae (CV) is an essential document used to showcase an individual's education, work experience, skills, and achievements. Creating a well-formatted CV can be a time-consuming task. This project combines the power of Python for data processing and C for encapsulation and execution, providing an efficient way to generate and compile CVs in LaTex format.

## Features

- Accepts input data for personal information, education, work experience, skills, and achievements.
- Generates a LaTex document template based on the provided information.
- Converts the generated LaTex document to a PDF using PDFLaTeX.

## Prerequisites

- C compiler (such as GCC)
- Python 3.x
- PDFLaTeX (TeX Live distribution recommended)

## Project Structure

[WIP/TBC] **pytexcv_c.c** : The encapsulating C program that manages input/output and invokes the Python script.
[WIP/TBC] **pycv_template.tex** : LaTex template for the CV.
[WIP] **cvbuilder.py** : The Python script that processes the input data and generates the LaTex document.
**README.md**: This README file providing project information and instructions.

## Future Enhancements

1. Implement more customization options for the LaTex template.
2. Add support for additional output formats (e.g., HTML, Markdown).
3. Create a graphical user interface (GUI) for easier interaction.

## Contributors

- Tommi Bimbato (Project Creator)

## License

This project is dedicated to the public domain under the Creative Commons Zero (CC0) license. You can find more information about CC0 [here](https://creativecommons.org/publicdomain/zero/1.0/) or in the LICENSE file in this repo.

---

**Note:** This README is a work in progress and will be updated as the project develops. Please refer to the repository for the most up-to-date information and instructions.
