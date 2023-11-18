import pyaudio
import wave
import os

default_frames = 512


class TextColors:
    if not os.name == 'nt':
        blue = '\033[94m'
        green = '\033[92m'
        warning = '\033[93m'
        fail = '\033[91m'
        end = '\033[0m'
    else:
        blue = ''
        green = ''
        warning = ''
        fail = ''
        end = ''


recorded_frames = []
device_info = {}
record_time = 5

# Use module
p = pyaudio.PyAudio()

# Set default to first in list or ask Windows
try:
    default_device_index = p.get_default_input_device_info()
except IOError:
    default_device_index = -1

# Select Device
print(TextColors.blue + "Available devices:\n" + TextColors.end)
for i in range(0, p.get_device_count()):
    info = p.get_device_info_by_index(i)
    print(TextColors.green + str(info["index"]) + TextColors.end + ": \t %s \n \t %s \n" % (
        info["name"], p.get_host_api_info_by_index(info["hostApi"])["name"]))

    if default_device_index == -1:
        default_device_index = info["index"]

# Handle no devices available
if default_device_index == -1:
    print(TextColors.fail + "No device available. Quitting." + TextColors.end)
    exit()

# Get input or default
device_id = int(input(
    "Choose device [" + TextColors.blue + str(default_device_index) + TextColors.end + "]: ") or default_device_index)
print("")

# Get device info
try:
    device_info = p.get_device_info_by_index(device_id)
except IOError:
    device_info = p.get_device_info_by_index(default_device_index)
    print(TextColors.warning + "Selection not available, using default." + TextColors.end)

# Choose between loopback or standard mode
is_input = device_info["maxInputChannels"] > 0
is_wasapi = (p.get_host_api_info_by_index(device_info["hostApi"])["name"]).find("WASAPI") != -1
if is_input:
    print(TextColors.blue + "Selection is input using standard mode.\n" + TextColors.end)
else:
    if is_wasapi:
        use_loopback = True
        print(TextColors.green + "Selection is output. Using loopback mode.\n" + TextColors.end)
    else:
        print(TextColors.fail + "Selection is input and does not support loopback mode. Quitting.\n" + TextColors.end)
        exit()

record_time = int(
    input("Record time in seconds [" + TextColors.blue + str(record_time) + TextColors.end + "]: ") or record_time)

# Open stream
channel_count = device_info["maxInputChannels"] if (
        device_info["maxOutputChannels"] < device_info["maxInputChannels"]) else device_info["maxOutputChannels"]
stream = p.open(format=pyaudio.paInt16,
                channels=channel_count,
                rate=int(device_info["defaultSampleRate"]),
                input=True,
                frames_per_buffer=default_frames,
                input_device_index=device_info["index"],
                as_loopback=True)

# Start Recording
print(TextColors.blue + "Starting..." + TextColors.end)

for i in range(0, int(int(device_info["defaultSampleRate"]) / default_frames * record_time)):
    recorded_frames.append(stream.read(default_frames))
    print(".")

print(TextColors.blue + "End." + TextColors.end)
# Stop Recording

stream.stop_stream()
stream.close()

# Close module
p.terminate()

filename = input("Save as [" + TextColors.blue + "out.wav" + TextColors.end + "]: ") or "out.wav"

waveFile = wave.open(filename, 'wb')
waveFile.setnchannels(channel_count)
waveFile.setsampwidth(p.get_sample_size(pyaudio.paInt16))
waveFile.setframerate(int(device_info["defaultSampleRate"]))
waveFile.writeframes(b''.join(recorded_frames))
waveFile.close()
