#!/bin/bash

gnome-terminal -- bash -c "roscore; bash"
gnome-terminal -- bash -c "rosrun translate ja.py; bash"
gnome-terminal -- bash -c "rosrun translate en.py; bash"
