#!/bin/bash

gnome-terminal -- bash -c "roscore; bash"
gnome-terminal -- bash -c "rosrun translate ja.py; bash"
gnome-terminal -- bash -c "rosrun translate de.py; bash"
gnome-terminal -- bash -c "rosrun translate es.py; bash"
gnome-terminal -- bash -c "rosrun translate fr.py; bash"
gnome-terminal -- bash -c "rosrun translate zh.py; bash"
gnome-terminal -- bash -c "rosrun translate ko.py; bash"
gnome-terminal -- bash -c "rosrun translate random.py; bash"
