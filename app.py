from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home_page():
    html = """
    <html>
      <body>
        <h1>Home Page!</h1>
        <p>Welcome to my simple App!</p>
        <a href='/hello'>Go To Hello Page</a>
        <br>
        <a href='/goodbye'>Say Bye!</a>
      </body>
    </html>
    """
    return html


@app.route("/hello")
def say_hello():
    html = """
    <html>
      <body>
        <h1>HELLO!</h1>
        <p>This is the hello page!</p>
      </body>
    </html>
    """
    return html


@app.route("/goodbye")
def say_bye():
    return "GOODBYE!!"


@app.route("/search")
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1> Search Results For: {term}</h1> <p>Sorting By: {sort}</p>"


# @app.route("/post", methods=["POST"])
# def post_demo():
#     return "YOU MADE A POST REQUEST"


# @app.route("/post", methods=["GET"])
# def get_demo():
#     return "YOU MADE A GET REQUEST"


@app.route("/add-comment")
def add_comment_form():
    """Show form for adding a comment."""

    return """
      <h1> Add Comment</h1>
      <form method="POST">
        <input type='text' placeholder="comment" name='comment'/>
        <input type='text' placeholder="username" name='username'/>
        <button>Submit</button>
      </form>
      """


@app.route("/add-comment", methods=["POST"])
def save_comment():
    """Handles adding comment and username input"""
    comment = request.form["comment"]
    username = request.form["username"]
    return f"""
      <h1>SAVED YOUR COMMENT</h1>
      <ul>
        <li>Username: {username}</li>
        <li>Comment: {comment}</li>
      </ul>
    """


@app.route("/r/<subreddit>")
def show_subreddit(subreddit):
    return f"<h1>Browsing The {subreddit} Subreddit</h1>"


@app.route("/r/<subreddit>/comments/<int:post_id>")
def show_comments(subreddit, post_id):
    return (
        f"<h1>Viewing Comments for post {post_id} from the {subreddit} Subreddit</h1>"
    )


POSTS = {
    1: "I like chicken tenders",
    2: "I hate mayo!",
    3: "Double rainbow all the way",
    4: "Yolo OMG (end me)",
}


@app.route("/posts/<int:id>")
def find_post(id):
    """Finds post by the id within the URL"""
    post = POSTS.get(id, "POST NOT FOUND")
    return f"<p>{post}</p>"
