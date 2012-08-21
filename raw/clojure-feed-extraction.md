Title: Extracting feed articles in Clojure
Date: 2012-08-21 21:10
tags: clojure, programming

I'm reading [**Programming Collective Intelligence**][pci] by [**Toby Segaran**][kiwitobes] and doing the examples in Clojure. *Chapter 3* in the book shows you how to cluster similar blogs together using word-frequencies generated from their feeds. 

Now, some blogs annoyingly give out just a link to the post or just a short blurb of the post in their feeds. That proved to be a major annoyance but I found a workaround to deal with it, which I will describe in this post. 

*(By the way, if you have a blog that publishes just links or blurbs, please consider changing your feed settings; you'll make a lot of people reading your blog using a feed reader, and a few programmers a lot happier)*

I used [**feedparser-clj**][feedparser] to parse feeds in order to grab the whole article from the feed, I used [Goose][goose], which is a Scala library. Because of this, you can't simply start using Goose by just adding it as a Leiningen dependency. Thankfully, there is a tool, [`lein-localrepo`][localrepo] that greatly simplifies installing Leiningen or Maven repos from a local file(as opposed to from clojars.org). After installing localrepo, you need to install Goose:

	::
	lein localrepo coords <path-to-jar-file>

Which will give you something like `goose/target/goose-2.1.19.jar goose/goose 2.1.19`. Now, to actually install it:

	::
	lein localrepo install goose/target/goose-2.1.19.jar goose/goose 2.1.19

Then, add `[com.gravity/goose "2.1.19"]` to your project dependencies. Now, if you open a REPL in the project dir(using `lein repl`), you should be able to import stuff from Goose:

	::clojure
	import (com.gravity.goose Goose Configuration Article))

To extract the article from a URL, type in a function:

	::clojure
	(defn extract-article
	"Extracts the article from url."
	[url]
	(let [url     url
        goose   (Goose. (Configuration.))
        article (.extractContent goose url)]
			(.cleanedArticleText article)))

Next, we will extract a list of blog post URLs:

	::clojure
	(use '[feedparser-clj :exclude (-main)])

	(defn articles-list
	[feed-url]
	(let [parsed (parse-feed feed-url)]
		(map :link (:entries parsed))))

Finally, to get all the extracted articles from a feed, you can map `extract-article` to a list of article URLs:

	::clojure
	(map extract-article (articles-list "http://samrat.me/feeds/all.xml"))

I hope that helped clear out or avoid at least some confusion. You can shoot out any queries or feedback to [@samratmansingh][tweet]

[pci]: http://shop.oreilly.com/product/9780596529321.do
[kiwitobes]: http://kiwitobes.com/
[goose]: https://github.com/jiminoc/goose
[feedparser]: https://github.com/scsibug/feedparser-clj
[localrepo]: https://github.com/kumarshantanu/lein-localrepo
[tweet]: http://twitter.com/samratmansingh
