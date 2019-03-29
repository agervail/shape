FROM ubuntu:18.04
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata && \
    apt-get install -y --no-install-recommends python python-pip python-setuptools \
    software-properties-common && \
    add-apt-repository ppa:freecad-maintainers/freecad-stable && \
    apt-get install -y --no-install-recommends freecad && \
    pip install wheel && \
    pip install progressbar svgpathtools && \
    ln -s /usr/share/freecad/Ext /usr/lib/freecad-python2/Ext && \
    ln -s /usr/share/freecad/Gui /usr/lib/freecad-python2/Gui && \
    ln -s /usr/share/freecad/Mod /usr/lib/freecad-python2/Mod && \
    ln -s /etc/alternatives/freecadlib /usr/lib/freecad-python2/lib
RUN apt-get install -y --no-install-recommends imagemagick librsvg2-bin
COPY config/policy.xml /etc/ImageMagick-6/policy.xml
WORKDIR /ShapeDetector
