Title: Videodropper- Behind the scenes
Date: 2011-10-21 18:15
Tags: dropbox, youtube, webapps, projects

My [previous post][videodropper post] about my new web app- [Videodropper][videodropper], which lets you send Youtube videos to your Dropbox account got quite huge on Hacker News yesterday(At least, much more than I'd anticipated). So, I decided to write another post about Videodropper on how it works.

Videodropper is powered by [Python][python], [Flask][flask], [Redis][redis] and [Celery][celery]. It is hosted on [Epio][epio](as you might have guessed from the ep.io subdomain). All the downloading is handled by [youtube-dl][youtubedl] and of course, the uploading is done using the Dropbox API. 
<br/><br/>
## Basics ##
What happens when you press the "Send to Dropbox" button is that Videodropper gets the Youtube video URL(playlists won't work, more on that later), and it queues it up on a Celeryd process; when the download starts, another process also starts that monitors the size of the video file so that it doesn't cross the upload limit. So, that's two processes for one file download. Currently, Videodropper runs only four processes which means that it can process only two videos at a time. Up until now, these modest resources have served quite well, as the download and upload speed is pretty high. However, the Celery instance, which is limited to 128MB of memory runs out of memory when Videodropper starts getting a lot of requests. 

When Celery starts a task which in this case is a "download, then upload", youtube-dl starts downloading the Youtube video which, as I mentioned above happens quite fast. Then, if the size hasn't exceeded Dropbox's upload limit(which is 150MB now, but it should soon be upgraded to 300MB), the upload process begins. That's basically the core functionality of the app. Oh, and if you choose to optimize the video for iPhone, youtube-dl simply downloads the .mp4 file(Youtube format=18) of the video, no transcoding takes place.
<br/><br/>
## Size monitoring ##

One obvious optimization for Videodropper is the size-monitoring as you've seen that it eats up a whole process. One solution would have been to find out the file size before downloading, but I couldn't find any way to do that(if you happen to know of any please, please tell me about it.)
<br/><br/>
## Playlist support ##

I've got some requests for Videodropper to start supporting playlists which is quite a reasonable request, given that Playlists is a huge part of Youtube. However, at present supporting playlists is just not an option. As I've mentioned above, Videodropper runs on a very modest server configuration and downloading playlists would surely cause Videodropper to run out of memory. The limits on the server resources are mostly because Videodropper is a free app, so I am not able to invest much money on it, so if you're interested in supporting Videodropper you could [donate some money on Flattr][flattr] to help upgrade Videodropper's server capacity.

In a nutshell, Flask serves the website, Celery queues up the download tasks(and also a size monitoring task) and Redis is used mostly as a backend to Celery, but also for storing the "Recent Downloads" of the user. That's it. If you have any query or suggestion feel free to shoot them at the comments below. 

[videodropper post]: http://samrat.github.com/blog/videodropper.html
[videodropper]: http://videodropper.ep.io
[python]: http://python.org
[flask]: http://flask.pocoo.org
[redis]: http://redis.io
[celery]: http://celeryproject.org
[epio]: http://ep.io
[flattr]: https://flattr.com/thing/414622/Videodropper
[youtubedl]: https://github.com/rg3/youtube-dl
