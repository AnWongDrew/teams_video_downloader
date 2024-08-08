import pandas as pd
import subprocess
from tqdm import tqdm
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Prompt to ask for the Excel file
Tk().withdraw()
excel_file_path = askopenfilename(title="Select Excel file")

# Load the Excel file
df = pd.read_excel(excel_file_path)

# Iterate over the rows of the DataFrame with tqdm
for index, row in tqdm(df.iterrows(), total=df.shape[0], desc="Processing videos"):
    video_url = row['V_URL']
    video_name = row['VideoName']
    
    # Construct the ffmpeg command
    cmd = f'ffmpeg -i "{video_url}" -codec copy "{video_name}.mp4'

    # Execute the command
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, universal_newlines=True)
    for line in process.stdout:
        print(line)
    
print("All videos processed.")