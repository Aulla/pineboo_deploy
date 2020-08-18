#!/bin/bash
TARGET="linux-64"
QMAKE_EXEC="/opt/Qt5.15.0/5.15.0/gcc_64/bin/qmake"
python3 ./build-pineboo.py --target $TARGET  --qmake $QMAKE_EXEC --verbose



