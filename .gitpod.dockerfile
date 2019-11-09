FROM gitpod/workspace-full
RUN pip3 install pytest pytest-cov
RUN wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && sudo dpkg -i packages-microsoft-prod.deb
RUN sudo apt-get update && sudo apt-get install apt-transport-https && sudo apt-get update && sudo apt-get install dotnet-sdk-3.0 --yes
RUN sudo apt-get update -q && \
    sudo apt-get install -yq libtinfo5 libcurl4-openssl-dev libncurses5 && \
    sudo rm -rf /var/lib/apt/lists/*

# Install Swift
RUN mkdir -p /home/gitpod/.swift && \
    cd /home/gitpod/.swift && \
    curl -fsSL https://swift.org/builds/swift-5.1-release/ubuntu1804/swift-5.1-RELEASE/swift-5.1-RELEASE-ubuntu18.04.tar.gz | tar -xzv
ENV PATH="$PATH:/home/gitpod/.swift/swift-5.1-RELEASE-ubuntu18.04/usr/bin"
RUN sudo apt-get update && sudo apt-get install apt-transport-https && sudo apt-get update && sudo apt-get install dotnet-sdk-3.0 mono-complete --yes
