from moviepy.editor import VideoFileClip

def video_to_wav(input_video_path, output_wav_path):
    # Load the video clip
    video_clip = VideoFileClip(input_video_path)
    
    # Extract audio
    audio_clip = video_clip.audio
    
    # Write audio to .wav file
    audio_clip.write_audiofile(output_wav_path)
    
    # Close the clips
    audio_clip.close()
    video_clip.close()

# Input video file path
input_video_path = "path_to_your_input_video.mp4"

# Output .wav file path
output_wav_path = "path_to_your_output_audio.wav"

# Convert video to .wav
video_to_wav(input_video_path, output_wav_path)

print("Conversion completed!")
