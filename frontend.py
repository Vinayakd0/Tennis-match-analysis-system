import streamlit as st
import os
import subprocess
from pathlib import Path

# Input and output directories
INPUT_DIR = r"C:\Users\admin\Desktop\Tennis-analysis-system\input_videos"
OUTPUT_DIR = r"C:\Users\admin\Desktop\Tennis-analysis-system\output_videos"

# Ensure the directories exist
os.makedirs(INPUT_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

def run_main_script(input_video_path, output_video_path):
    """
    Function to call your main.py script to process the video.
    Replace with the actual logic from your main.py if needed.
    """
    command = f"python main.py --input {input_video_path} --output {output_video_path}"
    subprocess.run(command, shell=True, check=True)

def display_video(video_path):
    """
    Function to display video in Streamlit.
    """
    video_file = open(video_path, "rb")
    video_bytes = video_file.read()
    st.video(video_bytes)

# Streamlit UI
st.set_page_config(page_title="Tennis Court Line Detector", page_icon="🏸", layout="centered")
st.title("🏸 Tennis Court Line Detection System")
st.markdown(
    """
    This system detects court lines and player movements on the tennis court. 
    Upload a video and get the processed result with court lines and positions detected.
    """
)

# Upload video
uploaded_file = st.file_uploader("Choose a video file (MP4, AVI, MOV, MKV)", type=["mp4", "avi", "mov", "mkv"])

if uploaded_file:
    # Save the uploaded file to the input folder
    input_video_path = os.path.join(INPUT_DIR, "input_video.mp4")
    with open(input_video_path, "wb") as f:
        f.write(uploaded_file.read())
    st.success(f"Video uploaded successfully: {uploaded_file.name}")

    # Specify the output video path
    output_video_path = os.path.join(OUTPUT_DIR, "output_video.mp4")

    # Process video
    if st.button("Process Video"):
        st.info("Processing video... This may take a few moments.")
        with st.spinner("Processing..."):
            try:
                # Call your processing function/script
                run_main_script(input_video_path, output_video_path)
                st.success("Video processed successfully!")

                # Display the processed video
                st.write("### Processed Video:")
                display_video(output_video_path)

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
