import re
import subprocess

# Define the command
command = [
    "npx", "thirdweb", "upload",
    "/Users/sayandeepsharma/Downloads/Untitled.png"
]

# Run the command and capture the output
result = subprocess.run(command, capture_output=True, text=True)

# Check if the process was successful
if result.returncode == 0:
    # Extract relevant information from the output
    output_string = result.stderr

    # Define a regex pattern to match IPFS URI and View Link
    pattern = r'https://[^ \n/]+'

    # Find all matches in the string
    match = re.search(pattern, output_string)
    

    # Print the matches
    print(match.group())
else:
    print("Error uploading file.")
