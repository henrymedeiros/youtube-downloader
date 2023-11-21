# Youtube video downloader

## Requirements
Python and pip installed. <br>
To install requirements:
`pip install -r requirements.txt`

## Usage

With this script You can download one or multiple videos.

### Parameters
- `-h`: Show thishelp message and exit
- `--path PATH` Download path
- `--file FILE`  Read links from a file

### Instructions

- <b>To download just one video</b>
    - Run: `python main.py {link_goes_here}`   

- <b>To download multiple videos</b>
    - Create a file named `links.txt` and provide all of the links. (You can change which file, use --help for more info)
    - Run: `python main.py`   


You can also decide the download output path for these videos, it defaults to the same directory as the script.
To change it

- Run: `python main.py --path {absolute_path_goes_here}`

### Examples
- Downloads links of `links.txt` to current (same) folder: `python main.py`
- Downloads links of `links.txt` to download folder: `python main.py --path C:\Users\henry\Downloads`
- Download video using url : `python main.py https://www.youtube.com/watch?v=VKMw2it8dQY`