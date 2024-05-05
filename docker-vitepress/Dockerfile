# Stage 1: Build Vitepress website
FROM node:18 AS build-stage

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Copy the entire project
COPY . .

# Build Vitepress
RUN npm install vitepress

# Build site for Production Environment
RUN npm run docs:build 

# Stage 2: Serve Vitepress with Nginx
FROM nginx:alpine

# Copy the built files from the previous stage
COPY --from=build-stage /app/root/.vitepress/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx server
CMD ["nginx", "-g", "daemon off;"]