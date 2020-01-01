from random import *
def randomenglishsound(english,num):
    
    e = english[num]
    
    return e
    
def randomhirogana(hiro):
    
    a = randint(0,65)
    h = hiro[a]
    
    return h,a
    
def main():
    hirogana = ["あ","い","う","え","お","か","き","く",
    "け","こ","が","ぎ","ぐ","げ","ご",
    "さ","し","す","せ","そ","ざ","じ","ず","ぜ","ぞ",
    "た","ち","つ","て","と","だ","ぢ","づ","で","ど","な","に","ぬ","ね","の",
    "は","ひ","ふ","へ","ほ","ば","び","ぶ","べ","ぼ","ぱ",
    "ぴ","ぷ","ぺ","ぽ","ま","み","む","め","も",
    "や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん"]
    
    englishsound = ["a","i","u","e","o","ka","ki","ku",
    "ke","ko","ga","gi","gu","ge",
    "go","sa","shi","su","se","so","za","ji","zu","ze","zo","ta","chi","tsu","te",
    "to","da","ji","zu","de","do","na",
    "ni","nu","ne","no","ha","hi","fu","he","ho","ba","bi","bu","be","bo",
    "pa","pi","pu","pe","po","ma","mi","mu","me","mo","ya","yu",
    "yo","ra","ri","ru","re","ro","wa","wo","n/m"]
    trys = 0
    userinput = "notdone"
    print("Type done if your done.")
    while(userinput != "done"):
        hirocharacter=randomhirogana(hirogana)
        englishs=randomenglishsound(englishsound,randomnum)
        print("What is this sound?", hirocharacter)
        userinput = input()
        while(userinput != englishs and trys < 2):
            trys += 1
            print("wrong")
            userinput = input()
            if(trys == 2):
                print("Too bad!")
                pass
        while(userinput == englishs):
            print("Correct")
            pass
main()
