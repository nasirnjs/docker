# Set a default value for the node version using ARG
ARG NODE_VERSION=14
# Use the specified node version as the base image
FROM node:${NODE_VERSION}
WORKDIR /app
COPY package.json .
RUN npm install
COPY . .
#EXPOSE 3000
CMD [ "npm", "start" ]
