import openai
from dotenv import load_dotenv
import os
import base64
import glob
import sys
from pathlib import Path  # Added this import

def encode_image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def process_screenshots(directory):
    # Load environment variables and set up OpenAI client
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    client = openai.OpenAI()

    # Get absolute path and find all Screenshot*.png files
    dir_path = Path(directory).resolve()
    screenshot_files = list(dir_path.glob("Screenshot*.png"))

    if not screenshot_files:
        print(f"No Screenshot*.png files found in {dir_path}")
        return

    for original_file in screenshot_files:
        # Convert the image to base64
        base64_image = encode_image_to_base64(original_file)
        
        # Get content description from OpenAI
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text", 
                            "text": "Generate a brief, descriptive filename (using underscores between words) for this screenshot. Keep it under 4 words."
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{base64_image}",
                                "detail": "low",
                            }
                        }
                    ]
                }
            ],
            max_tokens=50
        )
        
        # Get the suggested name and clean it
        new_name = response.choices[0].message.content.strip().lower()
        # Remove any characters that aren't safe for filenames
        new_name = "".join(c if c.isalnum() or c == '_' else '_' for c in new_name)
        # Add .png extension
        new_name = f"{new_name}.png"
        
        # Print the mv command with full paths
        print(f"mv '{original_file}' '{dir_path / new_name}'")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)
    
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Error: '{directory}' is not a valid directory")
        sys.exit(1)

    process_screenshots(directory)

