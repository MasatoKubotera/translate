#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

from googletrans import Translator
translator = Translator()

def translate(data): 
    rospy.loginfo(data.data + '-->' + translator.translate(data.data, src='ja', dest='de').text)

def main():
    print('日本語をドイツ語に翻訳します。')
    rospy.Subscriber('words', String, translate)
    rospy.spin()
       
if __name__ == '__main__':
    rospy.init_node('translate_de', anonymous=True)
    main()