#!/bin/bash



# Define the URL of the Oracle JDK 11 tar.gz file
JDK_FILENAME="amazon-corretto-17-x64-linux-jdk.tar.gz"
JDK_URL="https://corretto.aws/downloads/latest/${JDK_FILENAME}"

# Define the directory to download JDK into
DOWNLOAD_DIR="/tmp"

# Define the directory to install JDK into
JAVA_INSTALL_DIR="$HOME/jdk"

# Download JDK tar.gz file
echo "Downloading JDK..."
wget --no-check-certificate --no-cookies --header "Cookie: oraclelicense=accept-securebackup-cookie" -P $DOWNLOAD_DIR $JDK_URL

# Extract JDK tar.gz file
echo "Extracting JDK..."
mkdir -p $JAVA_INSTALL_DIR
tar -xf "${DOWNLOAD_DIR}/${JDK_FILENAME}" -C $JAVA_INSTALL_DIR --strip-components=1

# Add JDK to PATH and set JAVA_HOME
echo "Updating PATH and JAVA_HOME..."
echo "export PATH=\$PATH:$JAVA_INSTALL_DIR/bin" >> $HOME/.bashrc
echo "export JAVA_HOME=$JAVA_INSTALL_DIR" >> $HOME/.bashrc

# Source the .bashrc file to apply changes to the current shell
source ~/.bashrc

# Verify Java installation
echo "Java installation complete. Verifying..."
java -version



# Define the URL of the Ghidra release
#GHIDRA_VERSION="11.0.3_PUBLIC"
#GHIDRA_URL="https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_${GHIDRA_VERSION}/ghidra_${GHIDRA_VERSION}_PUBLIC.zip"
GHIDRA_FILENAME="ghidra_11.0.3_PUBLIC_20240410.zip"
GHIDRA_URL="https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_11.0.3_build/${GHIDRA_FILENAME}"

# Define the directory to download Ghidra into
DOWNLOAD_DIR="/tmp"

# Define the directory to install Ghidra into
GHIDRA_INSTALL_DIR="$HOME/ghidra"

# Download Ghidra zip file
echo "Downloading Ghidra..."
wget -P $DOWNLOAD_DIR $GHIDRA_URL

# Extract Ghidra zip file
echo "Extracting Ghidra..."
unzip -q "${DOWNLOAD_DIR}/${GHIDRA_FILENAME}" -d $GHIDRA_INSTALL_DIR

# Change directory to Ghidra installation directory
cd $GHIDRA_INSTALL_DIR

# Run Ghidra
echo "Running Ghidra..."
./ghidraRun