import roslib
import rospy
import sys
import PyKDL
from std_msgs.msg import Float64MultiArray
from geometry_msgs.msg import Pose
from geometry_msgs.msg import Quaternion
from geometry_msgs.msg import WrenchStamped

from std_srvs.srv import Empty

import numpy as np
import tf

class Dynamics:
    def s(self, x) :
        """ Given a 3D vector computes the 3x3 antisymetric matrix """
#        rospy.loginfo("s(): \n %s", x)
        ret = array([0.0, -x[2], x[1], x[2], 0.0, -x[0], -x[1], x[0], 0.0 ])
        return ret.reshape(3,3)

    
