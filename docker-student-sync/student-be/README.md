
```

technonext@tn-nasir student-be % docker run --rm \
   -v "$HOME/.m2:/root/.m2" \
   -v "$(pwd):/app" \
   -w /app \
   maven:3.9-eclipse-temurin-17 \
   mvn clean package org.sonarsource.scanner.maven:sonar-maven-plugin:sonar \
     -DskipTests \
     -Dsonar.projectKey=air-account-be \
     -Dsonar.projectName="Air Account BE" \
     -Dsonar.host.url=http://157.245.136.36:9000 \
     -Dsonar.token="$SONAR_TOKEN"
```