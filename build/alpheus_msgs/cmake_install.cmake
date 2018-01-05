# Install script for directory: /home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/install")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_msgs/msg" TYPE FILE FILES
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs/msg/thruster.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs/msg/pressure.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs/msg/offsetData.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs/msg/headingPID.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs/msg/pressurePID.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_msgs/cmake" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_msgs/catkin_generated/installspace/alpheus_msgs-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/include/alpheus_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/roseus/ros/alpheus_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/common-lisp/ros/alpheus_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/gennodejs/ros/alpheus_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/lib/python2.7/dist-packages/alpheus_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/lib/python2.7/dist-packages/alpheus_msgs")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_msgs/catkin_generated/installspace/alpheus_msgs.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_msgs/cmake" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_msgs/catkin_generated/installspace/alpheus_msgs-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_msgs/cmake" TYPE FILE FILES
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_msgs/catkin_generated/installspace/alpheus_msgsConfig.cmake"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_msgs/catkin_generated/installspace/alpheus_msgsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_msgs" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_msgs/package.xml")
endif()

