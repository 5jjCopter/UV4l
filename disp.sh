#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M%S")
raspistill -vf -hf -o /media/fotostaller/$DATE.jpg
