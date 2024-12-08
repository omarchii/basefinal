#!/bin/bash
DATE=$(date +%Y-%m-%d)
mongodump --db appdb --out ../backups/mongodb_backup_$DATE
echo "Backup MongoDB completed on $DATE"
