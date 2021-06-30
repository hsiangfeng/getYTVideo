#!/usr/bin/python3

from pytube import Playlist, YouTube
import re, os, ssl, time

ssl._create_default_https_context = ssl._create_unverified_context

url = str(input('請輸入你要下載的影片網址 => '))

#避免使用者輸入空白的 Url
if not url:
  print('你輸入了一個空的 Youtub 網址。')
  exit()

ytList = str(input('是否為播放清單(y/n) => '))
ytAudio = str(input('是否下載純粹的聲音檔(y/n) => '))
ytListStatus = bool(False)
ytAudioStatus = bool(False)

filename = time.strftime("%Y%m%d%H%M%S", time.localtime())

# 切換播放清單用
if ytList == 'y':
  ytListStatus = bool(True)
else:
  ytListStatus = bool(False)

# 切換純粹聲音檔案用
if ytAudio == 'y':
  ytAudioStatus = bool(True)
else:
  ytAudioStatus = bool(False)

def YTDownload(url):
  # 若目錄不存在就建立一個
  if not os.path.isdir(filename):
      os.mkdir(filename)

  yt = YouTube(url)
  results = yt.streams[0]
  if ytAudioStatus:
    results = yt.streams.filter(subtype="mp4", only_audio=True)
    results[0].download(filename)
    return results[0].title
  else:
    results.download(filename)
    return results.title

def getYoutube():
  if ytListStatus:
    try:
      downNun = int(0)
      playlist = Playlist(url)
      playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
      print('你準備下載的清單連結網址 =>', url)
      print('準備下載的數量 =>', len(playlist.video_urls), '筆。')
      for idx, val in enumerate(playlist.video_urls):
        print(idx + 1, '-', YTDownload(val), '- 下載完畢。')
        downNun += 1
      print('總共下載了', downNun, '筆影音。')
    except:
      print('下載播放清單音樂出現錯誤或是輸入錯誤的播放清單網址。')
  else:
    try:
      print(YTDownload(url), '- 下載完畢。')
    except:
      print('下載音樂出現錯誤或是輸入錯誤的網址。')

# 初始化
getYoutube()

