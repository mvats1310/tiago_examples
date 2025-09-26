#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist

def move_forward():
    # Create a publisher to the cmd_vel topic
    pub = rospy.Publisher('/mobile_base_controller/cmd_vel', Twist, queue_size=10)
    rospy.init_node('move_forward_node', anonymous=True)

    rate = rospy.Rate(10)  # 10 Hz loop rate
    twist = Twist()
    twist.linear.x = 0.2   # move forward at 0.2 m/s
    twist.angular.z = 0.0  # no rotation

    rospy.loginfo("Moving forward...")
    start_time = rospy.Time.now().to_sec()

    while not rospy.is_shutdown():
        current_time = rospy.Time.now().to_sec()
        if current_time - start_time < 5.0:   # run for 5 seconds
            pub.publish(twist)
        else:
            # Stop the robot
            twist.linear.x = 0.0
            pub.publish(twist)
            rospy.loginfo("Stopping.")
            break
        rate.sleep()

if __name__ == '__main__':
    try:
        move_forward()
    except rospy.ROSInterruptException:
        pass
