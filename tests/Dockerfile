FROM python:3.9.2
RUN wget -qO - https://packages.lunarg.com/lunarg-signing-key-pub.asc | apt-key add - &&\
    echo "deb https://packages.lunarg.com/vulkan/1.2.170 bionic main" >> /etc/apt/sources.list &&\
    apt-get update && apt-get install -y shaderc
RUN python3 -m pip install pytest
ENV PYTHONUNBUFFERED=1

WORKDIR /build
COPY glnext_compiler.cpp setup.py MANIFEST.in README.md LICENSE /build/
RUN python3 setup.py sdist
RUN python3 -m pip wheel dist/glnext-compiler-*.tar.gz
RUN python3 -m pip install glnext-compiler-*.whl

WORKDIR /tests
COPY tests /tests
CMD python3 -m pytest
