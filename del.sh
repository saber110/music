#!/bin/bash
for i in $(less files.txt)
do  rm -rf $i
done
