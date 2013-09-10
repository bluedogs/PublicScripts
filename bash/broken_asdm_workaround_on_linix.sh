#!/bin/bash

COMMAND=$(javaws -verbose -Xnosplash asdm.jnlp | grep -v "Java(TM) Web Start");

$COMMAND

