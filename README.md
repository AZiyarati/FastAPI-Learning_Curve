# Learn FastAPI

Welcome to the **Learn FastAPI** repository! This is a structured learning resource designed to help you master [FastAPI](https://fastapi.tiangolo.com/), the modern, high-performance web framework for Python, step by step. Whether you're a beginner or an experienced developer exploring FastAPI for the first time, this repository has something for you.

---

## 📖 Overview

This repository is divided into well-organized sections that cover all essential aspects of FastAPI, from basic concepts to advanced topics. Each section includes detailed explanations, examples, and exercises to solidify your understanding.

---

## 🏗️ Project Structure

The repository is structured as follows:

- **1. Basics:**
  - Setting up FastAPI.
  - Writing your first FastAPI application.

- **2. Routing:**
  - Defining endpoints and handling requests.
  - Using path and query parameters.

- **3. Data Models:**
  - Working with `Pydantic` for data validation.
  - Defining request and response models.

- **4. Dependency Injection:**
  - Managing dependencies efficiently.
  - Reusable components with `Depends`.

- **5. Authentication:**
  - Implementing OAuth2.
  - Securing APIs with JWT tokens.

- **6. Advanced Topics:**
  - WebSockets for real-time communication.
  - Background tasks for asynchronous processing.
  - Middleware and custom exceptions.

Each topic is accompanied by practical examples to help you learn by doing.

---

## 🚀 Getting Started

### Prerequisites

Before you begin, make sure you have:
- **Python** 3.9 or higher installed.
- Basic familiarity with Python programming.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/AZiyarati/FastAPI-Learning_Curve.git
   cd FastAPI-Learning_Curve
   ```

2. Switch to the desired branch for the specific exercise or topic:

   ```bash
   git checkout <branch-name>
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Start the FastAPI development server:

   ```bash
   uvicorn main:app --reload
   ```

5. Open your browser and visit [http://127.0.0.1:8000](http://127.0.0.1:8000) to see the application running.

---

## 📂 Branches

Each exercise or section is organized into a separate branch for easy access and cloning. Here are the key branches:

- `01-introduction`: Basics and motivation for using FastAPI.
- `02-routing`: Setting up routes and handling requests.
- `03-data-models`: Using Pydantic models for validation.
- `04-dependencies`: Dependency injection and reusable components.
- `05-authentication`: Implementing JWT and OAuth2.
- `06-advanced`: Advanced topics like WebSockets and background tasks.

To work on a specific branch, simply switch to it using:

```bash
git checkout <branch-name>
```

---

## 🤝 Contributions

Contributions are welcome! This repository is maintained by:

- **AZiyarati** ([GitHub](https://github.com/AZiyarati))
- **Pakrohk** ([GitHub](https://github.com/pakrohk))

If you'd like to add examples, fix issues, or improve the content:

1. Fork the repository.
2. Create a new branch:

   ```bash
   git checkout -b feature-name
   ```

3. Commit your changes:

   ```bash
   git commit -m "Add feature-name"
   ```

4. Push to your branch:

   ```bash
   git push origin feature-name
   ```

5. Open a pull request.

---

## 🛡️ License

This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🌟 Acknowledgments

Special thanks to the creators of FastAPI for building an amazing framework and providing extensive documentation. For more information, visit the [FastAPI documentation](https://fastapi.tiangolo.com/).

---

Happy coding! 🎉

