import sys,base64,json,os,time,pyperclip
from PIL import Image
from urllib import request
from baidusearch import BaiduSearch



isDebug = False

start = time.time()


class ParseColors(object):
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[1;31;40m'
    ENDC = '\033[0m'

    def __init__(self):
        super(ParseColors, self).__init__()

    def colorKey(self, key):
        result = self.FAIL + key + self.ENDC
        return result

    def parseBlue(self, word):
        result = self.OKGREEN + word + self.ENDC
        return result

color = ParseColors()

os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png") 
os.system("adb pull /sdcard/screenshot.png /home/chenxin/code/tools/MillionHeroes/screenpng/screenshot.png")  


im = Image.open(r"/home/chenxin/code/tools/MillionHeroes/screenpng/screenshot.png")   

img_size = im.size
w = im.size[0]
h = im.size[1]
# print("xx:{}".format(img_size))


region = im.crop((70,270, w-70,600))    #裁剪的区域
region.save("/home/chenxin/code/tools/MillionHeroes/screenpng/crop_test1.png")


anser = im.crop((150,725, 910,1200))
# anser = im.crop((70,630, 1000,1225))

anser.save("/home/chenxin/code/tools/MillionHeroes/screenpng/crop_anwser.png")

if isDebug:
    cropTime = time.time()
    print('裁切用时：'+str(cropTime-start)+'秒')


textResult = os.popen("tesseract ~/code/tools/MillionHeroes/screenpng/crop_test1.png stdout -l chi_sim").read()
noLine = textResult.replace('\n', '')
keyword = noLine[3:]   #识别的问题文本
print(color.parseBlue('question: ') + keyword)


answerResult = os.popen("tesseract ~/code/tools/MillionHeroes/screenpng/crop_anwser.png stdout -l chi_sim").read()
answerAttr = answerResult.split('\n\n')

if isDebug:
    print(answerAttr)

if isDebug:
    ocrTime = time.time()
    print('ocr用时：'+str(ocrTime-cropTime)+'秒')

splitKey = '不是'
keyIndex = keyword.find(splitKey)

notIntKey = '不包括'
notInKeyIndex = keyword.find(notIntKey)

notInKeyStr = answerAttr[0] + ' ' + answerAttr[1]

if keyIndex != -1:
    keyword = keyword[keyIndex+len(splitKey):]
    keyword = answerAttr[0] + ' ' + answerAttr[1] + ' ' + keyword;

# elif notInKeyIndex != -1:
#     keyword = keyword.replace(notIntKey, notInKeyStr)

print(keyword)

search = BaiduSearch(keyword)
allResult = search.getResult()


for i in range(0, len(answerAttr) - 1):
    # item = item.strip()
    item = answerAttr[i]
    # print(item)
    allResult = allResult.replace(item, color.colorKey(item))

print(allResult)

if isDebug:
    searchTime = time.time()
    print('search用时：'+str(searchTime-ocrTime)+'秒')

end = time.time()
print('程序用时：'+str(end-start)+'秒')



