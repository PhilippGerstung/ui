FROM node:20.15.1-slim

COPY --chown=node:node package.json .

RUN ls -l

# Install dependencies
RUN npm install -g npm@latest
RUN rm -rf node_modules
RUN npm i


# Build the app
RUN chmod -R 777 /node_modules
COPY --chown=node:node . .
RUN npm run build

# Start the app
CMD ["node", ".output/server/index.mjs"]