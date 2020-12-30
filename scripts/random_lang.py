#!/usr/bin/env python3
import rospy
from std_msgs.msg import String
from googletrans import Translator
import random

translator = Translator()
random.random()

def translate(data):
    lang = [['af','afrikaans'],['sq','albanian'],['am','amharic'],['ar','arabic'],['hy','armenian'],['az','azerbaijani'],['eu','basque'],['be','belarusian'],['bn','bengali'],['bs','bosnian'],['bg','bulgarian'],['ca','catalan'],['ceb','cebuano'],['ny','chichewa'],['zh-cn','chinese (simplified)'],['zh-tw','chinese (traditional)'],['co','corsican'],['hr','croatian'],['cs','czech'],['da','danish'],['nl','dutch'],['en','english'],['eo','esperanto'],['et','estonian'],['tl','filipino'],['fi','finnish'],['fr','french'],['fy','frisian'],['gl','galician'],['ka','georgian'],['de','german'],['el','greek'],['gu','gujarati'],['ht','haitian creole'],['ha','hausa'],['haw','hawaiian'],['iw','hebrew'],['hi','hindi'],['hmn','hmong'],['hu','hungarian'],['is','icelandic'],['ig','igbo'],['id','indonesian'],['ga','irish'],['it','italian'],['ja','japanese'],['jw','javanese'],['kn','kannada'],['kk','kazakh'],['km','khmer'],['ko','korean'],['ku','kurdish (kurmanji)'],['ky','kyrgyz'],['lo','lao'],['la','latin'],['lv','latvian'],['lt','lithuanian'],['lb','luxembourgish'],['mk','macedonian'],['mg','malagasy'],['ms','malay'],['ml','malayalam'],['mt','maltese'],['mi','maori'],['mr','marathi'],['mn','mongolian'],['my','myanmar (burmese)'],['ne','nepali'],['no','norwegian'],['ps','pashto'],['fa','persian'],['pl','polish'],['pt','portuguese'],['pa','punjabi'],['ro','romanian'],['ru','russian'],['sm','samoan'],['gd','scots gaelic'],['sr','serbian'],['st','sesotho'],['sn','shona'],['sd','sindhi'],['si','sinhala'],['sk','slovak'],['sl','slovenian'],['so','somali'],['es','spanish'],['su','sundanese'],['sw','swahili'],['sv','swedish'],['tg','tajik'],['ta','tamil'],['te','telugu'],['th','thai'],['tr','turkish'],['uk','ukrainian'],['ur','urdu'],['uz','uzbek'],['vi','vietnamese'],['cy','welsh'],['xh','xhosa'],['yi','yiddish'],['yo','yoruba'],['zu','zulu'],['fil','Filipino'],['he','Hebrew']]
    random.shuffle(lang)
    rospy.loginfo('Translate to ' + lang[0][1] + ' : ' + data.data + '-->' + translator.translate(data.data, src='ja', dest=lang[0][0]).text)

def main():
    print('日本語をランダムな言語に翻訳します。')
    rospy.Subscriber('words', String, translate)
    rospy.spin()
       
if __name__ == '__main__':
    rospy.init_node('translate_random', anonymous=True)
    main()