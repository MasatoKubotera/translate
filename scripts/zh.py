#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

from googletrans import Translator
translator = Translator()

def translate(data): 
    rospy.loginfo(data.data + '-->' + translator.translate(data.data, src='ja', dest='zh-cn').text)

def main():
    print('日本語を中国語(簡体字)に翻訳します。')
    rospy.Subscriber('words', String, translate)
    rospy.spin()
       
if __name__ == '__main__':
    rospy.init_node('translate_zh', anonymous=True)
    main()