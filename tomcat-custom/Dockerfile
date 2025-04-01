# Use official Tomcat image as base (specify version for reproducibility)
FROM tomcat:10.1-jdk17 AS base

# Metadata (best practice for maintainability)
LABEL maintainer="Your Name <your.email@example.com>"
LABEL version="1.0"
LABEL description="Custom Tomcat with a landing page"

# Remove default webapps to avoid conflicts (minimal image)
RUN rm -rf /usr/local/tomcat/webapps/*

# Copy custom landing page to ROOT directory
COPY webapp/index.html /usr/local/tomcat/webapps/ROOT/index.html

# Expose port 8080 (Tomcat default)
EXPOSE 8080

# Set a healthcheck (best practice for monitoring)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD curl -f http://localhost:8080/ || exit 1

# Run Tomcat (default command from base image)
CMD ["catalina.sh", "run"]
