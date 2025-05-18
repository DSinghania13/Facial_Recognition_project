# Facial Recognition Project

This project demonstrates a facial recognition system using Python and computer vision libraries. It is capable of detecting and recognizing human faces in images by comparing them to a dataset of known individuals.

---

## 🛠️ Technologies Used

- **Python** 3.9  
- **dlib** 19.24.99  
- **face-recognition** 1.3.0  
- **NumPy** 1.26.4  
- **OpenCV-Python** 4.9.0.80

> **Note:**  
> Before installing `face-recognition`, you must install `dlib` with all necessary build tools. Refer to the [dlib installation guide](https://pypi.org/project/dlib/) if you encounter issues.

---

## 📁 Dataset

You can use your own custom dataset of images. In this project, we use images of characters from the popular American TV show **“The Office”** as the training data.

---

## 📂 Project Structure

```
Facial_Recognition_Project/
├── main.py # Main script to perform facial recognition
├── result.jpg # Output image with labeled recognized faces
├── train/ # Directory containing known face images
│ ├── dwight.jpeg
│ ├── jim.jpeg
│ ├── michael.jpg
│ ├── pam.jpeg
│ └── ryan.jpeg
└── test/ # Directory containing images for testing
└── test.jpg
```

---

## 🚀 Getting Started

1. **Clone the repository**  
   ```bash
   git clone https://github.com/your-username/facial_recognition_project.git
   cd facial_recognition_project
   ```

2. **Install dependencies**
  * It's recommended to use a virtual environment.
    ```bash
    pip install dlib
    pip install face-recognition
    pip install numpy
    pip install opencv-python
    ```

3. **Run the project**
    ```bash
    python main.py
    ```

4. **View the output**
* Check the generated result.jpg to see the recognized faces.

---

## 📸 Example
* Sample input from test/test.jpg and output saved as result.jpg:
* **test.jpg** -
![image](https://github.com/user-attachments/assets/2cf74361-d20b-4d27-b5c5-484915f3e78b)
* **result.jpg** -
![image](https://github.com/user-attachments/assets/9bd79de5-6c7e-4469-82fd-492d869476c7)

---

## 👨‍💻 Author
* Developed by [Divit Singhania](https://www.linkedin.com/in/divit-singhania-13401628a/).
