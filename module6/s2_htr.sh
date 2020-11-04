#!/usr/bin/env bash

# Installing SimpleHTR and testing handwritten text recognition (only works with <=3.6 !!!)

git clone https://github.com/githubharald/SimpleHTR.git
cd SimpleHTR/
pip install -r requirements.txt 
cd model/
unzip model.zip 
cd ..src/
python main.py
