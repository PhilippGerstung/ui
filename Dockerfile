FROM node:20.15.1-slim
ARG WORKINGDIR=/app
WORKDIR $WORKINGDIR
ADD package.json $WORKINGDIR

RUN ls -l

# Install dependencies
RUN npm install -g npm@latest
RUN rm -rf node_modules
RUN npm i

# Build the app
ADD . $WORKINGDIR
RUN npm run build

# Start the app
CMD ["node", ".output/server/index.mjs"]