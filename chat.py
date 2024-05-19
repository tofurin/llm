import sys
import time
import random
import voicevox as voicevox
import threading
import ollama
import pytts

# ChatGPTの回答を表示する関数を定義
def display_chatgpt_response(response):
    for char in response:
        print(char, end="", flush=True)
        print("●", end="", flush=True)
        time_random=random.randrange(1, 4)
        time.sleep(time_random*0.01)
        sys.stdout.write("\b \b")
        sys.stdout.flush()
          # 文字ごとの表示間隔を調整
    print()  # 改行


if __name__ == "__main__":
    # ユーザーの入力を受け取り、ChatGPTに質問し、回答をアニメーション風に表示する
    while True:
        user_input = input("You: ")
        if user_input.lower() == '/exit':
            break
        # ChatGPTの回答を代わりに用いています
        response = ollama.ollama(user_input)
        thread1=threading.Thread(target=voicevox.play, args=(response,))
        thread2=threading.Thread(target=display_chatgpt_response, args=(response,))

        print("AI:", end="", flush=True)
        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

