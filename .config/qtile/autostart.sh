#! /bin/bash 
picom --experimental-backends &
nitrogen --restore &
~/Startup/nvidia.sh &
~/Startup/pywal.sh &
~/Startup/bootstrap.sh &
~/.config/polybar/launch.sh &
exec spotify &

