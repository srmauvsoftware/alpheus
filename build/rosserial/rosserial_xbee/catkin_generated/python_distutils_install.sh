#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/rosserial/rosserial_xbee"

# snsure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/install/lib/python2.7/dist-packages:/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build" \
    "/usr/bin/python" \
    "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/src/rosserial/rosserial_xbee/setup.py" \
    build --build-base "/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/build/rosserial/rosserial_xbee" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/install" --install-scripts="/home/pushkalkatara/Desktop/PUbuntu/AUV/alpheus/install/bin"
