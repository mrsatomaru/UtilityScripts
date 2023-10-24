import argparse
import sys

def ask_preprocessing_question():
    while True:
        answer = input("前処理はしましたか? (yes/no): ").strip().lower()
        if answer in ['yes', 'no']:
            return answer == 'yes'
        else:
            print("正しい答え (yes/no) を入力してください。")

parser = argparse.ArgumentParser(description="前処理の確認")
parser.add_argument("-y", "--yes", action="store_true", help="前処理の確認をスキップする")
args = parser.parse_args()

if not args.yes:
    if not ask_preprocessing_question():
        print("前処理を完了してから再度実行してください。")
        sys.exit(1)  # プログラムを停止
    else:
        print("プログラムを実行します。")
else:
    print("プログラムを実行します。")

# この後に、現存するスクリプトの内容を貼り付けてください。
