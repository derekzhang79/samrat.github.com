Title: Building a database-backed Clojurescript app
Date: 2012-10-17 00:39
tags: clojure, clojurescript, programming

In my [previous post][getting_started], I gave a pretty quick introduction to Clojurescript. If you haven't already, I recommend you read through that post. This post assumes that you have some Clojure knowledge and already have Leiningen running.

In this post, I'll show how to create a SQL database-backed Clojurescript app(you were expecting NoSQL, weren't you?). For the lack of a better idea, I'm going to walk you through building a trivial app that helps keep track of books you've read. You can view the source code for the app [on Github][repo].

### The Setup

We'll use Noir as the back-end(with Hiccup generating the HTML); on the front-end besides using Clojurescript we'll also use a Clojurescript library called [Fetch][fetch], which makes client-server communication(as in AJAX) really easy and another one called [enfocus][enfocus] for DOM manipulation(mainly stuff like event-handling). For dealing with the database we'll use [clojure.java.jdbc][jdbc]. To compile our Clojurescript we'll use a Leiningen plugin called `lein-cljsbuild`.

So, first create a Noir project called `books`(I'm assuming you're using Leiningen 2):

    ::shell
    lein new noir books

Now, let's add some dependencies and some Clojurescript-specific settings to our `project.clj`:

    ::clojure
    (defproject books "0.1.0-SNAPSHOT"
                :description "Books- A database-backed Clojurescript app."
                :dependencies [[org.clojure/clojure "1.4.0"]
                               [noir "1.3.0-beta3"]
                               [fetch "0.1.0-alpha2"]
                               [org.clojure/java.jdbc "0.2.3"]]
                :plugins [[lein-cljsbuild "0.2.8"]]
                :cljsbuild {
                            :builds [{
                                      :source-path "src/cljs"
                                      :compiler {
                                                 :output-to "resources/public/js/main.js"
                                                 :optimizations :whitespace
                                                 :pretty-print true}}]}
                :main books.server)

If you've gone through the first post, this should be pretty self-explanatory.

### Adding a database

The first thing we're going to do is set up our database. For the sake of simplicity, in this post I'll use SQLite, however I think its safe to advise you guys not to use SQLite in production. Anyway, you'll also need to add `[org.xerial/sqlite-jdbc "3.7.2"]` to the list of dependencies.

Pull in the newly added dependency using `lein deps`, then create a file in `src/books/models` called `db.clj`. To that file add:

    ::clojure
    (ns books.models.db
      (:require [clojure.java.jdbc :as sql]))

    (def db
      {:classname   "org.sqlite.JDBC"
       :subprotocol "sqlite"
       :subname     "db/database.db"
      })

    (defn init-db []
      (try
        (sql/with-connection db
          (sql/create-table
           :books
           [:title "varchar(250)"]
           [:review "varchar(500)"]))
        (catch Exception ex
          (.getMessage (.getNextException ex)))))

We've set the path of the SQLite database to `db/database.db`, so you'll need to create a folder called `db` at the root of the project. Now, to initialize the database, run `lein repl` then

    ::clojure
    => (use 'books.models.db)
    => (init-db)

If you don't get an error the database file should have been created. You can check if its present inside `db/`. The database will have a table called `:books` with just two fields- `:title` and `:review`.

Now, we'll add some helper functions to `db.clj` to make our dealings with our database a lot simpler:

    ::clojure
    (defn add-book
      [book]
      (sql/with-connection
        db
        (sql/insert-record :books book)))

    (defn db-read-all
      []
      (sql/with-connection db
        (sql/with-query-results result
          ["SELECT * FROM books"]
          (into [] result))))

The `add-book` function does exactly what you'd expect and the code should be pretty easy to understand. The argument to the function should be a Clojure hash-map, so a call to that function would look like:

    ::clojure
    (add-book {:title "Clojure Programming" :review "Great book. I really need to work on completing this one, though."})

The `db-read-all` function pulls all entries from the `:books` table and returns a vector of the entries.

### Views

Now, we'll work on our views. Open `src/books/views/welcome.clj` to edit it. This is what it should look like:

    ::clojure
    (ns books.views.welcome
      (:require [books.views.common :as common])
      (:use [noir.core :only [defpage]]
            books.models.db
            noir.fetch.remotes
            hiccup.form))

    (defpage "/" []
             (common/layout
              [:h1 "Books"]
              [:div
               (label {} "title" "Title: ")
               (text-field {:class "title"} "title")
               [:br]
               (label {} "review" "Review: ")
               (text-area  {:class "review"} "review")
               [:br]
               [:button {:class "submit"} "Submit"]]))

    (defremote add-book-to-db [book]
      (println book)
      (add-book book))

The most important part of this is the `defremote` definition. Its defining a `fetch` remote, which simply calls the `add-book` function from the `books.models.db` namespace that we defined above. The little `println` call is simply there to help us see in a short while whether our program is working.

### Client-side

Now, we finally get to writing some Clojurescript code. Create a new file inside `src/cljs/main.cljs` and into it type in the following:

    ::clojure
    (ns books.cljs.main
      (:require [enfocus.core :as ef]
                [fetch.remotes :as remotes])
      (:require-macros [enfocus.macros :as em]
                       [fetch.macros :as fm]))

    (defn get-book-title []
      (em/from (em/select ["#title"]) (em/get-prop :value)))

    (defn get-book-review []
      (em/from (em/select ["#review"]) (em/get-prop :value)))

    (defn get-book-data []
      {:title (get-book-title)
       :review (get-book-review)})

    (defn push-book []
      (fm/remote (add-book-to-db (get-book-data))))

    (em/defaction setup []
      [".submit"] (em/listen :click push-book))

    (set! (.-onload js/window) setup)

In the namespace declaration you'll notice that we're bringing in stuff into our namespace from the Clojurescript libraries that we talked about in the beginning- Fetch and Enfocus. You've already seen how the server-side of our Fetch remote works, now you'll see how the other half of it, the client-side works.

Starting from the top, the two functions `get-book-title` and `get-book-review` use enfocus to extract the value of the "title" and "review" fields in the browser. Read the enfocus docs to find out exactly how that works.

The function `get-book-data` simply puts the title and review into a Clojure map and returns it. `push-book` then pushes this map to the remote function we defined in our `welcome.clj` file.

The next block of code sets up a listener that calls the `push-book` function if the submit button is clicked. And the last line loads this listener when the web page loads.

Compile the Javascript using `lein cljsbuild once` and make sure you've added the Javascript file to your template(in `common.clj`). If you visit the browser now, you should see the form as expected. Fill in the title and review and hit "Submit". And what happens? Nothing! Well, actually something does happen. If everything worked fine, the little `println` call in our remote function should have printed out some text in the process where you're running the Noir server. Also, if you try running the `db-read-all` function we defined, you should see that a book was in fact added when you hit "Submit".

Congratulations! You've created a Clojurescript application backed by a database. I know its a really trivial app, stupid even but I do hope this post helped at least a few people get started with Clojurescript. And if you are interested in moving forward with this app, here are a few thoughts:

- Show a list of the books already added. Should be quite trivial to add using the `db-read-all` function.
- Search shouldn't be too difficult to add either. You'll probably want to add another helper function in `db.clj`
- Make the text fields clear up when the user hits "Submit"- for this you'll want to read up on the [enfocus][enfocus] docs.

[getting_started]: http://samrat.me/blog/2012/10/getting-started-with-clojurescript
[fetch]: https://github.com/ibdknox/fetch
[enfocus]: https://github.com/ckirkendall/enfocus
[jdbc]: https://github.com/clojure/java.jdbc
[repo]: https://github.com/samrat/books-cljs-tutorial
