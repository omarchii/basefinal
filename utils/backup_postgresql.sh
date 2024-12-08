#!/bin/bash
DATE=$(date +%Y-%m-%d)
pg_dump -U app_user -h localhost appdb > ../backups/appdb_$DATE.sql
echo "Backup PostgreSQL completed on $DATE"
