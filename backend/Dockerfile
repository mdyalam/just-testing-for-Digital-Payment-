# Use the official Node.js image
FROM node:18-alpine

# Create a working directory inside the container
WORKDIR /usr/src/app

# Copy package.json and package-lock.json first
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of your backend code
COPY . .

# Expose the port your app runs on
EXPOSE 5000

# The command to start your backend
CMD ["npm", "start"]