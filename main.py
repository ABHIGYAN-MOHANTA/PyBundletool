import subprocess
import sys
import os

def build_apks(aab_path, output_file):
    # Path to bundletool JAR file
    bundletool_jar = "/usr/bin/java"

    # Command to build the APK set
    command = [
        bundletool_jar,
        "-jar",
        "./bundletool-all-1.15.6.jar",
        "build-apks",
        "--bundle=" + aab_path,
        "--output=" + output_file,
        "--mode=universal"
    ]

    try:
        # Run the command
        subprocess.run(command, check=True)
        print("APK set successfully created at:", output_file)
    except subprocess.CalledProcessError as e:
        print("Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <aab_file_path> <output_file_name.apks>")
        sys.exit(1)

    # Get input arguments
    aab_file_path = sys.argv[1]
    output_file_name = sys.argv[2]

    # Ensure the provided .aab file exists
    if not os.path.exists(aab_file_path):
        print("Error: The specified .aab file does not exist.")
        sys.exit(1)

    # Build the APK set
    output_file = "./" + output_file_name
    build_apks(aab_file_path, output_file)
