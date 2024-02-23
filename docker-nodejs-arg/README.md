# How to Set Docker Environment ARG Variables?

The ARG instruction defines a variable that users can pass at build-time to the builder with the docker build command using the --build-arg <varname>=<value> flag.
- ARG parameters are applied only during the docker image building process; they are unavailable once you have built the image.
- The running containers cannot access ARG values.
- Some examples of ARG arguments include a version of your Ubuntu or a version of a library.
- You can specify a default value for ARG parameters in dockerfile, and you can modify them during the creation of the build

server.js file env has been set *app.listen(process.env.PORT);* that are pass via cli --env-file project root directory.

**Steps 1: Build image with new ARG values**

`docker build --build-arg NODE_VERSION=16 -t my-node-app:0.2 .`


**Steps 2: Run Build image with ENV values**

`docker run -p 8080:8000 -e PORT=8000 nasirnjs/nodejs:0.2`\
or\
`docker run -p 8080:8000 --env-file .env nasirnjs/nodejs:0.2`

Now Browse `http://localhost:8080`

**Steps 3: Exec into container and check ARG values worked! image build with new Node version**

Check container ID and exec into container.\
`docker ps`

Exec to container.\
`docker exec -it 88c /bin/bash`

Check node version.\
` node -v`