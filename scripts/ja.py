#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

def main():
    rospy.init_node('master_ja', anonymous=True)
    pub = rospy.Publisher('words', String, queue_size=1)

    while not rospy.is_shutdown():    
        str = input('翻訳する日本語を入力してくだいさい：')
        pub.publish(str)


if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass