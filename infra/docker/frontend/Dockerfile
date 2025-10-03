FROM node:18-alpine
WORKDIR /app
COPY apps/frontend/package*.json ./
RUN npm install
COPY apps/frontend .
RUN npm run build
CMD ["npx","serve","-s","dist","-l","4200"]
