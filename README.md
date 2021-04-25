# 下載 Youtube 影音

> 此為使用 Python 撰寫下載 Youtube 影音的練習程式碼。

![Python](https://user-images.githubusercontent.com/19990752/115986204-acc8d680-a5e1-11eb-9d62-8f6bc256b712.png)

## 說明

執行 Python 之後會要求你輸入以下資訊：

- Youtube 網址
- 依據使用者輸入判斷是否為播放清單(y/n)
- 是否下載純粹的音樂檔案 or 影音檔案(y/n)

Youtube 播放清單測試用網址：[https://www.youtube.com/watch?v=wdH26D8Ssww&list=PLg_r40S5jeMIvAaq9OZweLCx8_N1OxO_Q](https://www.youtube.com/watch?v=wdH26D8Ssww&list=PLg_r40S5jeMIvAaq9OZweLCx8_N1OxO_Q)

單一 Youtube 下載網址：[https://www.youtube.com/watch?v=wdH26D8Ssww](https://www.youtube.com/watch?v=wdH26D8Ssww&list=PLg_r40S5jeMIvAaq9OZweLCx8_N1OxO_Q)

下載完畢之後將會依照當下下載的時間建立一個新資料夾，並放在該資料夾下。

## 使用技術

- Python3
- pytube
- re
- os
- ssl
- time
