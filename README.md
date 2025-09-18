# News Search Engine with Information Retrieval

This project is a full-stack web application that demonstrates a functional news search engine built using information retrieval techniques. It features a fast and efficient search backend and a modern, responsive frontend.
<img width="1342" height="606" alt="search_1" src="https://github.com/user-attachments/assets/6b1e33ad-39b0-4a62-a45f-b4cc2e62e4c9" />

## 🌟 Features

* **Information Retrieval Backend:** Utilizes **Term Frequency–Inverse Document Frequency (TF-IDF)** and **Cosine Similarity** for fast and highly relevant search results on a document corpus.
* **Django REST API:** A robust and scalable backend built with Python's Django REST Framework to handle search queries and serve data.
* **React.js Frontend:** A dynamic Single Page Application (SPA) that provides an intuitive user interface for searching and viewing results.
* **Containerized with Docker Compose:** The entire application stack is containerized, ensuring a consistent and isolated environment for easy setup and deployment.

## 🛠️ Technologies Used

* **Backend:** Python, Django, Django REST Framework, scikit-learn
* **Frontend:** React.js, JavaScript, HTML, CSS
* **Deployment:** Docker, Docker Compose

## 🚀 Getting Started

These instructions will get a copy of the project up and running on your local machine.

### Prerequisites

You need to have Docker installed on your system.

### Installation and Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Mo-Atef-r/News_Search_Engine
    cd news_search_engine
    ```

2.  **Build the React frontend:**
    Navigate to the `frontend` directory and build the production static files.
    ```bash
    cd frontend
    npm install
    npm run build
    cd ..
    ```

3.  **Run the application with Docker Compose:**
    From the project's root directory, start the containers.
    ```bash
    docker compose up --build
    ```

The application will now be running.

## 🌐 Usage

Open your web browser and navigate to `http://localhost:8000`.

* Use the search bar to enter a query (e.g., "computer graphics technology").
* Press "Search" to view the top-ranked articles based on relevance.

<img width="674" height="607" alt="search_1_1" src="https://github.com/user-attachments/assets/75fb2df5-215e-44f6-9bf1-9c4b471d4886" />
