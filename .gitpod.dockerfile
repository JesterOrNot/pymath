FROM gitpod/workspace-full
RUN pip3 install pytest pytest-cov
RUN wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb && sudo dpkg -i packages-microsoft-prod.deb
RUN sudo apt-get update && sudo apt-get install apt-transport-https && sudo apt-get update && sudo apt-get install dotnet-sdk-3.0 mono-complete --yes