import requests


header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
                       '62.0.3202.89 Safari/537.36'}

#r = requests.get('https://github.com')

for i in range(0,50):
    r = requests.get('https://kyfw.12306.cn/passport/captcha/captcha-image', verify=False)
    imgsrc = 'img/code'+str(i)+'.jpeg'
    with open(imgsrc, 'wb') as fd:
        # for chunk in tqdm(r.iter_content()):
        #     fd.write(chunk)

        for chunk in r.iter_content(100):
            fd.write(chunk)

    print('success')