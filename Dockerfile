from node:24-alpine

WORKDIR /workspace


RUN npm install -g @opencode/cli
RUN  addgroup -S appgroup && adduser -S appuser -G appgroup
RUN chown -R appuser:appgroup /workspace
USER appuser



CMD ["opencode"]