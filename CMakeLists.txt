cmake_minimum_required(VERSION 3.16)
project(lgl-scxctl-manager VERSION 1.0.0 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

find_package(Qt6 REQUIRED COMPONENTS Core Widgets)

add_executable(lgl-scxctl-manager
    main.cpp
    mainwindow.cpp
    mainwindow.h
    resources.qrc
)

target_link_libraries(lgl-scxctl-manager PRIVATE Qt6::Core Qt6::Widgets)

# Enable warnings. Add -Werror here once all warnings are clean.
target_compile_options(lgl-scxctl-manager PRIVATE
    $<$<CXX_COMPILER_ID:GNU,Clang>:-Wall -Wextra -Wpedantic>
)

install(TARGETS lgl-scxctl-manager DESTINATION bin)
install(FILES lgl-scxctl-manager.desktop DESTINATION share/applications)
install(FILES packaging/lgl-scxctl-manager_icon.png
        DESTINATION share/icons/hicolor/256x256/apps
        RENAME lgl-scxctl-manager.png)
