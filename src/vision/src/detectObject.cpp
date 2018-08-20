#include <ros/ros.h>
#include <ros/package.h>
#include <sensor_msgs/Image.h>
#include <actionlib/client/simple_action_client.h>

#include <detectObject.h>

#include <boost/thread.hpp>

#include <opencv2/core/core.hpp>
#include <opencv2/highgui/highgui.hpp>
#include <opencv2/imgproc/imgproc.hpp>
#include <cv_bridge/cv_bridge.h>

#include <darknet_ros_msgs/CheckForObjectsAction.h>

typedef actionlib::SimpleActionClient<darknet_ros_msgs::CheckForObjectsAction> CheckForObjectsActionClient;
typedef std::shared_ptr<CheckForObjectsActionClient> CheckForObjectsActionClientPtr;

#include <string>
#include <cmath>

#ifdef DARKNET_FILE_PATH
std::string darknetFilePath_ = DARKNET_FILE_PATH;
#else
#error Path of darknet repository is not defined in CMakeLists.txt.
#endif

void checkForObjectsResultCB(
    const actionlib::SimpleClientGoalState& state,
    const darknet_ros_msgs::CheckForObjectsResultConstPtr& result) {
  std::cout <<  "[ObjectDetectionTest] Received bounding boxes." << std::endl;

  boundingBoxesResults_ = result->bounding_boxes;
}

bool sendImageToYolo(ros::NodeHandle nh, const std::string& pathToTestImage) {
  //!Check for objects action client.
  CheckForObjectsActionClientPtr checkForObjectsActionClient;

  // Action clients.
  std::string checkForObjectsActionName;
  nh.param("/darknet_ros/camera_action", checkForObjectsActionName, std::string("/darknet_ros/check_for_objects"));
  checkForObjectsActionClient.reset(
      new CheckForObjectsActionClient(
          nh, checkForObjectsActionName,
          true));

  // Wait till action server launches.
  if(!checkForObjectsActionClient->waitForServer(ros::Duration(20.0))) {
	  std::cout << "[ObjectDetectionTest] sendImageToYolo(): checkForObjects action server has not been advertised." << std::endl;
	  return false;
  }

  // Get test image
  cv_bridge::CvImagePtr cv_ptr(new cv_bridge::CvImage);
  cv_ptr->image = cv::imread(pathToTestImage, CV_LOAD_IMAGE_COLOR);
  cv_ptr->encoding = sensor_msgs::image_encodings::RGB8;
  sensor_msgs::ImagePtr image = cv_ptr->toImageMsg();

  // Generate goal.
  darknet_ros_msgs::CheckForObjectsGoal goal;
  goal.image = *image;

  // Send goal.
  ros::Time beginYolo = ros::Time::now();
  checkForObjectsActionClient->sendGoal(
      goal,
      boost::bind(&checkForObjectsResultCB, _1, _2),
      CheckForObjectsActionClient::SimpleActiveCallback(),
      CheckForObjectsActionClient::SimpleFeedbackCallback());

  if(!checkForObjectsActionClient->waitForResult(ros::Duration(100.0))) {
    std::cout << "[ObjectDetectionTest] sendImageToYolo(): checkForObjects action server took to long to send back result." << std::endl;
    return false;
  }
  ros::Time endYolo = ros::Time::now();
  std::cout << "[ObjectDetectionTest] Object detection for one image took " << endYolo-beginYolo << " seconds." << std::endl;
  return true;
}
