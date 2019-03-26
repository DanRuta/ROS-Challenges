# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "baxter_challenge: 1 messages, 1 services")

set(MSG_I_FLAGS "-Ibaxter_challenge:/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg;-Igeometry_msgs:/opt/ros/kinetic/share/geometry_msgs/cmake/../msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(baxter_challenge_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" NAME_WE)
add_custom_target(_baxter_challenge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "baxter_challenge" "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" "geometry_msgs/Quaternion:geometry_msgs/Pose:geometry_msgs/Point"
)

get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" NAME_WE)
add_custom_target(_baxter_challenge_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "baxter_challenge" "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/baxter_challenge
)

### Generating Services
_generate_srv_cpp(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/baxter_challenge
)

### Generating Module File
_generate_module_cpp(baxter_challenge
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/baxter_challenge
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(baxter_challenge_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(baxter_challenge_generate_messages baxter_challenge_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_cpp _baxter_challenge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_cpp _baxter_challenge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(baxter_challenge_gencpp)
add_dependencies(baxter_challenge_gencpp baxter_challenge_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS baxter_challenge_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/baxter_challenge
)

### Generating Services
_generate_srv_eus(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/baxter_challenge
)

### Generating Module File
_generate_module_eus(baxter_challenge
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/baxter_challenge
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(baxter_challenge_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(baxter_challenge_generate_messages baxter_challenge_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_eus _baxter_challenge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_eus _baxter_challenge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(baxter_challenge_geneus)
add_dependencies(baxter_challenge_geneus baxter_challenge_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS baxter_challenge_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/baxter_challenge
)

### Generating Services
_generate_srv_lisp(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/baxter_challenge
)

### Generating Module File
_generate_module_lisp(baxter_challenge
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/baxter_challenge
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(baxter_challenge_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(baxter_challenge_generate_messages baxter_challenge_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_lisp _baxter_challenge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_lisp _baxter_challenge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(baxter_challenge_genlisp)
add_dependencies(baxter_challenge_genlisp baxter_challenge_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS baxter_challenge_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/baxter_challenge
)

### Generating Services
_generate_srv_nodejs(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/baxter_challenge
)

### Generating Module File
_generate_module_nodejs(baxter_challenge
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/baxter_challenge
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(baxter_challenge_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(baxter_challenge_generate_messages baxter_challenge_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_nodejs _baxter_challenge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_nodejs _baxter_challenge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(baxter_challenge_gennodejs)
add_dependencies(baxter_challenge_gennodejs baxter_challenge_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS baxter_challenge_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg"
  "${MSG_I_FLAGS}"
  "/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Quaternion.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Pose.msg;/opt/ros/kinetic/share/geometry_msgs/cmake/../msg/Point.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/baxter_challenge
)

### Generating Services
_generate_srv_py(baxter_challenge
  "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/baxter_challenge
)

### Generating Module File
_generate_module_py(baxter_challenge
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/baxter_challenge
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(baxter_challenge_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(baxter_challenge_generate_messages baxter_challenge_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/msg/BlockState.msg" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_py _baxter_challenge_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/user/HS121/rw00636/baxterchallenge/src/baxter_challenge/srv/ObjectInspection.srv" NAME_WE)
add_dependencies(baxter_challenge_generate_messages_py _baxter_challenge_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(baxter_challenge_genpy)
add_dependencies(baxter_challenge_genpy baxter_challenge_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS baxter_challenge_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/baxter_challenge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/baxter_challenge
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_cpp)
  add_dependencies(baxter_challenge_generate_messages_cpp geometry_msgs_generate_messages_cpp)
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(baxter_challenge_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/baxter_challenge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/baxter_challenge
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_eus)
  add_dependencies(baxter_challenge_generate_messages_eus geometry_msgs_generate_messages_eus)
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(baxter_challenge_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/baxter_challenge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/baxter_challenge
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_lisp)
  add_dependencies(baxter_challenge_generate_messages_lisp geometry_msgs_generate_messages_lisp)
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(baxter_challenge_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/baxter_challenge)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/baxter_challenge
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_nodejs)
  add_dependencies(baxter_challenge_generate_messages_nodejs geometry_msgs_generate_messages_nodejs)
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(baxter_challenge_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/baxter_challenge)
  install(CODE "execute_process(COMMAND \"/usr/bin/python\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/baxter_challenge\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/baxter_challenge
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET geometry_msgs_generate_messages_py)
  add_dependencies(baxter_challenge_generate_messages_py geometry_msgs_generate_messages_py)
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(baxter_challenge_generate_messages_py std_msgs_generate_messages_py)
endif()
