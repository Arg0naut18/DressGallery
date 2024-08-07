uvicorn app:app  --port 8086 --reload &
pid backend=$!

cd gallery-ui
npm start &
pid frontend=$!

wait $backend
wait $frontend
