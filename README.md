## Plant Disease Expert System API

This API empowers you to manage a plant disease expert system, leveraging the AIMA package for diagnosis and storing disease and symptom information in a database.

### Project Structure

The project is organized as follows:

- `routes.py`: Defines API endpoints for managing diseases, symptoms, and diagnosing plant diseases.
- `schema.py`: Contains Pydantic models for data validation and serialization/deserialization. 
- `utils.py`: Implements the diagnosis logic using the AIMA package (code not shown here).
- `db/database.py`: Establishes database connection and defines session dependency.
- `db/models.py`: Defines database models for diseases and symptoms using SQLAlchemy.

### API Endpoints

The API offers several endpoints for interacting with disease and symptom data, as well as diagnosing plant issues:

#### Disease Management

- **Create Disease (POST /disease/)**
   - Request Body: `DiseaseBase` schema (title, description, treatment)
   - Response: `DiseaseDisplay` schema (created disease information including ID)
- **Get All Diseases (GET /diseases/)**
   - Response: List of `DiseaseDisplay` schemas for all diseases in the database

#### Symptom Management

- **Create Symptom (POST /symptoms/)**
   - Request Body: `SymptomBase` schema (description)
   - Response: `SymptomDisplay` schema (created symptom information including ID)
- **Get All Symptoms (GET /symptoms/)**
   - Response: List of `SymptomDisplay` schemas for all symptoms in the database

#### Diagnosis

- **Diagnose Plant Disease (POST /diagnose)**
   - Request Body: `UserSymptoms` schema (list of symptom IDs)
   - Response:
     - `DiseaseDisplay` schema (containing information about the diagnosed disease) if a match is found
     - `ErrorResponse` schema with error message if diagnosis fails

**Data Models:**

The API utilizes Pydantic data models for data validation and ensuring consistent data structures. You'll find these models defined in `schema.py`.

**Database:**

The project utilizes a database to store information about diseases and symptoms. The connection and session management are handled in `db/database.py`.


### Running the Server

**Prerequisites:**

- Python 3.x
- uvicorn (install using `pip install uvicorn`)
- Required project dependencies (refer to `requirements.txt`)

**Steps:**

1. Install dependencies: `pip install -r requirements.txt`
2. Start the development server: `uvicorn routes.py:app --reload` (This will start the server and automatically reload on code changes)

**Accessing the API:**

Once the server is running, you can interact with the API endpoints using tools like Postman or curl. Refer to the specific endpoint documentation for request body formats and expected responses.

**Example Usage (using curl):**

* Create a new disease:

```bash
curl -X POST http://localhost:8000/disease/ -H "Content-Type: application/json" -d '{"title": "Leaf Blight", "description": "Brown spots on leaves", "treatment": "Fungicide"}'
