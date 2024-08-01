import unittest
import os
os.environ['TESTING'] = "true"

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get('/')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>MLH Fellow</title>" in html
        assert "<h1>Ali Nawab</h1>" in html
        assert '<section class="about-me">' in html
        assert '<section class="map-container">' in html

    def test_timeline(self):
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        form_data = {
            "name": "John Doe",
            "email": "john@example.com",
            "content": "Hello, world, I'm John Doe!"
        }

        # Create a new post with form data
        response = self.client.post('/api/timeline_post', data=form_data)
        print(response.status_code)
        assert response.status_code == 200
        assert response.is_json

        # Check the new post
        response = self.client.get('/api/timeline_post')
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 1
        post = json["timeline_posts"][0]
        assert post["name"] == "John Doe"
        assert post["email"] == "john@example.com"
        assert post["content"] == "Hello, world, I'm John Doe!"

    def test_timeline_page(self):
        response = self.client.get('/timeline')
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Timeline</title>" in html
        assert "<h1>Timeline</h1>" in html
        assert '<form id="timeline-form">' in html

    def test_malformed_timeline_post(self):
        # POST request with missing name
        response = self.client.post('/api/timeline_post', data={
            "email": "john@example.com", "content": "Hello, world, I'm John Doe!"}
        )
        assert response.status_code == 400
        # Check response body
        html = response.get_data(as_text=True)
        print(html)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe", "email": "john@example.com", "content": ""}
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post('/api/timeline_post', data={
            "name": "John Doe", "email": "not-an-email", "content": "Hello, world, I'm John Doe!"}
        )
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
