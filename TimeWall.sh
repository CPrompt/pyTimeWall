#Fetch PID
pid=$(ps -C xfce4-session -o pid=)
pid=$(echo $pid)


export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$pid/environ|cut -d= -f2-)

python /home/curtis/Scripts/time_wall_changer/pyTimeWall.py
