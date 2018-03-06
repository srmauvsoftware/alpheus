#include <ros/ros.h>
#include <alpheus_msgs/thruster.h>
#include <geometry_msgs/Pose2D.h>
#include <alpheus_msgs/pressure.h>
#include <alpheus_msgs/offsetData.h>
#include <alpheus_msgs/pressurePID.h>
#include <alpheus_msgs/headingPID.h>
#include <pid.h>

int MAX_HEADING_PID = 640;
int MIN_HEADING_PID = -640;
int MAX_PRESSURE_PID = 640;
int MIN_PRESSURE_PID = -640;
int T200MAX = 400;
int T200MIN = -400;

ros::Time t_old;
/*
alpheus_msgs::pressure pressure;
alpheus_msgs::offsetData offsetData;
*/
alpheus_msgs::thruster thruster;
ros::Subscriber pressureSub;
ros::Subscriber imuSub;
ros::Subscriber offsetSub;
ros::Subscriber pressurePIDSub;
ros::Subscriber headingPIDSub;
ros::Publisher thrusterPub;

double pressure_setpoint, pressure_value;
double heading_setpoint, heading_value;
double offsetX, offsetY;
double pKp, pKi, pKd; //Pressure Kp, Ki, Kd
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

void getPressure(const alpheus_msgs::pressure &pressure){
  pressure_value = (double)pressure.pressure;
}

void getOffset(const alpheus_msgs::offsetData &offset){
  heading_setpoint = offsetX = offset.offsetX;
  pressure_setpoint = offsetY = offset.offsetY;
}

void getHeadingPID(const alpheus_msgs::headingPID &headingPIDdata){
  hKp = headingPIDdata.hKp;
  hKi = headingPIDdata.hKi;
  hKd = headingPIDdata.hKd;
}

void getPressurePID(const alpheus_msgs::pressurePID &pressurePIDdata){
  pKp = pressurePIDdata.pKp;
  pKi = pressurePIDdata.pKi;
  pKd = pressurePIDdata.pKd;
}
// End of Subscriber Callback Functions

//Controller Function
void HeadingController(){
  ros::Time t = ros::Time::now();
  double dt = (t.nsec - t_old.nsec) / 100000000;
  PID pid = PID(dt, MAX_HEADING_PID, MIN_HEADING_PID, hKp, hKi, hKd);
  double output = pid.calculate(heading_setpoint, heading_value);
  int tVal = map(output, MIN_HEADING_PID, MAX_HEADING_PID, T200MIN, T200MAX);
  thruster.speeddir1 = 1500 - tVal;
  thruster.speeddir2 = 1500 - tVal;
}

void PressureController(){
  ros::Time t = ros::Time::now();
  double dt = (t.nsec - t_old.nsec) / 100000000;
  PID pid = PID(dt, MAX_PRESSURE_PID, MIN_PRESSURE_PID, pKp, pKi, pKd);
  double output = pid.calculate(pressure_setpoint, pressure_value);
  int tVal = map(output, MIN_PRESSURE_PID, MAX_PRESSURE_PID, T200MIN, T200MAX);
  ROS_INFO("tVal is %d\n output is %f",tVal,output);
  thruster.speedup1 = 1500 - tVal;
  thruster.speedup2 = 1500 - tVal;
  thruster.speedup3 = 1500 - tVal;
  thruster.speedup4 = 1500 - tVal;
}
//End of Controller Functions

int main(int argc, char **argv){
  ros::init(argc, argv, "pidcontroller");
  ros::NodeHandle nh;
  thrusterPub = nh.advertise<alpheus_msgs::thruster>("/thruster",1000);
  imuSub = nh.subscribe("/imu/HeadingTrue_degree", 1000, getHeading);
  pressureSub = nh.subscribe("/pressure", 1000, getPressure);
  offsetSub = nh.subscribe("/offsetData", 1000, getOffset);
  pressurePIDSub = nh.subscribe("/pressurePIDdata", 1000, getPressurePID);
  headingPIDSub = nh.subscribe("/headingPIDdata", 1000, getHeadingPID);
  thruster.speedfwd1 = 1500;
  thruster.speedfwd2 = 1500;
  thruster.speedup1 = 1500;
  thruster.speedup2 = 1500;
  thruster.speedup3 = 1500;
  thruster.speedup4 = 1500;
  thruster.speeddir1 = 1500;
  thruster.speeddir2 = 1500;

  ros::Rate r(2);
  while(ros::ok()){
    HeadingController();
    PressureController();
    thrusterPub.publish(thruster);
    ROS_INFO("Thruster Information Published From Controller");
    ros::spinOnce();
    r.sleep();
  }
  return 0;
}
