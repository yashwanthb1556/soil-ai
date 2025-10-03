FROM golang:1.20-alpine
WORKDIR /app
COPY apps/worker-service .
RUN go build -o worker
CMD ["./worker"]
