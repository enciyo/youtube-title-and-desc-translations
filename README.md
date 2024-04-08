# Youtube Title and Description Translations

This project is about translating YouTube video titles and descriptions.

## Table of Contents

- [Aim](#aim)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Support](#support)

## Aim

The aim of this project is to provide a cost-effective solution for translating YouTube video titles and descriptions. While similar services can be accessed via the YouTube API, our goal is to offer the same functionality without incurring any additional expenses.

## Installation

To install and run this project, follow these steps:

1. Install Python on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. Clone the repository to your local machine.

3. Navigate to the project directory and install the required dependencies with pip:
    ```
    pip install -r requirements.txt
    ```

4. Run the main.py file:
    ```
    python main.py
    ```
Please ensure that you have the necessary permissions to install and run programs on your system.

## Usage

To use this project, follow these steps:

1. Change the `CONST_EMAIL` variable in the `constants.py` file.
2. Run the project. This will open a Google login page.
3. Log in to Google within the `CONST_WAIT_GOOGLE_LOGIN_TIMEOUT` minute.
4. Once a successful Google login is detected, the script will continue running.

## Contributing

For performance operations and errors, please open an issue and describe it in detail.

## Support
If you find this project helpful and want to support, you can subscribe to my YouTube channel [here](https://www.youtube.com/@Voicepa).
