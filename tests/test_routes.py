# Get all books and return no records
def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# Get one book by id
def test_get_book_by_id(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "The ocean as a divine entity."
    }

# Test no data in test database returns 404
def test_get_book_by_id_with_no_data(client):
    # Act
    response = client.get("/book/1")
    response_body = response.get_json()
    
    # Assert
    assert response.status_code == 404
    assert response_body == None 

# Valid test data returns 200 with an array including appropriate test data
def test_get_valid_data_with_all_records(client, two_saved_books):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 1,
            "title": "Ocean Book",
            "description": "The ocean as a divine entity."
        },
        {
            "id": 2,
            "title": "Food Book",
            "description": "A book about food and its origins."
        }
    ]

# POST/books with a JSON request body returns 201
def test_post_with_json_request_body(client):
    # Act
    response = client.post("/books",  json={
        "title": "Wine Book",
        "description": "A Beginners Guide to Wine Pairings."
    }
    )
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "Wine Book",
        "description": "A Beginners Guide to Wine Pairings."
    }




