# Use the official OpenJDK base image
FROM eclipse-temurin:17-jdk-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the JAR file into the container
COPY target/student_management-0.0.1-SNAPSHOT.jar app.jar

# Expose the port that your Spring Boot application will run on
EXPOSE 8080

# Command to run your application
CMD ["java", "-jar", "app.jar"]
