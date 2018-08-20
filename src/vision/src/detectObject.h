#ifndef DETECTOBJECT
#define DETECTOBJECT

// ROS
#include <ros/ros.h>
#include <ros/package.h>
#include <sensor_msgs/Image.h>
#include <actionlib/client/simple_action_client.h>

// boost
#include <boost/thread.hpp>

// OpenCV2.
#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <cv_bridge/cv_bridge.h>

// Actions.
#include <darknet_ros_msgs/CheckForObjectsAction.h>

typedef actionlib::SimpleActionClient<darknet_ros_msgs::CheckForObjectsAction> CheckForObjectsActionClient;
typedef std::shared_ptr<CheckForObjectsActionClient> CheckForObjectsActionClientPtr;

// c++
#include <string>
#include <cmath>

#ifdef DARKNET_FILE_PATH
std::string darknetFilePath_ = DARKNET_FILE_PATH;
#else
#error Path of darknet repository is not defined in CMakeLists.txt.
#endif

darknet_ros_msgs::BoundingBoxes boundingBoxesResults_;

bool sendImageToYolo(ros::NodeHandle nh, const std::string& pathToTestImage);

#endif
