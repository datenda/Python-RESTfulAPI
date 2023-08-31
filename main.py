from flask import Flask, jsonify, request


app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': "bruh"
    },
    {
        'id': 2,
        'title': "dude"
    },
]

@app.route('/books',methods=['GET'])
def get_books():
    return jsonify(books)

@app.route('/books/<int:id>',methods=['GET'])
def get_book_by_id(id):
    for book in books:
        if book.get('id') == id:
            return jsonify(book)
        
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_by_id(id):
    altered_book = request.get_json()
    for index, book in enumerate(books):
        if book.get('id') == id:
            books[index].update(altered_book)
            return jsonify(books[index])
    return jsonify({'error': 'Book not found'}), 404

@app.route("/books_create",methods=['POST'])
def create_new_book():
    new_book = request.get_json()
    books.append(new_book)
    
    return jsonify(books)

@app.route('/books/<int:id>',methods=['DELETE'])
def delete_book(id):
    for index, book in enumerate(books):
        if book.get('id') == id:
            del books[index]
            
    return jsonify(books)

app.run(port=5000,host='localhost',debug=True)