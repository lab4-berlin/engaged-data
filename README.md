# engaged-data
Database and API for the EngagED project

## Documentation
- [Database Schema Documentation](docs/database.md) - Detailed documentation of the database schema, tables, relationships, and constraints.

## Running the Application

### Prerequisites
- Docker
- Docker Compose

### Project Structure
```
your-project/
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   ├── models.py
│   └── requirements.txt
├── database_schema.sql
├── docker-compose.yml
└── README.md
```

### Running the Database and Backend

1. **Start the Services**
```bash
docker-compose up -d
```

This will start:
- PostgreSQL database on port 5432
- FastAPI backend on port 8000

2. **Access Points**
- API Documentation: http://localhost:8000/docs
- API: http://localhost:8000
- Health Check: http://localhost:8000/health
- Database: localhost:5432

3. **Common Commands**
```bash
# Start all services
docker-compose up -d

# Stop all services
docker-compose down

# View logs
docker-compose logs -f

# Rebuild the images
docker-compose build

# Connect to the database using psql
docker-compose exec db psql -U postgres -d engaged_data

# Restart a specific service
docker-compose restart backend
```

### API Endpoints

#### Health Check
- `GET /health` - Check if the API is running
- Response: `{"status": "healthy"}`

#### Institution Endpoints
- `GET /institutions` - List all institutions
- `GET /institutions/{id}` - Get institution by ID
- `POST /institutions` - Create new institution
- `PUT /institutions/{id}` - Update institution
- `DELETE /institutions/{id}` - Delete institution

#### Educator Endpoints
- `GET /educators` - List all educators
- `GET /educators/{id}` - Get educator by ID
- `POST /educators` - Create new educator
- `PUT /educators/{id}` - Update educator
- `DELETE /educators/{id}` - Delete educator

#### Lecture Endpoints
- `GET /lectures` - List all lectures
- `GET /lectures/{id}` - Get lecture by ID
- `POST /lectures` - Create new lecture
- `PUT /lectures/{id}` - Update lecture
- `DELETE /lectures/{id}` - Delete lecture

#### Question Endpoints
- `GET /questions` - List all questions
- `GET /questions/{id}` - Get question by ID
- `POST /questions` - Create new question
- `PUT /questions/{id}` - Update question
- `DELETE /questions/{id}` - Delete question

#### Answer Option Endpoints
- `GET /answer-options` - List all answer options
- `GET /answer-options/{id}` - Get answer option by ID
- `POST /answer-options` - Create new answer option
- `PUT /answer-options/{id}` - Update answer option
- `DELETE /answer-options/{id}` - Delete answer option

#### Student Answer Endpoints
- `GET /student-answers` - List all student answers
- `GET /student-answers/{id}` - Get student answer by ID
- `POST /student-answers` - Create new student answer
- `GET /student-answers/device/{device_id}` - Get all answers from a specific device

### Development

1. **Database Migrations**
The application uses SQLAlchemy for database operations. To create or update the database schema:
```bash
# Connect to the database
docker-compose exec db psql -U postgres -d engaged_data

# Run the schema script
\i database_schema.sql
```

2. **Environment Variables**
The application uses the following environment variables:
- `DATABASE_URL`: PostgreSQL connection string
- Default: `postgresql://postgres:postgres@db:5432/engaged_data`

3. **API Documentation**
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Security Notes
The current setup is for development only. For production:
- Use stronger passwords
- Use environment variables for sensitive data
- Implement proper authentication/authorization
- Use HTTPS
- Configure proper CORS settings
- Use a more secure PostgreSQL configuration

### Troubleshooting

1. **Database Connection Issues**
- Check if the database is running: `docker-compose ps`
- Check database logs: `docker-compose logs db`
- Verify connection string in environment variables

2. **API Issues**
- Check if the backend is running: `docker-compose ps`
- Check backend logs: `docker-compose logs backend`
- Verify API documentation at http://localhost:8000/docs

3. **Common Problems**
- Port conflicts: Ensure ports 5432 and 8000 are available
- Volume permissions: Check Docker volume permissions
- Network issues: Ensure Docker network is properly configured
