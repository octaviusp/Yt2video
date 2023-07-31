from pytube import YouTube

def already_downloaded():
    print(f"\n- YT VIDEO was downloaded succesfully!")

def download_video(url_video: str, filename="", output_path="", high_quality=True):
    yt = YouTube(url_video, on_complete_callback=already_downloaded()).streams
    
    if not output_path: output_path = "" 
    if not filename: yt._title

    filename = has_extension(filename)
    if high_quality: 
        yt.get_highest_resolution().download(output_path,filename)
    else:
        yt.get_lowest_resolution().download(output_path,filename)

def has_extension(title: str):
    if ".mp3" not in title:
        title += ".mp3"
    return title

if __name__ == "__main__":
    url_to_download = input("\n - URL TO DOWNLOAD: ")
    file_name = input("\n - NAME OF THE FILE (WITHOUT EXTENSION!): ")
    path_to_extract = input("\n - PATH TO EXTRACT (ENTER TO THE CURRENT PATH): ")
    try:
        download_video(url_video=url_to_download, filename=file_name, output_path=path_to_extract)
    except:
        print("\nAn error was ocurred, try again.")



