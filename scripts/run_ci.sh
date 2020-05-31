#!/bin/bash

set -eux

flake8 .
pykins job list > /dev/null
echo "Alfred: Well done sir. Excellent work"
