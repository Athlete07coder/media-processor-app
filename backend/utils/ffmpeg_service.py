import subprocess

def process_media(input_path, operation, file_id):
    try:
        if operation == "thumbnail":
            output = f"output/{file_id}.jpg"
            cmd = [
                "ffmpeg", "-i", input_path,
                "-ss", "00:00:02",
                "-vframes", "1",
                output
            ]

        elif operation == "compress":
            output = f"output/{file_id}_compressed.mp4"
            cmd = [
                "ffmpeg", "-i", input_path,
                "-vcodec", "libx264",
                "-crf", "28",
                output
            ]

        elif operation == "extract_audio":
            output = f"output/{file_id}.mp3"
            cmd = [
                "ffmpeg", "-i", input_path,
                "-q:a", "0",
                "-map", "a",
                output
            ]

        else:
            raise Exception("Invalid operation")

        result = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30
        )

        if result.returncode != 0:
            raise Exception(result.stderr.decode())

        return output

    except subprocess.TimeoutExpired:
        raise Exception("Processing timed out")

    except Exception as e:
        raise Exception(f"FFmpeg error: {str(e)}")