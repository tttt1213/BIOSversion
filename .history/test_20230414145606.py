#!/bin/python3

import asyncio
import cgi
import os

print("Content-type: text/html")
print("")
print("<html>")
print("<html>")


"""
# フォームのHTMLを出力する関数
def print_form():
    print("Content-type: text/html")
    print("")
    print("<html>")
    print("<body>")
    print("<form method='post' action='async_cgi.py'>")
    print("<input type='submit' name='submit' value='Start Async Task'>")
    print("</form>")
    print("</body>")
    print("</html>")

# 非同期処理を実行する関数
async def async_task():
    # ここに非同期で実行したい処理を記述する
    await asyncio.sleep(5)
    print("Async Task Completed")

# メインの処理
async def main():
    # フォームが送信されたかどうかを判定
    form = cgi.FieldStorage()
    if 'submit' in form:
        # フォームが送信された場合、非同期処理を開始
        task = asyncio.ensure_future(async_task())
        print_form()
        await task
    else:
        # フォームが送信されていない場合、フォームを表示
        print_form()

# メインの処理をイベントループで実行
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
"""