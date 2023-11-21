import argparse
from pytube import YouTube
from sys import exit
from loguru import logger

def download_video(link, download_path=None):
    '''
    Downloads the video from the given link at the specified resolution.
    
    Parameters:
    link (str): URL of the YouTube video.
    download_path (str, optional): Directory path where the video will be downloaded.
    '''
    try:
        yt = YouTube(link)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=download_path)
        logger.info(f"Downloaded video: {yt.title}")
    except Exception as e:
        logger.error(f"Error downloading video: {e}")

def read_links_from_file(file_path, download_path=None):
    '''
    Reads video links from a file and downloads them.

    Parameters:
    file_path (str): Path to the file containing YouTube video links.
    download_path (str, optional): Directory path where videos will be downloaded.
    '''
    try:
        with open(file_path, "r") as file:
            links = file.readlines()
            if not links:
                logger.warning("No links found in the file.")
                return

            for link in links:
                download_video(link.strip(), download_path)
    except FileNotFoundError:
        logger.error(f"File {file_path} not found")
        exit()

def main():
    parser = argparse.ArgumentParser(description="Download videos from YouTube.")
    parser.add_argument("link", nargs='?', help="YouTube video link", default=None)
    parser.add_argument("--path", help="Download path", default=None)
    parser.add_argument("--file", help="Read links from a file", default="links.txt")

    args = parser.parse_args()

    if args.link:
        download_video(args.link, args.path)
    else:
        read_links_from_file(args.file, args.path)

if __name__ == "__main__":
    main()
