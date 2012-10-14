Title: Getting started with Clojurescript
tags: programming, clojure, clojurescript
Date: 2012-10-14 12:11

There doesn't seem to be much written about running Clojurescript, especially considering how great a tool it really is. I know there is [a book][orielly_book] that's coming out soon, but I had some trouble getting started with Clojurescript so I decided to put together this post, that hopefully at least some of you will find useful. This post does assume that you have some knowledge of Clojure and that you've got Leiningen already running.

To those not familiar with Clojurescript, its a Clojure compiler that targets Javascript. This simply means that it turns Clojure code into Javascript. It's like [Coffeescript][coffee]. To find out why you might want to use Clojurescript(and Clojure) check out this [talk][stuartsierra_talk].

### Getting started
As I said, you need to have Leiningen installed. For this post, I'll use Noir as the backend for a really simple app that doesn't do much. However, I'll show how you can have the app's client and server side communicate with each other, which'll make use of Noir. So, we'll just start off with a Noir project:

If you're using Lein 1:

    ::shell
    lein plugin install lein-noir 1.3.0-beta3
    lein noir new cljsintro

And if you're running Lein 2:

    ::shell
    lein new noir cljsintro

Great! Now if you `cd` into your Noir project and do `lein run` your app should run and you should be able to see the default Noir page, when you visit `http://localhost:8080` on your browser. Nothing special there. To be able to have your Clojurescript compile, we'll use the `lein-cljsbuild` plugin. To do that, you need to add a couple of things to your `project.clj`:

    ::Clojure
    (defproject cljsintro "0.1.0-SNAPSHOT"
                :description "A short intro to Clojurescript"
                :dependencies [[org.clojure/clojure "1.4.0"]
                               [noir "1.3.0-beta3"]]

                ;; Add lein-cljsbuild plugin
                :plugins [[lein-cljsbuild "0.2.8"]]

                ;; config. for cljsbuild
                :cljsbuild {
                            :builds [{
                                      :source-path "src/cljs"
                                      :compiler {
                                                 :output-to "resources/public/js/main.js"
                                                 :optimizations :whitespace
                                                 :pretty-print true}}]}
                :main cljsintro.server)

We've added 2 main things to the default `project.clj`: `:plugins` and `:cljsbuild`. The `:plugins` part is pretty self-explanatory- we just added the `lein-cljsbuild` plugin to our project. The second thing that we added, `:cljsbuild` gives the plugin the configuration necessary to compile our Clojrurescript code. Let's take a look at the configuration. Our `:builds` sequence contains only one map which means that we want all our code to compile with the same settings. Inside `:builds`, the `:source-path` tells the compiler where to look for the Clojurescript source files. And the `:output-to` tells the compiler where to put the compiled Javascript file.

Before talking about `optimizations`, lets tackle off `:pretty-print`- its pretty simple, setting it to `true` will cause the resulting JS file to have pretty-printed code, and setting-it to `false` will not. Now, to talk about optimizations- Clojurescript is compatible with with something called Google Closure(don't confuse yourself between Closure and Clojure), which optimizes Javascript code. I'm really not familiar with Google Closure, but apparently, its really powerful and will help your code load and run faster. You can set `:optimizations` to three possible values: `:whitespace`, `:simple` and `:advanced`. Here, we have set it to `:whitespace` which is the most basic level of optimization but you can set it to `:simple` and `:advanced` when pushing code to production.

### Clojurescript-ing
We've told the compiler that all our Clojurescript is to be found at `src/cljs`, so you'll need to make that directory. Also, before writing any Clojurescript, let's make a few changes to the Noir app. Open `common.clj` inside `/src/cljsintro/views` and make a few edits:

    ::Clojure
    (ns cljsintro.views.common
      (:use [noir.core :only [defpartial]]
            [hiccup.page :only [include-css include-js html5]]))

    (defpartial layout [& content]
            (html5
              [:head
               [:title "cljsintro"]
               (include-css "/css/reset.css")]
              [:body
               [:div#wrapper
                content]
               (include-js "/js/main.js")]))

I've made two changes to the default template- on line 3 I've added `include-js`, which we used on the last line to use `main.js` on our HTML files. Note that you didn't have to type in the `resources/public` where the `js` folder lies in because Noir is already looking there for static files.

Now, finally lets create a file inside the `cljs` directory called `main.cljs` and add the following:

    ::Clojure
    (ns cljs.main)

    (js/alert "Hey, there")

That's the Javascript equivalent of just `alert("Hey There");`. To compile it run

    ::shell
    lein cljsbuild once

which will compile the code just once. Alternatively if you do `lein cljsbuild auto`, the compiler will watch for changes in the source-path and re-compile when a change is made.

Run the Noir app with `lein run` and if you visit `http://localhost:8080/welcome` you should see an alert box. Cool.

### DOM
A lot of people use Javascript for manipulating the DOM- that is, adding effects like making things happen when buttons get clicked. You can do all of that stuff with Clojurescript. There are a couple of libraries available like [jayq][jayq](which is a jQuery wrapper), [domina][domina] and [enfocus][enfocus]. I've personally used enfocus because its better documented compared to the other two. These are pretty easy to use.

### Go, fetch
At the beginning I talked about making the client and server sides of our app talk to each other. Now, let's do that using a neat library called `fetch`.

The first thing we'll need to do is add `fetch` as a dependency. Strangely enough, fetch's Github Readme page doesn't tell what the latest version is and I have to go to `project.clj` to find it out. At the time of this writing its "0.1.0-alpha2", so add `[fetch "0.1.0-alpha2"]` to `:dependencies`.

Then, add these two lines to your Clojurescript file's namespace declaration:

    ::Clojure
    (:require [fetch.remotes :as remotes])
    (:require-macros [fetch.macros :as fm])

And let's create a call to a function that's on the server-side.

    ::Clojure
    (fm/remote (adder 2 3 4) [result]
      (js/alert result))

This calls a remote function on the server which looks like this:

    ::Clojure
    ;; Add (:use noir.fetch.remotes) to the namespace

    (defremote adder [& nums]
      (apply + nums))

Now recompile the Clojurescript code and refresh your browser, and you should be able to see the result of `adder` applied to the numbers we provided in a JS alert box. This is nothing special, as we could have defined `adder` in the Clojurescript code itself, but the same principle can be applied to use with functions that needs to be run on the server.

Hope you found this post useful; you can shoot out any questions on Twitter @samratmansingh or email me. Some resources that you might want to check out:

- [Chris Granger- Overtone and Clojurescript](http://www.chris-granger.com/2012/02/20/overtone-and-clojurescript/)
- [My Clojure Adventure: Intro to ClojureScript - Getting Started](http://www.myclojureadventure.com/2012/09/intro-to-clojurescript-getting-started.html)

[orielly_book]: http://shop.oreilly.com/product/0636920025139.do
[jayq]: https://github.com/ibdknox/jayq
[domina]: https://github.com/levand/domina
[enfocus]: https://github.com/ckirkendall/enfocus
[coffee]: http://coffeescript.org
[stuartsierra_talk]: https://oracleus.activeevents.com/connect/sessionDetail.ww?SESSION_ID=3242
