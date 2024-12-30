import pywhatkit as pw

try:
    txt = input("Enter Your Text: ").strip()
    if not txt:
        raise ValueError("Text input cannot be empty.")
    
    change_color = input("Do you want to change the handwriting color? (yes/no): ").strip().lower()
    
    if change_color == "yes":
        try:
            color_input = input("Enter the color code as R,G,B (e.g., 255,0,0 for red): ").strip()
            color = [int(c) for c in color_input.split(",")]
            if len(color) != 3 or not all(0 <= c <= 255 for c in color):
                raise ValueError("Invalid color code. Please provide three values between 0 and 255.")
        except Exception as e:
            print(f"Invalid color input: {e}. Using default color [0, 0, 138].")
            color = [0, 0, 138]
    else:
        print("Using default color [0, 0, 138].")
        color = [0, 0, 138]
    
    pw.text_to_handwriting(txt, "demo.png", color)
    
    print("Handwriting image successfully created as 'demo.png'")
except pw.core.exceptions.UnableToAccessApi:
    print("Error: Unable to access the PyWhatKit handwriting API. Please check your internet connection or try again later.")
except ValueError as ve:
    print(f"Input Error: {ve}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print("End")
