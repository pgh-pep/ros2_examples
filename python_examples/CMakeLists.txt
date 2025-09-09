cmake_minimum_required(VERSION 3.8)
project(python_examples)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake_auto REQUIRED)
ament_auto_find_build_dependencies()

ament_python_install_package(${PROJECT_NAME})

# Python Nodes:
install(PROGRAMS
    ${PROJECT_NAME}/base_py_node.py
    ${PROJECT_NAME}/example_client.py
    ${PROJECT_NAME}/example_publisher.py
    ${PROJECT_NAME}/example_subscriber.py
    ${PROJECT_NAME}/example_server.py
    ${PROJECT_NAME}/example_action_client.py
    ${PROJECT_NAME}/example_action_service.py
    # ${PROJECT_NAME}/base_py_node.py
    DESTINATION lib/${PROJECT_NAME}
)

# ament_auto_package(
#     USE_SCOPED_HEADER_INSTALL_DIR
#     INSTALL_TO_SHARE launch 
# )