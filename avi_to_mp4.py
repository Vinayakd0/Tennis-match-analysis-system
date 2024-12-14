import subprocess

def convert_to_mp4(input_file, output_file):
    command = [
        'ffmpeg', '-i', input_file, '-c:v', 'libx264', '-preset', 'slow', 
        '-crf', '22', '-c:a', 'aac', '-b:a', '192k', '-y', output_file
    ]
    subprocess.run(command)
