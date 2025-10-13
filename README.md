### :page_facing_up: What is Huayoo-Orchestrator?
**Huayoo-Orchestrator** is the application layer serving the Huayoo app, hitting the Huayoo-ORM database layer and LLM APIs to fetch, generate and transform data served to and coming from the frontend. All requests requires inclusion of the Firebase Auth token as auth header, which will be verified in Huayoo-Orchestrator using the Firebase Admin SDK to control access.

### :gear: How to run
To run locally, 
1. Install requirements by running `pip install -r requirements.txt`
2. Fetch 
3. From root directory, run command `npm run dev`