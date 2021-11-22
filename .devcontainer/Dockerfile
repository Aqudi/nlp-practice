FROM tensorflow/tensorflow:latest-gpu 

# Upgrade pip
RUN pip3 install --upgrade pip

# Install python pacakges
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp
