# AltasTool

使用python 2.7

一個簡單的圖形化介面工具, 主要把一個資料夾內所有的圖片資源做轉換的工作, 主要做兩件事:    

1. 將副檔名為.png的altas轉換成.png.ccz, 並使用[TexturePacker](https://www.codeandweb.com/texturepacker)轉換成統一的格式, 使用以下參數    
```
--format cocos2d --opt RGBA4444 --dither-fs-alpha --size-constraints AnySize --allow-free-size --disable-rotation --trim-mode None --border-padding 0 --inner-padding 0
```
2. 可以設定黑名單, 如果不要轉成.ccz的可以加入黑名單中, 可以設置[pngquant](https://pngquant.org/)路徑用來做png優化
