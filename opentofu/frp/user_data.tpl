#!/bin/bash

set -e

yum update -y
amazon-linux-extras install ansible2 -y
