# PyBundletool

PyBundletool is a Python script that facilitates the creation of APK sets using Google's [bundletool](https://developer.android.com/studio/command-line/bundletool). This script takes a path to an Android App Bundle (`.aab` file) and an output file name as input, then executes the necessary `bundletool` command to generate the APK set.

## Prerequisites

- Python 3.x
- Java Development Kit (JDK) installed

## Usage

1. Clone this repository.

2. Open a terminal and navigate to the directory containing the `main.py` script.

3. Run the script with the following command:

    ```bash
    python3 main.py /path/to/your/application.aab output_filename.apks
    ```

    Replace `/path/to/your/application.aab` with the actual path to your `.aab` file and `output_filename.apks` with the desired output file name.

## Example

```bash
python3 main.py ./a.aab g.apks
