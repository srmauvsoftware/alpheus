#include <ros/ros.h>
#include <alpheus_msgs/thruster.h>
#include <geometry_msgs/Pose2D.h>
#include <alpheus_msgs/depth.h>
#include <alpheus_msgs/offsetData.h>
#include <alpheus_msgs/depthPID.h>
#include <alpheus_msgs/headingPID.h>
#include <pid.h>

int MAX_HEADING_PID = 640;
int MIN_HEADING_PID = -640;
int MAX_DEPTH_PID = 640;
int MIN_DEPTH_PID = -640;
int T200MAX = 400;
int T200MIN = -400;

ros::Time t_old;
alpheus_msgs::thruster thruster;
ros::Subscriber depthSub;
ros::Subscriber imuSub;
ros::Subscriber offsetSub;
ros::Subscriber depthPIDSub;
ros::Subscriber headingPIDSub;
ros::Publisher thrusterPub;

double depth_setpoint, depth_value;
double heading_setpoint, heading_value;
double offsetX, offsetY;
double pKp, pKi, pKd; //Depth Kp, Ki, Kd
double hKp, hKi, hKd; //Heading Kp, Ki, Kd

// PID Format - PID pid = PID(dt, max, min, Kp, Kd, Ki);
// pid.calculate(setpoint, value);
int map(double x, int in_min, int in_max, int out_min, int out_max){
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

// Subscriber Callback Functions
void getHeading(const geometry_msgs::Pose2D &msg){
  if( msg.theta < 0 ) heading_value = 360 + msg.theta;
  else heading_value = msg.theta;
}

void getDepth(const alpheus_msgs::depth &depth){
  depth_value = (double)depth.depth;
}

void getOffset(const alpheus_msgs::offsetData &offset){
  heading_setpoint = offsetX = offset.offsetX;
  depth_setpoint = offsetY = offset.offsetY;
}

void getHeadingPID(const alpheus_msgs::headingPID &headingPIDdata){
  hKp = headingPIDdata.hKp;
  hKi = headingPIDdata.hKi;
  hKd = headingPIDdata.hKd;
}

void getDepthPID(const alpheus_msgs::depthPID &depthPIDdata){
  pKp = depthPIDdata.pKp;
  pKi = depthPIDdata.pKi;
  pKd = depthPIDdata.pKd;
}
// End of Subscriber Callback Functions

//Controller Function
void HeadingController(){
  ros::Time t = ros::Time::now();
  double dt = (t.nsec - t_old.nsec) / 100000000;
  PID pid = PID(dt, MAX_HEADING_PID, MIN_HEADING_PID, hKp, hKi, hKd);
  double output = pid.calculate(heading_setpoint, heading_value);
  int tVal = map(output, MIN_HEADING_PID, MAX_HEADING_PID, T200MIN, T200MAX);
  //ROS_INFO("HeadingPID is %f,%f,%f",hKp, hKi, hKd);
  thruster.tfr = 1500 - tVal;
  thruster.tfl = 1500 - tVal;
  thruster.trr = 1500 - tVal;
  thruster.trl = 1500 - tVal;
}

void DepthController(){
  ros::Time t = ros::Time::now();
  double dt = (t.nsec - t_old.nsec) / 100000000;
  PID pid = PID(dt, MAX_DEPTH_PID, MIN_DEPTH_PID, pKp, pKi, pKd);
  double output = pid.calculate(depth_setpoint, depth_value);
  int tVal = map(output, MIN_DEPTH_PID, MAX_DEPTH_PID, T200MIN, T200MAX);
  //ROS_INFO("DepthPID is %f,%f,%f", pKp, pKi, pKd);
  thruster.td1 = 1500 - tVal;
  thruster.td2 = 1500 - tVal;
  thruster.td3 = 1500 - tVal;
  thruster.td4 = 1500 - tVal;
}
//End of Controller Functions

int main(int argc, char **argv){
  ros::init(argc, argv, "pidcontroller");
  ros::NodeHandle nh;
  thrusterPub = nh.advertise<alpheus_msgs::thruster>("/thruster",1000);
  imuSub = nh.subscribe("/imu/HeadingTrue_degree", 1000, getHeading);
  depthSub = nh.subscribe("/depth", 1000, getDepth);
  offsetSub = nh.subscribe("/offsetData", 1000, getOffset);
  depthPIDSub = nh.subscribe("/depthPIDdata", 1000, getDepthPID);
  headingPIDSub = nh.subscribe("/headingPIDdata", 1000, getHeadingPID);
  thruster.td1 = 1500;
  thruster.td2 = 1500;
  thruster.td3 = 1500;
  thruster.td4 = 1500;
  thruster.tfr = 1500;
  thruster.tfl = 1500;
  thruster.trr = 1500;
  thruster.trl = 1500;

  ros::Rate r(2);
  while(ros::ok()){
    HeadingController();
    DepthController();
    thrusterPub.publish(thruster);
    ROS_INFO("Thruster Information Published From Controller");
    ros::spinOnce();
    r.sleep();
  }
  return 0;
}
