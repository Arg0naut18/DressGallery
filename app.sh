#!/bin/bash
uvicorn app:app --host $REACT_APP_BACKEND_HOST --port $REACT_APP_BACKEND_PORT --reload &
backend=$!

cd gallery-ui
npm start &
frontend=$!

wait $backend
wait $frontend
