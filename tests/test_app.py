import unittest
from src.app import app, db
from src.models import Student

class TestApp(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    def test_healthcheck(self):
        response = self.app.get('/api/v1/healthcheck')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'ok'})

    def test_add_student(self):
        response = self.app.post('/api/v1/students', json={"name": "John Doe", "age": 20, "grade": "A"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {"message": "Student added successfully"})

    def test_get_students(self):
        self.app.post('/api/v1/students', json={"name": "John Doe", "age": 20, "grade": "A"})
        response = self.app.get('/api/v1/students')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)

    def test_get_student(self):
        self.app.post('/api/v1/students', json={"name": "John Doe", "age": 20, "grade": "A"})
        response = self.app.get('/api/v1/students/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['name'], "John Doe")

    def test_update_student(self):
        self.app.post('/api/v1/students', json={"name": "John Doe", "age": 20, "grade": "A"})
        response = self.app.put('/api/v1/students/1', json={"name": "Jane Doe", "age": 21, "grade": "B"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Student updated successfully"})

    def test_delete_student(self):
        self.app.post('/api/v1/students', json={"name": "John Doe", "age": 20, "grade": "A"})
        response = self.app.delete('/api/v1/students/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {"message": "Student deleted successfully"})

if __name__ == '__main__':
    unittest.main()
