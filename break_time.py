import webbrowser
import time

breaks = 0
maxbreaks = 3

while (breaks < maxbreaks):
  time.sleep(90)
  print "The video was played at:" + time.ctime()

  url = "https://www.youtube.com/watch?v=x6ggW8ei0yU";

  new = 2

  webbrowser.open(url, new = new)
  breaks = breaks + 1