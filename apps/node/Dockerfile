FROM node:22-alpine AS build

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY tsconfig.base.json ./
COPY apps/node ./apps/node
RUN npm run nx -- build node

FROM node:22-alpine AS runtime

WORKDIR /app
ENV NODE_ENV=production
ENV PORT=3000

COPY package*.json ./
RUN npm ci --omit=dev

COPY --from=build /app/dist/apps/node ./dist

EXPOSE 3000

CMD ["node", "dist/main.js"]
