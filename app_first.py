#真正讓網站上線
# 除了這個python檔，還要建立3個檔
#  1.runtim.txt 寫python的版本(Python-3.8.5)
#  2.requirements.txt 寫使用的套件=>(Flask=>程式中用的，gunicorn=>雲端運作用的)
#  3.Procfile 管理heroku如何執行程式(web gunicorn python檔名:python程式檔中實體物件)
#  4.安裝git.tool(已經安裝過就Ok了，如果沒有就去"https://git-scm.com/download/win"安裝)
#  5.heroku註冊(帳號:jim80129@gmail.com 密碼:/ityity222 (密碼的確有/喔)
#  6.登入後，create new app，進入app後，案deploy開始布署，讓程式能上線運作
#  7.安裝heroku CLI 
#  8.在下方終端機鍵入git，以及鍵入heroku會出現一堆東西，代表成功安裝了
#  9.鍵入heroku login，打上帳號密碼登入
#  10.初始化專案(只需要做一次，後續更新不需要做): 1.鍵入git init 2.鍵入heroku git:remote -a python-trainingfu
#  11.布署專案: 1.鍵入git add . 2.鍵入git commit -am "make it better" 3.鍵入git push heroku master
#  12.網頁網址出現，別人電腦都可以連上線(下方網址一樣是主機名稱+根目錄)
#  #修改程式內部處理，只要再重新打佈署的三行指令就可以了(不用初始化)

from flask import Flask
app_1=Flask(__name__)

@app_1.route("/")
def interface():
    return "online，林彥甫架設"

@app_1.route("/step_1")
def step_1():
    return "step_1 is ok"

@app_1.route("/step_2")
def step_2():
    return "step_2 is ok"

if __name__=="__main__":
    app_1.run()

