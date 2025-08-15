from flask import Flask, request
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'لا يوجد ملف', 400
    file = request.files['file']
    if file.filename == '':
        return 'اسم الملف فارغ', 400
    path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(path)
    return f'تم رفع الملف: {file.filename}'

if __name__ == '__main__':
    app.run(debug=True)
