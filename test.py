import unittest
import app
from app import fetch_images

class BasicTests(unittest.TestCase):
    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_main_page_index(self):
        response = self.app.get('/index', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        response = self.app.get('/fail', follow_redirects=True)
        self.assertEqual(response.status_code, 404)

    def test_image_count(self):
        self.assertEqual(len(fetch_images()), 4)

    def test_images_width(self):
        rv = fetch_images()
        for item in rv:
            assert item['width'] < 500


if __name__ == "__main__":
    unittest.main()
