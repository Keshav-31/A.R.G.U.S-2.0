#!/usr/bin/env python
import rospy
from std_msgs.msg import UInt16
import time
import getch
import getkey as gk

def talker():
    pub = rospy.Publisher('servo_pantilt', UInt16 , queue_size=10)
    rospy.init_node('pan_tilt', anonymous=True)
    rate = rospy.Rate(2) # 10hz3
    
    while not rospy.is_shutdown():
        #print" Enter the angle " 
        key_pressed=gk.getkey()
        if(key_pressed == gk.keys.UP) :
            i=0
        if(key_pressed == gk.keys.DOWN) :
            i=1
        if(key_pressed == gk.keys.LEFT) :
            i=2
        if(key_pressed == gk.keys.RIGHT) :
            i=3
        pub.publish(i)
        rate.sleep()
       

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
