#!/bin/sh

echo "⏳ Waiting for PostgreSQL to start..."

# Tunggu sampai PostgreSQL bisa diakses
while ! nc -z db 5432; do
  sleep 1
done

echo "✅ PostgreSQL started, launching Django..."
exec "$@"
