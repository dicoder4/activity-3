from flask import Flask, render_template, request
from services.book_service import BookService
from services.user_service import UserService

app = Flask(__name__)

book_service = BookService()
user_service = UserService()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add-book", methods=["GET", "POST"])
def add_book():
    if request.method == "POST":
        title = request.form["title"]
        author = request.form["author"]
        isbn = request.form["isbn"]
        book_service.add_book(title, author, isbn)
        return "Book added successfully!"
    return render_template("add_book.html")

@app.route("/remove-book", methods=["POST"])
def remove_book():
    isbn = request.form["isbn"]
    book_service.remove_book(isbn)
    return "Book removed successfully!"

@app.route("/search-books", methods=["GET"])
def search_books():
    query = request.args.get("query")
    results = book_service.search_books(query)
    return render_template("search_books.html", results=results)

@app.route("/borrow-book", methods=["POST"])
def borrow_book():
    user_id = request.form["user_id"]
    isbn = request.form["isbn"]
    user_service.borrow_book(user_id, isbn)
    return "Book borrowed successfully!"

@app.route("/return-book", methods=["POST"])
def return_book():
    user_id = request.form["user_id"]
    isbn = request.form["isbn"]
    user_service.return_book(user_id, isbn)
    return "Book returned successfully!"

@app.route("/view-users")
def view_users():
    users = user_service.get_all_users()
    return render_template("view_users.html", users=users)

if __name__ == "__main__":
    app.run(debug=True)
