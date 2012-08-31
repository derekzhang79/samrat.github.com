Title: How to add Reading Time to your website or blog
Date: 2012-08-31 9:00
tags: programming, projects, api,

A few days ago I released [Reading Time][rt], a small Noir web app that tells you how long it will take for you to read an online article. The front-facing web app is pretty simple to use- just copy the URL of an article, paste it into Reading Time and it'll tell you how long you'll probably need to read the article. 

<a href="http://imgur.com/IITRk"><img src="http://i.imgur.com/IITRk.png?1" title="Reading Time" alt="" width='675px'/></a>

So, instead I'm going to go through how to embed Reading Time into your blog or website, so you can tell your readers how long they will take to read an article. The original inspiration for Reading Time was [Swizec][swizec]'s blog post- [Services I want to pay for][swiz-blog] which lists the idea as **"Tell my users how long they are likely to take reading a story"** so I had been working on an API along with the web app right from the beginning. 

## The API

The API is dead simple. Send a GET request to `http://reading-time.samrat.me/api` with just `url` as a parameter and you'll get a JSON message. If JSONP is required, send a `callback` argument too.

The URL should look like this:

	::
	http://reading-time.samrat.me/api?url=http://samrat.me/blog/2011/08/newsblur-an-awesome-alternative-to-google-reader&callback=?

This is what the responses look like:

	::bash
	$ curl http://reading-time.samrat.me/api?url=http://samrat.me/blog/2011/08/newsblur-an-awesome-alternative-to-google-reader&callback=?
	?({"minutes":1.0160000324249268,"readable":"1 minutes, 0 seconds"})
	
	$ curl http://reading-time.samrat.me/api?url=http://samrat.me/blog/2011/08/newsblur-an-awesome-alternative-to-google-reader
	{"minutes":1.0160000324249268,"readable":"1 minutes, 0 seconds"}

## Embedding Reading Time

To embed Reading Time on this site, I'm using this short script that makes use of jQuery:

	::javascript
	$.getJSON("http://www.reading-time.samrat.me/api?url=" + location.href + "&callback=?",
	{},
	function(data) {
	  $("div.rt_readable").append("Reading Time: ");
	  $("div.rt_readable").append(data.readable);
	});

The script is also available at [http://www.reading-time.samrat.me/js/embed_rt.js][js], so you can add it to your site by just adding a `<script>` pointing to that link. Note that you'll also need to add [jQuery][jq] to your site *before* this script.

Now, all you need to do is add `<div class='rt_readable'> </div>` where you want Reading Time to appear. And when the page loads, you should see the Reading Time of the page. 

[rt]: http://reading-time.samrat.me
[swizec]: http://swizec.com
[api]: http://reading-time.samrat.me/api?url=http://samrat.me/blog/2011/08/newsblur-an-awesome-alternative-to-google-reader&callback=?
[swiz-blog]: http://swizec.com/blog/services-i-want-to-pay-for/swizec/5158
[js]: http://www.reading-time.samrat.me/js/embed_rt.js
[jq]: http://jquery.com
