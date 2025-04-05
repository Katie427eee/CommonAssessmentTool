Team TicTech 

Project -- Feature Development Backend: Create CRUD API's for Client

User Story

As a user of the backend API's, I want to call API's that can retrieve, update, and delete information of clients who have already registered with the CaseManagment service so that I more efficiently help previous clients make better decisions on how to be gainfully employed.

Acceptance Criteria
- Provide REST API endpoints so that the Frontend can use them to get information on an existing client.
- Document how to use the REST API
- Choose and create a database to hold client information
- Add tests


This will contain the model used for the project that based on the input information will give the social workers the clients baseline level of success and what their success will be after certain interventions.

The model works off of dummy data of several combinations of clients alongside the interventions chosen for them as well as their success rate at finding a job afterward. The model will be updated by the case workers by inputing new data for clients with their updated outcome information, and it can be updated on a daily, weekly, or monthly basis.

This also has an API file to interact with the front end, and logic in order to process the interventions coming from the front end. This includes functions to clean data, create a matrix of all possible combinations in order to get the ones with the highest increase of success, and output the results in a way the front end can interact with.

-------------------------How to Use-------------------------
1. In the virtual environment you've created for this project, install all dependencies in requirements.txt (pip install -r requirements.txt)

2. Run the app (uvicorn app.main:app --reload)

3. Load data into database (python initialize_data.py)

4. Go to SwaggerUI (http://127.0.0.1:8000/docs)

4. Log in as admin (username: admin password: admin123)

5. Click on each endpoint to use
-Create User (Only users in admin role can create new users. The role field needs to be either "admin" or "case_worker")

-Get clients (Display all the clients that are in the database)

-Get client (Allow authorized users to search for a client by id. If the id is not in database, an error message will show.)

-Update client (Allow authorized users to update a client's basic info by inputting in client_id and providing updated values.)

-Delete client (Allow authorized users to delete a client by id. If an id is no longer in the database, an error message will show.)

-Get clients by criteria (Allow authorized users to get a list of clients who meet a certain combination of criteria.)

-Get Clients by services (Allow authorized users to get a list of clients who meet a certain combination of service statuses.)

-Get clients services (Allow authorized users to view a client's services' status.)

-Get clients by success rate (Allow authorized users to search for clients whose cases have a success rate beyond a certain number.)

-Get clients by case worker (Allow users to view which clients are assigned to a specific case worker.)

---

## 🐳 Running the Backend with Docker

You can run the backend API using Docker for easy deployment and cross-platform compatibility.

### ▶️ Option 1: Run with Docker

```bash
docker build -t backend-app .
docker run -p 8000:8000 backend-app
```

Open in browser: http://localhost:8000/docs

---

### ▶️ Option 2: Run with Docker Compose (Recommended)

```bash
docker compose up --build
```

To stop the service:

```bash
docker compose down
```

---

## ⚙️ Environment Configuration

Create a `.env` file in the root directory with the following content:

```env
DATABASE_URL=sqlite:///./test.db
SECRET_KEY=your-very-secret-key
DEBUG=True
```

This file is automatically used when running with Docker Compose.

---

## 🔄 Continuous Integration & Deployment (CI/CD)

This project uses **GitHub Actions** for continuous integration and deployment.

Workflows automatically perform the following tasks on every `push` or `pull_request` to `main`:

- ✅ Install project dependencies
- ✅ Run code formatters and linters (via [Ruff](https://github.com/astral-sh/ruff))
- ✅ Run unit tests using [Pytest](https://docs.pytest.org/)
- ✅ Build and run the Docker image to validate container functionality

You can view workflow runs in the **Actions** tab of the GitHub repository.


