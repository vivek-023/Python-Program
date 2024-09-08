from PIL import Image
import numpy as np
import sounddevice as sd 
from scipy.io.wavfile import write 

def read_image(image_path):
    """Read an image and convert it to grayscale."""
    image = Image.open(image_path).convert('L')
    return np.array(image)

def map_image_to_sound(image_data, duration=5, sample_rate=44100):
    """Map image data to sound parameters and generate sound."""
    height, width = image_data.shape
    # Flatten the image data
    flat_image_data = image_data.flatten()
    # Normalize pixel values to range [0, 1]
    normalized_data = flat_image_data / 255.0
    # Generate time array
    t = np.linspace(0, duration, int(sample_rate * duration))
    # Generate sound array
    sound_data = np.sin(2 * np.pi * 440 * t) * np.interp(t, np.linspace(0, duration, len(normalized_data)), normalized_data)
    return sound_data

def play_sound(sound_data, sample_rate=44100):
    """Play the generated sound."""
    sd.play(sound_data, sample_rate)
    sd.wait()

def save_sound(sound_data, sample_rate=44100, filename='output.wav'):
    """Save the generated sound to a file."""
    write(filename, sample_rate, sound_data.astype(np.float32))

def main(image_path):
    """Main function to run the image to sound conversion."""
    # Read the image
    image_data = read_image(image_path)
    # Map the image data to sound
    sound_data = map_image_to_sound(image_data)
    # Play the sound
    play_sound(sound_data)
    # Save the sound to a file
    save_sound(sound_data, filename='output.wav')

if __name__ == "__main__":
    image_path = r'C:\Users\VIVEK RANJAN\Downloads\0001 (8).jpg'
    main(image_path)