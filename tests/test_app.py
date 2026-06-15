from app import app


def test_home_route():
    """Test that home route returns correct response"""
    with app.test_client() as client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.data == b"WRONG RESPONSE"  # This will fail!


def test_app_exists():
    """Test that Flask app object exists"""
    assert app is not None
