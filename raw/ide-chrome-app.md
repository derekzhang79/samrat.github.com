Title: An IDE as a packaged Chrome app
Date: 2012-08-05
tags: development environment, software, cloud, chrome

Everyone is talking about how browsers are getting more powerful. With recent developments such as Google's V8 Javascript engine, web browsers are being viewed more and more as platforms and not as mere "document viewers" to the web. The Chromebook is probably the best example I can site of this paradigm shift.

Anyways as browsers become more powerful, attempts to create development environments based on browsers have also gotten more agressive. The most notable of these attempts is probably [Light Table][lt], which is a really sleek IDE that runs on the browser. (Just to be accurate for Light Table, the actual "evaluation" of the code happens outside the browser)

Its first beta version that's called Light Table Playground was released a while back, and while the initial "pitch" had seemed really promising, **I found that programming inside the browser was not something that I enjoyed doing**. Well, I know that the guys working on Light Table are developing the tool as an in-browser tool. And I think an IDE that can talk to the Internet is the right way to go.

What I really want to see is an **IDE that acts as first-class desktop app, but can still talk to the web**, like most web apps. And yes, that would be something close to Chrome apps, but the Google Chrome team recently(it was about a month back) announced that Chrome apps are about to get an overhaul that is more along the lines of what I'm talking about:

<iframe width="560" height="315" src="http://www.youtube.com/embed/lBUGTVIJVfM" frameborder="0" allowfullscreen></iframe>

Having such an app would feel comfortable while still leveraging the power of the mighty "clouds". Since I already keep my `code/` folder inside Dropbox, I'd say that the app could take Dropbox as a "role model". The app would be available offline, but when its online it would start syncing to its servers so you can access your code anywhere.

Ideally, the app would be a one-click install which would set up your development environment exactly as you've configured. And of course, there's bonus points for modeling this around Vim :)

[lt]: http://app.kodowa.com/playground
