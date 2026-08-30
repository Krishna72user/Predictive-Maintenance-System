def test_register(client):
    response = client.post('/api/v1/auth/register',json={
        "username": "test",
        "email": "test@gmail.com",
        "password": "test123"
    })
    if response.status_code==400:
        assert response.json() == {"detail":"Username already exists"}
    else:
        assert response.status_code == 200
        assert response.json() == {"message": "User created successfully"}

def test_login(client):
    response = client.post('/api/v1/auth/login',json={
        "email": "test@gmail.com",
        "password": "test123"
    })
    if response.status_code == 200:
        assert response.json() =={"message": "User logged in successfully"}
    else:
        assert response.status_code ==401
        assert response.json()=={{"detail":"Invalid Credentials"}}


def test_profit(client):
    response = client.post("/api/v1/auth/get_user")

    if  response.status_code == 401:
        assert response.json() == {
           'detail':"No session cookie provided"
        }



