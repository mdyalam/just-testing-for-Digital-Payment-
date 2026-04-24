# Use the official Node.js image
FROM node:18-alpine

# Create a working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of your frontend code
COPY . .

# Expose the standard React port
EXPOSE 3000

# Start the React development server
CMD ["npm", "start"]