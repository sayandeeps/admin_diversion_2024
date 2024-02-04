from flask import Flask, render_template, request, redirect, url_for
import subprocess
import os
import re

app = Flask(__name__)

def storeipfs(input_path):
    # Define the command for uploading to IPFS
    command = ["npx", "thirdweb", "upload", input_path]

    # Run the command and capture the output
    result = subprocess.run(command, capture_output=True, text=True)

    # Check if the process was successful
    if result.returncode == 0:
        # Extract relevant information from the output
        output_string = result.stderr

        # Define a regex pattern to match only strings starting with https
        pattern = r'https://[^ \n/]+'

        # Find the first match in the string
        match = re.search(pattern, output_string)

        # Return the matched URL if found, otherwise return an error
        if match:
            return match.group()
        else:
            return "Error: No match found."
    else:
        return "Error: Unable to upload file to IPFS."

def run_hello_photogrammetry(input_path, output_path):
    subprocess.call([
        "/Users/TrainingMug/hellophoto/Products/usr/local/bin/HelloPhotogrammetry",
        input_path,
        output_path,
        "-d",
        "preview",
        "-f",
        "normal"
    ])



def open_usdz_file(file_path):
    subprocess.call(["open", file_path])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    
    # Save the uploaded file
    upload_folder = f"/Users/TrainingMug/subproc/models/{email}" 

  

    # Generate output path
    output_usdz = f"/Users/TrainingMug/subproc/outputs/{email}.usdz"

    
    # Run photogrammetry and open the file
    run_hello_photogrammetry(upload_folder, output_usdz)
    open_usdz_file(output_usdz)

    return "Thank You for using our service please wait till we process your request" 

# Update the /ipfs route
@app.route('/ipfs', methods=['POST'])
def ipfs():
    furl = request.form['furl']

    # store
    result = storeipfs(f'/Users/sayandeepsharma/Downloads/{furl}.glb')
    thumbnamil = storeipfs(f'/Users/sayandeepsharma/Downloads/Untitled.png')

    # Extract matches from the result

    # Render the result template with the IPFS result and matches
    return render_template('result.html', result=result ,thumbnamil=thumbnamil )


if __name__ == '__main__':
    app.run(debug=True)
