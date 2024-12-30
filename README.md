# Text_To_Handwriting_Convertor
A Python-based tool to convert plain text into handwriting-style images with customizable colors. Perfect for creating visually appealing notes, personalizing projects, or adding a unique touch to your content.

## Features
- **Text to Handwriting**: Converts input text into handwriting-style images.
- **Customizable Colors**: Choose your preferred handwriting color using RGB values.
- **Error Handling**: Ensures smooth execution with helpful error messages.
- **Fallback Mechanism**: Defaults to a predefined color if no custom color is specified.

## Requirements
- Python 3.6 or later
- Required Libraries:
  - `pywhatkit`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/text-to-handwriting-converter.git
   ```
2. Navigate to the project directory:
   ```bash
   cd text-to-handwriting-converter
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python code1.py
   ```
2. Enter the text you want to convert.
3. Specify whether to use the default color or input a custom RGB color code.

## Example
```plaintext
Enter Your Text: Hello, this is a test.
Do you want to change the handwriting color? (yes/no): yes
Enter the color code as R,G,B (e.g., 255,0,0 for red): 0,128,255
Handwriting image successfully created as 'demo.png'
End
```

## Troubleshooting
- **Unable to Access PyWhatKit API**: Check your internet connection or try again later.
- **Invalid RGB Input**: Ensure the color code is in the format `R,G,B` with values between 0 and 255.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve this project.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgments
Special thanks to the creators of the `pywhatkit` library for providing the handwriting API.

