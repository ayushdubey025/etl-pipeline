# 📂 ETL Project: Sales Data Pipeline

This repository contains an end-to-end ETL (Extract, Transform, Load) pipeline designed to process raw sales data from various sources (CSV, JSON), clean and transform it, and then load it into a SQLite database. The project is containerized using Docker, demonstrating a complete data engineering workflow.

## 🚀 Project Overview

This project simulates a real-world scenario where data from different formats needs to be unified, cleaned, and stored for analysis.

**Key Features:**
* **Extract:** Reads sales data from both CSV and JSON files.
* **Transform:** Cleans data by handling missing values, standardizing data types, ensuring consistent date formats, and calculating new metrics (e.g., `total_sales_amount`). **Crucially, it converts all currency values to INR for unified reporting.**
* **Load:** Stores the processed data into an SQLite database for easy querying and reporting.
* **Containerization:** Utilizes Docker to create a portable and reproducible environment for the ETL pipeline.

## 📁 Project Structure

```
etl_project/
│── data/                     # Raw input data files
│   ├── sales_data.csv
│   └── sales_data.json
│
│── etl/                      # Python scripts for ETL logic
│   ├── extract.py            # Handles data extraction from sources
│   ├── transform.py          # Performs data cleaning and transformations
│   └── load.py               # Loads transformed data into the database
│
│── database/                 # Stores the SQLite database file
│   └── sales.db              # SQLite database for processed sales data
│
│── main.py                   # Orchestrates the ETL pipeline execution
│── Dockerfile                # Defines the Docker image for the project
│── requirements.txt          # Lists Python dependencies
│── .dockerignore             # keeps repo clean
│── .gitignore                # keeps repo clean
│── README.md                 # Project documentation (this file)
```

## 🛠️ Technologies Used

* **Python 3.x:** Core programming language.
* **Pandas:** For efficient data manipulation and analysis.
* **SQLite3:** Lightweight relational database for data storage.
* **Docker:** For containerizing the application and its dependencies.

## 🏃 How to Run the Project

You can run this project either natively (installing Python dependencies) or using Docker (recommended for consistency).

### Option 1: Running Natively

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/etl_project.git](https://github.com/your-username/etl_project.git)
    cd etl_project
    ```
    (Replace `your-username` with your actual GitHub username)

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the ETL pipeline:**
    ```bash
    python main.py
    ```
    After execution, you will find the `sales.db` file in the `database/` directory.

### Option 2: Running with Docker (Recommended)

1.  **Ensure Docker is installed:**
    Make sure Docker Desktop or Docker Engine is installed and running on your system.

2.  **Clone the repository (if you haven't already):**
    ```bash
    git clone [https://github.com/your-username/etl_project.git](https://github.com/your-username/etl_project.git)
    cd etl_project
    ```

3.  **Build the Docker image:**
    ```bash
    docker build -t etl-project .
    ```
    This command builds a Docker image named `etl-project` using the `Dockerfile` in the current directory.

4.  **Run the Docker container:**
    ```bash
    docker run --rm -v "$(pwd)/database:/app/database" etl-project
    ```
    * `--rm`: Automatically removes the container after it exits.
    * `-v "$(pwd)/database:/app/database"`: Mounts your local `database` folder into the container. This ensures that the `sales.db` file created inside the container is saved to your local machine, allowing you to inspect the database after the pipeline runs.

    After the container finishes, you will find the `sales.db` file in your local `database/` directory.

## 🔍 Verifying the Data

You can use a SQLite browser or the `sqlite3` command-line tool to inspect the `sales.db` file.

1.  **Install SQLite (if not already installed):**
    ```bash
    sudo apt-get install sqlite3 # For Debian/Ubuntu
    brew install sqlite3         # For macOS
    ```

2.  **Connect to the database:**
    ```bash
    sqlite3 database/sales.db
    ```

3.  **Run SQL queries:**
    ```sql
    .tables
    SELECT * FROM sales;
    .quit
    ```

## 📈 Future Enhancements

* Implement proper logging for better monitoring and debugging.
* Add unit tests for extract, transform, and load functions.
* Integrate with cloud storage (e.g., S3, GCS) for data sources and destinations.
* Schedule the pipeline using tools like Apache Airflow or Prefect.
* Expand error handling and data quality checks.
