from mutagen.mp4 import MP4
import os
import mimetypes
import sys


def change_mp4_title(file_path, new_title):
    mp4 = MP4(file_path)
    mp4["\xa9nam"] = new_title[:-4]
    mp4.save()


def Sync_name_and_title_of_video(directory):

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            # Check if the file is a video
            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type and mime_type.startswith('video'):
                # Get the video length and add it to total_length
                print(file)
                change_mp4_title(file_path, file)


if len(sys.argv) > 1:
    directory_path = sys.argv[1]
    Sync_name_and_title_of_video(directory_path)
else:
    print("You didn't provide the file/folder path in arguments.")
