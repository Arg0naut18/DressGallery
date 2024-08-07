# Dress Gallery
Upon the request of my beloved girlfriend Kiwi, this work is dedicated to her to categorize and keep track of all her clothes.

- A <strong>React</strong> based UI to cater seemless experience to browse through and categorize the endless collections of dresses.
- A <strong>FastApi</strong> based backend API to facilitate the storage of dresses.
- A <strong>MongoDB</strong> database in the backend to keep track of all the dresses and scale to limitless clothes.

### Steps to Run
1. Create a mongo database and a collection. 
2. Fetch the SRV of the mongo and update `MONGO_SRV` in .env.example file.
3. Update the .env.example file with the name of the mongo database in `MONGO_DB`.
4. Update the name of the collection in `MONGO_COLLECTION` in .env.example.
5. Run ```uvicorn app:app --reload```.
6. Change directory to gallery-ui.
7. Run ```npm start```. If this fails. Run ```npm init``` and then repeat step 7.
