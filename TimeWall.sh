#Fetch PID
pid=$(ps -C xfce4-session -o pid=)
pid=$(echo $pid)

export DBUS_SESSION_BUS_ADDRESS=$(grep -z DBUS_SESSION_BUS_ADDRESS /proc/$pid/environ|cut -d= -f2-)

# You need to edit this to match the path of pyTimeWall.py
python /home/user/pyTimeWall.py
