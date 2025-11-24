from profanity_filter.filter import ProfanityFilter

def interactive_test():
    filter = ProfanityFilter(languages=['zh', 'en'])
    while True:
        user_text = input("请输入要测试的文本（输入exit退出）：\n")
        if user_text == "exit":
            print("互动检测已退出。")
            break
        print(f"屏蔽结果：{filter.censor(user_text)}")
        print(f"检测到的脏话：{filter.get_profane_words(user_text)}")
        print("="*30)

if __name__ == '__main__':
    interactive_test()
