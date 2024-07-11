import pytest
from app import *

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_hello_world(client):
    response = client.get('/')
    json_data = response.get_json()

    assert response.status_code == 200
    assert json_data['message'] == 'Hello World!'


# *********************test for book routes *********************
def test_create_book(client):
    response = client.post('/book', json={
        "book_isbn" : "8763",
        "genre_id" : 24,
        "author_id" : 2,
        "title" : "titulo test 1",
        "stock" : 234
    })
    response3 = client.post('/book', json={
        "book_isbn": "8763",
        "genre_id": 24,
        "author_id": 2,
        "title": "titulo test 1",
        "stock": "wersd"
    })
    response2 = client.post('/book', json={})
    json_data = response.get_json()
    json_data2 = response2.get_json()
    json_data3 = response3.get_json()

    assert response.status_code == 201
    assert json_data['message'] == 'the book was added successfully'
    assert json_data['book added'] == ("{'author_id': 2, 'book_isbn': '8763', 'genre_id': 24, 'stock': 234, 'title': "
 "'titulo test 1'}")
    assert response2.status_code == 406
    assert json_data2['error'] == 'books_isbn, genre_id, author_id, title and stock cannot be null'
    assert response3.status_code == 400
    assert json_data3['error message'] == 'an error ocurred while saving the book'

def test_get_all_books(client):
    response = client.get('/book')
    assert response.status_code == 200

def test_get_book_by_id(client):
    book = {
    'author_id': {
        'author': '<Author - 2 - author updated - last name upd- USA - ''female - None>'},
     'book_isbn': 8763,
     'genre_id': {'genre': '<Genre - 24 - TEST - the genre is a comedy>'},
     'pages': None,
     'price': None,
     'publication_date': None,
     'stock': 234,
     'stock_added_date': None,
     'title': 'titulo test 1'}
    response = client.get('/book/8763')
    response2 = client.get('/book/234234456')
    json_data = response.get_json()
    json_data2 = response2.get_json()

    assert response.status_code == 200
    assert response2.status_code == 404
    assert json_data == book
    assert json_data2['error'] == 'book not found'

def test_update_book(client):
    response = client.put('/book/8763', json={
        "book_isbn": "8763",
        "genre_id": 24,
        "author_id": 2,
        "title": "titulo test 1 updated",
        "stock": 2342
    })
    response2 = client.put('/book/9634', json={})
    response3 = client.put('book/8763', json={})
    response4 = client.put('book/8763', json={
        "book_isbn": "8763",
        "genre_id": "asdfwer",
        "author_id": 2,
        "title": "titulo test 1 updated",
        "stock": 2342
    })

    json_data = response.get_json()
    json_data2 = response2.get_json()
    json_data3 = response3.get_json()
    json_data4 = response4.get_json()

    assert response.status_code == 200
    assert response2.status_code == 404
    assert response3.status_code == 406
    assert response4.status_code == 400
    assert json_data['message'] == 'the book was updated successfully'
    assert json_data2['error'] == 'book not found'
    assert json_data3['error'] == 'books_isbn, genre_id, author_id, title and stock cannot be null'
    assert json_data4['error message'] == 'an error ocurred while updating the book'

def test_delete_book(client):
    response = client.delete('/book/8763')
    response2 = client.delete('/book/976786')
    json_data = response.get_json()
    json_data2 = response2.get_json()

    assert response.status_code == 200
    assert response2.status_code == 404
    assert json_data['message'] == 'the book was deleted successfully'
    assert json_data2['error'] == 'book not found'

#*********************test for author*********************
def test_create_author(client):
    response = client.post('/author', json={
        "name": "author3",
        "last_name": "last name 3",
        "country": "USA",
        "gender": "male",
        "dob": "1997-01-01"
    })
    response2 = client.post('/author', json={})
    response3 = client.post('/author', json={
        "name" : "author3",
        "last_name" : "last name 3ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss",
        "country" : "USA",
        "gender" : "male",
        "dob" : "1997-01-01"
    })
    json_data = response.get_json()
    json_data2 = response2.get_json()
    json_data3 = response3.get_json()
    assert response.status_code == 201
    assert response2.status_code == 406
    assert response3.status_code == 400
    assert json_data['message'] == 'author was added successfully'
    assert json_data2['error'] == 'name and last_name cannot be null'
    assert json_data3['message'] == 'an error occured while creating the author'

