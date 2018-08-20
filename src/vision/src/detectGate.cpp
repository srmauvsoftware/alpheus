#include <detectObject.h>

void main(){
  srand((unsigned int) time(0));
  ros::NodeHandle nodeHandle("~");

  cv_bridge::CvImagePtr cv_ptr(new cv_bridge::CvImage);
  cv_ptr->image = cv::imread(pathToTestImage, CV_LOAD_IMAGE_COLOR);
  cv_ptr->encoding = sensor_msgs::image_encodings::RGB8;
  sensor_msgs::ImagePtr image = cv_ptr->toImageMsg();

  sendImageToYolo(nodeHandle, gateImage);

  bool detectedGate = false;
  double centerErrorGate;

  for(unsigned int i = 0; i < boundingBoxesResults_.bounding_boxes.size(); ++i) {
    double xPosCenter = boundingBoxesResults_.bounding_boxes.at(i).xmin +
        (boundingBoxesResults_.bounding_boxes.at(i).xmax - boundingBoxesResults_.bounding_boxes.at(i).xmin) * 0.5;
    double yPosCenter = boundingBoxesResults_.bounding_boxes.at(i).ymin +
        (boundingBoxesResults_.bounding_boxes.at(i).ymax - boundingBoxesResults_.bounding_boxes.at(i).ymin) * 0.5;

    if(boundingBoxesResults_.bounding_boxes.at(i).Class == "gate") {
      detectedGate = true;
      //std::cout << "centerErrorPerson  " << xPosCenter << ", " <<  yPosCenter << std::endl;
      centerErrorPerson = std::sqrt(std::pow(xPosCenter - 228.0, 2) + std::pow(yPosCenter - 238.0, 2));
    }
}
