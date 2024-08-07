#!/bin/bash
uvicorn app:app --port $REACT_APP_BACKEND_PORT --reload &
backend=$!

cd gallery-ui
npm start &
frontend=$!

wait $backend
wait $frontend
