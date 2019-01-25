#!/usr/bin/env python

""" 
SentryBot lets us know if an intruder walks past.

Author: Ryan Soong, Geoffrey Wright
Started with a group of 4 so our repo has other students names
Version: 1/25/19
"""

import rospy

from sensor_msgs.msg import Image
from kobuki_msgs.msg import Sound

from cv_bridge import CvBridge, CvBridgeError
import numpy as np


class SentryNode(object):
    """Monitor a vertical scan through the depth map and create an
    audible signal if the change exceeds a threshold.

    
    Subscribes:
         /camera/depth_registered/image
       
    Publishes:
        /mobile_base/commands/sound

    """
    global PREVIOUS
    global AVERAGE
    global COUNT
    PREVIOUS = None
    AVERAGE = None

    def __init__(self):
        
        global PREVIOUS
        global AVERAGE

        """ Set up the Sentry node. """
        rospy.init_node('sentry')
        self.cv_bridge = CvBridge()
        rospy.Subscriber('/camera/depth_registered/image',
                         Image, self.depth_callback, queue_size=1)
        self.sound_pub = rospy.Publisher('/mobile_base/commands/sound', Sound,
                                         queue_size=1)
        rospy.spin()
        
        

    def depth_callback(self, depth_msg):
        """ Handle depth callbacks. """
        global PREVIOUS
        sound = Sound() 
        d = 0
        # Convert the depth message to a numpy array
        depth = self.cv_bridge.imgmsg_to_cv2(depth_msg)

        # YOUR CODE HERE.
        # HELPER METHODS ARE GOOD.)
        #print (np_array.shape) #480 x 640
        slice = depth[:,320]
        
        if PREVIOUS == None:
            PREVIOUS = slice
        else:
            d = self.calcNorm(slice)
            self.updateAverage(d)
       
        if AVERAGE != None:
            
       
            if d/AVERAGE > 2:
                
                sound.value = 0
                self.sound_pub.publish(sound)
           
                
            
        
    def calcNorm(self,current):
        
        global PREVIOUS
        
        result = current - PREVIOUS #result is an array
        
        result = result[~np.isnan(result)]
        
        result = np.absolute(result)
        
        d = np.sum(result) #should be equal to d
        
        PREVIOUS = current
        
        return d
        
        #480 rows by 1 column
    def updateAverage(self,result):
        global AVERAGE
        
        if AVERAGE == None:
            AVERAGE = result
        else:
            AVERAGE = AVERAGE *.9 + result * (1-.9)
        
        

if __name__ == "__main__":
    SentryNode()
