# 🚀 URL Shortener

A simple and efficient URL shortener service built with **FastAPI**, **Redis** and **Postgres**.

---

## ✨ Features

- 🔗 **Shorten long URLs**
- ↪️ **Redirect to original URLs**

---

## 🛠️ Getting Started

### 📋 Prerequisites

- [🐳 Docker](https://www.docker.com/)

### ⚡ Installation

```bash
git clone https://github.com/yourusername/url-shortener.git
cd url-shortener
```

### ▶️ Running the App

```bash
docker-compose up
```

The service will be available at [http://localhost:8000](http://localhost:8000).  
Open the `index.html` file in your browser to see the UI.

## Running the frontend

```bash
cd url-shortener-app
npm run start
```

---

## 📚 API Endpoints

| 📝 Method | 🌐 Endpoint         | 📝 Description            |
|-----------|--------------------|---------------------------|
| **POST**  | `/api/urls`     | Shorten a long URL        |
| **GET**   | `/:shortCode`      | Redirect to long URL      |

Swagger: [http://localhost:8000/docs](http://localhost:8000/docs)


---

## ⚙️ Configuration

Edit the `.env` file to set environment variables.

---

## 📄 License

[MIT](LICENSE)
