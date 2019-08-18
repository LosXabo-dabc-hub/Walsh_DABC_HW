# 1 To create a server, we need to import Flask
from flask import Flask

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
# We use `@app.route` to associate an endpoint/URL (`/`, or `/about`) with the result of a function call
# (of `home` or `about`, respectively).

# Now, let us hit each route in our browser.

#   a. Notice that, in the _terminal_, we see the results of the `print` message,
#       but not trace of the string we `return` to the client.

#   b. In the browser, we see the string the request handler _returns_,
#       but no trace of the call to `print`.

#   c. This essentially illustrates the relationship between the client—which receives a request handler's return value
#       and the server where the functions associated with the response to a request are actually executed.
@app.route("/")
def home():
    print("Server received request for 'Home' page...")
    return "Welcome to my 'Home' page!"


# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    print("Server received request for 'About' page...")
    return "Welcome to my 'About' page!"


# Lastly, use `if __name__ == "__main__"` to define "main" behavior.
# See https://stackoverflow.com/questions/419163/what-does-if-name-main-do for a deeper explanation
# `app.run` is all we need to do to start the development server.
# Passing `debug=True` makes development much easier, but in production,
# best practices demand that `debug` must **always** be false.

if __name__ == "__main__":
    app.run(debug=True)
