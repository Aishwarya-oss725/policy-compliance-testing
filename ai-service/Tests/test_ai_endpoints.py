import pytest
from ai_service.app import app


# -----------------------------
# FIXTURE: Flask test client
# -----------------------------
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# -----------------------------
# 1. CHAT SUCCESS
# -----------------------------
def test_chat_success(client):
    res = client.post("/chat", json={"prompt": "hello"})
    data = res.get_json()

    assert res.status_code == 200
    assert "response" in data


# -----------------------------
# 2. DESCRIBE SUCCESS
# -----------------------------
def test_describe_success(client):
    res = client.post("/describe", json={"input": "test"})
    data = res.get_json()

    assert res.status_code == 200
    assert "description" in data


# -----------------------------
# 3. EMPTY INPUT
# -----------------------------
def test_empty_input(client):
    res = client.post("/chat", json={})
    assert res.status_code == 400


# -----------------------------
# 4. NULL INPUT
# -----------------------------
def test_null_input(client):
    res = client.post("/chat", json={"prompt": None})
    assert res.status_code == 400


# -----------------------------
# 5. INVALID PAYLOAD
# -----------------------------
def test_invalid_payload(client):
    res = client.post("/chat", data="not-json", content_type="text/plain")
    assert res.status_code in [400, 415]


# -----------------------------
# 6. LONG INPUT
# -----------------------------
def test_long_input(client):
    long_text = "A" * 5000
    res = client.post("/chat", json={"prompt": long_text})
    assert res.status_code == 200