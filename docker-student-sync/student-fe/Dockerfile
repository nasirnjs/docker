# Stage 1: Build the application
FROM node:alpine as build

ARG BACKEND_URL=http://localhost:8080/

WORKDIR /usr/src/app

RUN npm install -g @angular/cli

COPY package*.json ./

RUN npm install

COPY . .

# Inject backend URL into the production environment file before building
RUN sed -i "s|BACKEND_URL|${BACKEND_URL}|g" src/environments/environment.prod.ts

RUN npm run build

# Stage 2: Create the production image
FROM nginx:alpine

COPY --from=build /usr/src/app/dist/student-fontend /usr/share/nginx/html

COPY nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
