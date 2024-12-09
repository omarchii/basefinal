#!/bin/bash
DATE=$(date +%Y-%m-%d)
mongodump --db appdb --out ../backups/mongodb_backup_$DATE
echo "El Backup de MongoDB se creo el $DATE"
