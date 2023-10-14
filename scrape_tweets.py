debug = False
f = open('tweets.js', 'r', encoding="utf-8")
data = f.read()
f.close()
print("総ツイート数:", data.count('full_text'))
print(type(data))
tweets = []
for i in range(len(data)):
    if data[i:i + 9] == "full_text":
        st = ""
        j = i + 14
        while j < (len(data)) and data[j + 1] != ',':
            st += data[j]
            j += 1
        tweets.append(st)
        # print(st)

tmp = []
f = open('tweets', 'w', encoding="utf-8")
for tweet in tweets:
    tweet += "\n"
    if tweet[0:2] != "RT":
        tmp.append(tweet)

        f.writelines(tweet)
f.close()
tweets = tmp


