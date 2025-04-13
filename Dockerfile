FROM postgres:15-alpine

# Copy initialization scripts
COPY database_schema.sql /docker-entrypoint-initdb.d/01_schema.sql
COPY insert_test_data.sql /docker-entrypoint-initdb.d/02_data.sql

# Set environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=postgres
ENV POSTGRES_DB=engaged_data

# Expose PostgreSQL port
EXPOSE 5432 