FROM node:18-alpine
WORKDIR /app
COPY apps/auth-service/package*.json ./
RUN npm install
COPY apps/auth-service .
CMD ["node","dist/main.js"]
