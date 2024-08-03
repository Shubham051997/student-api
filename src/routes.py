from flask import Blueprint, request, jsonify
from src.app import app, db
from src.models import Student

bp = Blueprint('students', __name__)

@bp.route('/api/v1/students', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'], grade=data['grade'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 201

@bp.route('/api/v1/students', methods=['GET'])
def get_students():
    students = Student.query.all()
    return jsonify([{"id": student.id, "name": student.name, "age": student.age, "grade": student.grade} for student in students]), 200

@bp.route('/api/v1/students/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify({"id": student.id, "name": student.name, "age": student.age, "grade": student.grade}), 200

@bp.route('/api/v1/students/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.get_json()
    student = Student.query.get_or_404(id)
    student.name = data['name']
    student.age = data['age']
    student.grade = data['grade']
    db.session.commit()
    return jsonify({"message": "Student updated successfully"}), 200

@bp.route('/api/v1/students/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return jsonify({"message": "Student deleted successfully"}), 200
