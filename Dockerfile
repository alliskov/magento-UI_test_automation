FROM jenkins/jenkins:lts-jdk17
USER root
RUN apt-get update && apt-get -y install python3 python3-pip python3-venv
RUN apt-get update && apt-get install -y wget unzip curl
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get update && apt-get install -y google-chrome-stable
RUN git clone https://github.com/alliskov/magento-UI_test_automation.git
RUN python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip3 install --upgrade pip && \
    pip3 install -r magento-UI_test_automation/requirements.txt
ENV PATH="/venv/bin:$PATH"
