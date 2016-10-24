# pyTimeWall
A Wallpaper changer using Python, 8-bit wallpapers and Night, Twilight and Daylight times from timeanddate.com

#--------------------------------------------------
		        SETUP	
#--------------------------------------------------
The script assumes that the wallpapers and the pyTimeWall.py
script are in the same directory.

1. First you need to get the URL to pull the times for your area.

    a. Go to : http://www.timeanddate.com

    b. Click on "Sun & Moon"

    c. In the "Sun" section, type your location.  The site will use
	   completion to help make sure it can find your information
	
    d. Copy that URL and paste it in the pyTimeWall.py file.  An
	   example URL has been supplied.

2. Edit the pyTimeWall.py file

    a.  Make the pyTimeWall.py file executable (i.e. chmod a+x pyTimeWall.py)

3. Add to crontab

    a.  Open a terminal and edit cron as : crontab -e

    b.  Add an entry in cron to call the pyTimeWall.py script every hour
		i.e. 0 * * * * /path/to/TimeWall.sh >/dev/null 2&1
