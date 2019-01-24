#!/usr/bin/env python

""" 
SentryBot lets us know if an intruder walks past.

Author: Ryan Soong, Geoffrey Wright, Chris Williams, Elena Trafton
Version:
"""

import rospy

from sensor_msgs.msg import Image
from Math import abs
from cv_bridge import CvBridge, CvBridgeError
import numpy as np
global PREVIOUS
global AVERAGE
global COUNT

class SentryNode(object):
    """Monitor a vertical scan through the depth map and create an
    audible signal if the change exceeds a threshold.

    Subscribes:
         /camera/depth_registered/image
       
    Publishes:
        /mobile_base/commands/sound

    """

    def __init__(self):
        global PREVIOUS
        global AVERAGE
        global COUNT
        """ Set up the Sentry node. """
        rospy.init_node('sentry')
        self.cv_bridge = CvBridge()
        rospy.Subscriber('/camera/depth_registered/image',
                         Image, self.depth_callback, queue_size=1)
        rospy.spin()
        PREVIOUS = NULL    
        AVERAGE = NULL
        COUNT = 0
        

    def depth_callback(self, depth_msg):
        """ Handle depth callbacks. """

        # Convert the depth message to a numpy array
        depth = self.cv_bridge.imgmsg_to_cv2(depth_msg)

        # YOUR CODE HERE.
        # HELPER METHODS ARE GOOD.)
        #print (np_array.shape) #480 x 640
        slice = depth[:,320]
        
        if PREVIOUS == NULL:
            PREVOIUS = slice
        else:
            calcNorm(PREVIOUS,slide)
            
        
            
        
        
        
        
    def calcNorm(self,previous,current):
        
        
        result = current - previous #result is an array
        
        result = result[~np.isnan(result)]
        
        np.absolute(result)
        
        numpy.sum(result) #should be equal to d
        
        
        
        #480 rows by 1 column
    def updateAverage(self,result,counter):
        
        
        
        
        previous = current #this is then used for the next iteration

if __name__ == "__main__":
    SentryNode()
