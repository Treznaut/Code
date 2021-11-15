import youtube_dl

video_list = []

while True:
    v_m = int(input("Video \'1\' or Music \'2\' "))
    if v_m == 1:
        vm = "Videos/YouTubeVideos"
        break
    elif v_m == 2:
        vm = "Music"
        break
    else:
        print("Use correct formatting!")

print("Enter URLs (Terminate by 'STOP') ")
while True:
    url = input("")
    if url == 'STOP':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    
    
    print(f"Downloading video {x}...")
    ("C:/Users/IamTr/Videos")
    print("Done")