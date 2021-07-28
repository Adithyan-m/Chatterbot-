#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    count = 0
    pub = rospy.Publisher('alpha',String,queue_size=10)
    rospy.init_node('Talk',anonymous=True)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        if count <101:
            h = "hello_world %s" % count
            rospy.loginfo(h)
            pub.publish(h)
            count+=1
            rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        passss
