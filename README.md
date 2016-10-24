# pyTimeWall
A Wallpaper changer for XFCE using Python, 8-bit wallpapers and Night, Twilight and Daylight times from timeanddate.com

#--------------------------------------------------
		        SETUP	
#--------------------------------------------------
The script assumes that the wallpapers and both the .py and .sh
scripts are in the same directory.

1. First you need to get the URL to pull the times for your area.

	a. Go to : http://www.timeanddate.com/astronomy

	b. In the "Sun" section, type your location.  The site will use
	   completion to help make sure it can find your information
	
	c. Copy that URL and paste it in the pyTimeWall.py file in the "url" part at the top.  An
	   example URL has been supplied.

2. Edit the TimeWall.sh file
	a.  Here we need to change the path to the pyTimeWall.py file so that bash calls the file correctly
	b.  Make the TimeWall.sh file executable (i.e. chmod a+x TimeWall.sh)

3. Add to crontab
	a.  Open a terminal and edit cron as : crontab -e
	b.  Add an entry in cron to call the TimeWall.sh script every 15 minutes 
		i.e. */15 * * * * /path/to/TimeWall.sh >/dev/null 2&1
