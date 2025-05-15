import random
import string

#ローマ字・数字・記号の組み合わせのランダムな12文字を生成するプログラム
#それぞれの文字種別から4文字ずつ取得する。
def password_generator():
    random_let = [random.choice(string.ascii_letters) for i in range(4)]
    random_dit = [random.choice(string.digits) for i in range(4)]
    random_pun = [random.choice(string.punctuation) for i in range(4)]
    password = random_let + random_dit + random_pun
    print(password)
    password = ''.join(random.sample(password,len(password)))
    print(password)

password_generator()
