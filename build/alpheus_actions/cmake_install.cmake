# Install script for directory: /home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_actions

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
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions/action" TYPE FILE FILES
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_actions/action/depth.action"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_actions/action/heading.action"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions/msg" TYPE FILE FILES
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthAction.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthActionGoal.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthActionResult.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthActionFeedback.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthGoal.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthResult.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/depthFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions/msg" TYPE FILE FILES
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingAction.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingActionGoal.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingActionResult.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingActionFeedback.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingGoal.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingResult.msg"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/alpheus_actions/msg/headingFeedback.msg"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions/cmake" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_actions/catkin_generated/installspace/alpheus_actions-msg-paths.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/include/alpheus_actions")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/roseus/ros" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/roseus/ros/alpheus_actions")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/common-lisp/ros" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/common-lisp/ros/alpheus_actions")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/gennodejs/ros" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/share/gennodejs/ros/alpheus_actions")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  execute_process(COMMAND "/usr/bin/python" -m compileall "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/lib/python2.7/dist-packages/alpheus_actions")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python2.7/dist-packages" TYPE DIRECTORY FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/devel/lib/python2.7/dist-packages/alpheus_actions")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/pkgconfig" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_actions/catkin_generated/installspace/alpheus_actions.pc")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions/cmake" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_actions/catkin_generated/installspace/alpheus_actions-msg-extras.cmake")
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions/cmake" TYPE FILE FILES
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_actions/catkin_generated/installspace/alpheus_actionsConfig.cmake"
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/alpheus_actions/catkin_generated/installspace/alpheus_actionsConfig-version.cmake"
    )
endif()

if(NOT CMAKE_INSTALL_COMPONENT OR "${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified")
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/share/alpheus_actions" TYPE FILE FILES "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/alpheus_actions/package.xml")
endif()

