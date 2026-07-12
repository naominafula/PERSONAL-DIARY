# 📔 New Day Diary - Personal Journal Application

A secure, responsive, and minimalist web-based personal diary application designed for capturing daily thoughts, tracking moods, and safely storing private reflections behind robust user authentication.

---

## 🛠️ Tech Stack & Languages Used

This project follows a clean decoupled pattern utilizing a robust Python backend ecosystem paired with a dynamic, fast-loading JavaScript frontend.

### 🔤 Core Languages
* **Python**: Core backend application logic, database models, security routing, and API endpoint construction.
* **JavaScript (ES6+)**: Handles frontend dynamic rendering, processing secure user actions, storage handling, asynchronous RESTful API transactions (`fetch`), and state updates without page reloads.
* **HTML5**: Semi-semantic page layouts, dashboard input forms, modular content wrappers, and standard markup structure.
* **CSS3**: Underlying style rules orchestrated natively via a utilities-first framework approach.

### ⚙️ Backend Frameworks & Libraries
* **Flask**: Micro web framework managing routing, requests, application context, and view controllers.
* **Flask-SQLAlchemy**: Object-Relational Mapper (ORM) translating Python database class structures into structured SQL query models.
* **Flask-JWT-Extended**: Handles secure Json Web Token issuance, expiry management, and authorization guards across private REST endpoints.
* **Flask-Bcrypt**: Provides advanced cryptographic password hashing and verification protocols.

---

## 🎨 UI Style, Architecture & Themes

The front-end design leverages an optimized utilities configuration running directly via the cloud utility tool belt.

### 🚀 Tailwind CSS Framework
The visual architecture relies entirely on **Tailwind CSS**. No heavy custom stylesheets are needed; classes are declared directly inside component containers to preserve low layout latency.

### 🐳 UI Theme: "Bright Ocean Breeze" (Light Blue)
The interface features a bright, clean, calming sky-blue design configuration tailored to a focused digital diary experience:
* **Background Atmosphere:** A soft vertical canvas gradient flowing seamlessly from `#f0f7ff` (ice sky) to `#e0effe` (pale bright blue).
* **Navigation & Accent Panels:** Structured content blocks featuring clean glassmorphism variations using high-contrast highlight hues (`#e0f2fe` / `#f0f9ff`) bounded by structured soft borders (`#bae6fd`).
* **Primary Interactive Elements:** Focus buttons styled with an energetic high-visibility classic cobalt highlight (`#2563eb` hovering dynamically to deep indigo `#1d4ed8`).
* **Typography Hierarchy:** Strict high-contrast styling moving from rich deep teal-slate colors (`#1c352d`) down to soft neutral medium greys for entry context descriptions.

---

## 🏗️ Feature Map & CRUD Capabilities

The application implements a safe state machine for database content handling:

1. **Authentication (Auth Guard)**: Secure login/signup mechanisms ensuring users only view data tied to their verified profile. Token payloads are tracked in the user's secure client browser storage.
2. **Create (POST)**: Interactive home dashboard form offering dynamic prompt suggestions and mood metrics alongside a direct, asynchronous submission payload pipeline.
3. **Read (GET)**: Fast lookup query architecture assembling a secure feed of user-specific diary arrays.
4. **Delete (DELETE)**: Dedicated server-side authorization checkpoints preventing cross-user account modification while maintaining active client-side visual list pruning.

---

## 🚀 Quick Start Guide

### 1. Initialize the Environment
Ensure your virtual environment is active in your terminal, then install the necessary dependencies:
```bash
pip install flask flask-sqlalchemy flask-bcrypt flask-jwt-extended flask-cors