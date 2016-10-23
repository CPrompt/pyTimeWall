from bs4 import BeautifulSoup
import requests
import time
import datetime
import os

'''-----------------------------------------------------------------------
				Configure these two and that's it!
-----------------------------------------------------------------------'''

walls = [
	"9-Late-Night.png","1-Early-Morning.png","2-Morning.png","3-Late-Morning.png","4-Afternoon.png","5-Late-Afternoon.png","6-Evening.png","7-Late-Evening.png","8-Night.png"
	]

'''
	Go to this site: http://www.timeanddate.com
	Find your location
	Copy the URL and paste
	Below is my example
'''
url = "http://www.timeanddate.com/astronomy/usa/greensboro"

'''-----------------------------------------------------------------------
				End Configuration
-----------------------------------------------------------------------'''

#get current working directory
current_path = os.path.dirname(os.path.realpath(__file__))
current_path = current_path + "/"
#TESTING
print ("Current path is : %s"%current_path + '\n')

r = requests.get(url)

soup = BeautifulSoup(r.content,"lxml")

#get the table id lm-key
g_data = soup.find("table",{"id" : "lm-key"})

#get the td:class=tr rows
rows = g_data.findAll("td",{"class" : "tr"})

# TESTING
print(rows)

times = [] #initiate a list to put the time into

#parse out the data in each td class="tr"
for row in rows:
	data = row.get_text()
	data = data.encode("utf-8")
	data = data[:8]	#this just strips out the first chunck since that's all we need
	times.append(data.rstrip(' '))

#TESTING
print(times)

new_times = []
for time_format in times:
	newTime = time.strftime("%H:%M", time.strptime(time_format, "%I:%M %p"))
	new_times.append(newTime)
#TESTING
#print new_times
#print " "

#get todays time
my_time = time.strftime("%H:%M")

#TESTING
#print "The Time is now : %s"%my_time + '\n'

for k in range(8,0,-1):
	if my_time >= new_times[k]:
		#print "Time stops here : %s"%new_times[k]
		#print "The wall would be : %s"%walls[k]
		#TESTING
		#print "Setting the wallpaper to : %s"%current_path + walls[k]
                #  This is for the xfce DM
		#os.system('xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor0/image-path -s %s%s'%(current_path,walls[k]))
		#os.system('xfconf-query -c xfce4-desktop -p /backdrop/screen0/monitor1/image-path -s %s%s'%(current_path,walls[k]))
                os.system('feh --bgcenter --noxinerama %s%s'%(current_path,walls[k]))
                break
