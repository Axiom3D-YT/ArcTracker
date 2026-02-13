# ARC Raiders Event Tracker - Unraid Deployment Guide

This guide will help you deploy the ARC Raiders Event Tracker to your Unraid server using Docker.

## Prerequisites

- Unraid server with Docker enabled
- SSH access to your Unraid server
- Basic familiarity with Docker commands

## Deployment Methods

### Method 1: Docker Compose (Recommended)

1. **Create application directory on Unraid**:
   ```bash
   mkdir -p /mnt/user/appdata/arctracker
   cd /mnt/user/appdata/arctracker
   ```

2. **Upload files to Unraid**:
   Transfer these files from your local machine to `/mnt/user/appdata/arctracker`:
   - `Dockerfile`
   - `docker-compose.yml`
   - `app.py`
   - `requirements.txt`
   - `templates/` (entire directory)

   You can use SCP, SFTP, or Unraid's SMB shares to transfer files.

3. **Build and start the container**:
   ```bash
   cd /mnt/user/appdata/arctracker
   docker-compose up -d
   ```

4. **Access the application**:
   Open your browser and navigate to:
   ```
   http://YOUR-UNRAID-IP:5000
   ```

### Method 2: Docker Run Command

If you prefer not to use Docker Compose:

```bash
# Navigate to the app directory
cd /mnt/user/appdata/arctracker

# Build the image
docker build -t arctracker:latest .

# Run the container
docker run -d \
  --name arctracker \
  --restart unless-stopped \
  -p 5000:5000 \
  arctracker:latest
```

## Configuration

### Port Mapping

The default port is `5000`. To change it, modify the port mapping in `docker-compose.yml`:

```yaml
ports:
  - "8080:5000"  # Change 8080 to your preferred external port
```

Or in the docker run command:
```bash
-p 8080:5000  # Change 8080 to your preferred external port
```

### Auto-start on Boot

The container is configured with `restart: unless-stopped` which means it will automatically start when Unraid boots.

## Management Commands

### View logs
```bash
docker logs arctracker
```

### Stop the container
```bash
docker-compose down
# OR
docker stop arctracker
```

### Restart the container
```bash
docker-compose restart
# OR
docker restart arctracker
```

### Update the application
```bash
cd /mnt/user/appdata/arctracker
docker-compose down
# Update your files (app.py, templates, etc.)
docker-compose up -d --build
```

## Unraid Community Applications (Optional)

For easier management through Unraid's web UI, you can create a custom template:

1. Navigate to **Docker** tab in Unraid
2. Click **Add Container**
3. Fill in the following:
   - **Name**: `arctracker`
   - **Repository**: `arctracker:latest` (after building locally)
   - **Network Type**: `Bridge`
   - **Port**: `5000` (container) → `5000` (host)
   - **Icon URL**: `https://cdn.metaforge.app/arc-raiders/icons/arc.webp` (optional)

## Troubleshooting

### Container won't start
```bash
# Check logs for errors
docker logs arctracker

# Ensure port 5000 is not already in use
netstat -tulpn | grep 5000
```

### Can't access the web interface
- Verify the container is running: `docker ps`
- Check Unraid firewall settings
- Ensure you're using the correct IP and port

### Need to rebuild
```bash
cd /mnt/user/appdata/arctracker
docker-compose down
docker-compose build --no-cache
docker-compose up -d
```

## Support

For issues or questions, refer to the MetaForge API documentation at https://metaforge.app/arc-raiders
