![GitHub Repo stars](https://img.shields.io/github/stars/AnWongDrew/teams_video_downloader)
![GitHub forks](https://img.shields.io/github/forks/AnWongDrew/teams_video_downloader)
![GitHub contributors](https://img.shields.io/github/contributors/AnWongDrew/teams_video_downloader)

![Visitors](https://api.visitorbadge.io/api/visitors?path=AnWongDrew%2Fteams_video_downloader&countColor=%23263759)


# Teams Video Downloader

Teams Video Downloader is a Python-based tool that allows you to conveniently download lecture videos recorded using Microsoft Teams and stored in a SharePoint drive with view-only permissions.

## Background

Many educational institutions or organizations use Microsoft Teams for recording lectures, and these videos are often stored in a SharePoint drive with view-only permissions, preventing users from downloading them directly. This tool provides a solution to this problem by automating the process of extracting the video manifest links and downloading the videos using FFmpeg.

The inspiration for this project came from the blog post [How to Download "View Only" Teams Meeting Recording Video from SharePoint](https://www.lisenet.com/2022/how-to-download-view-only-teams-meeting-recording-video-from-sharepoint/). That blog post outlines the manual steps required to download "view-only" Teams meeting recordings from a SharePoint drive. The process involves using the browser's developer tools to locate the DASH XML URLs for the video files, which can then be used to download the videos. 

This project aims to automate that manual process by using a Python script to log in to the SharePoint drive, extract the necessary DASH XML URLs, and then download the videos using FFmpeg. By automating these steps, the Teams Video Downloader tool provides a more convenient and efficient way to access and save these lecture recordings for future use.

## Features

- Automatically logs in to the SharePoint drive and navigates to the specified Teams video URLs.
- Extracts the DASH XML URLs for the video files.
- Downloads the videos using FFmpeg, converting them to MP4 format.

## Prerequisites

- Python 3.x
- Selenium WebDriver (e.g., ChromeDriver or GeckoDriver)
- Selenium-wire (used for capture response objects)
- FFmpeg
- Pandas
- TKinter

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/teams-video-downloader.git
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Ensure you have the appropriate Selenium WebDriver installed and available in your system's PATH.

4. Download the FFmpeg binary from the official FFmpeg website and place it in the root folder of the project.

## Usage

1. Prepare an Excel file containing the URLs of the Teams video pages you want to download.

2. Run the `url_to_video_link.py` script, which will prompt you to select the Excel file.

3. Enter your login credentials when prompted.

4. The script will extract the DASH XML URLs for each video and add them to the Excel file.

5. Run the `video_link_to_mp4.py` script, which will prompt you to select the updated Excel file.

6. The script will download the videos in MP4 format using FFmpeg.

## Known Issues

- After entering the password, the script requires you to press Enter manually to proceed.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This project is intended for educational and learning purposes only. It is designed to demonstrate techniques for interacting with Microsoft Teams video content within the boundaries of ethical and legal standards. 

Downloading videos without proper authorization may infringe on the intellectual property rights of content creators. It is important to respect copyright laws and the terms of service of platforms like Microsoft Teams.

The developers and contributors of this project do not endorse, support, or promote the unauthorized downloading or distribution of copyrighted content. Any misuse of this project for illegal activities is not the responsibility of the project owners.

Use this tool responsibly and ensure that you have the necessary permissions before downloading any video content. By using this project, you agree to take full responsibility for your actions and to comply with all relevant laws and regulations.
