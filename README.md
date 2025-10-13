# Huayoo-Orchestrator

The application layer for the HuaYoo language learning platform, built with FastAPI and Python. This service orchestrates communication between the frontend, database layer, and AI services to provide intelligent language learning features.

## 🎯 Overview

Huayoo-Orchestrator serves as the middleware between the HuaYoo mobile app and the database/AI services. It handles user authentication via Firebase, manages API requests, and coordinates with LLM services to generate and transform language learning content.

## 🏗️ Architecture

- **Framework**: FastAPI for modern Python web API
- **Authentication**: Firebase Admin SDK for user verification
- **Database**: Communicates with HuaYooORM
- **AI Integration**: DeepSeek APIs for content generation
- **CORS Support**: Web platform compatibility

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip
- Firebase project with Admin SDK credentials
- Access to HuaYooORM service

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Huayoo-orchestrator
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your configuration
```

Required environment variables:
```env
# Firebase Configuration
FIREBASE_PROJECT_ID=your-firebase-project
FIREBASE_PRIVATE_KEY_ID=your-private-key-id
FIREBASE_PRIVATE_KEY=your-private-key
FIREBASE_CLIENT_EMAIL=your-client-email
FIREBASE_CLIENT_ID=your-client-id

# Service URLs
ORM_BASE=http://localhost:your-orm-port

# Platform Configuration
PLATFORM=mobile  # or 'web' for web platform
```

5. Place Firebase service account key:
```bash
# Place your Firebase admin service key at:
certs/admin_service.json
```

### Development

Start the development server:
```bash
npm run dev
# or
fastapi run ./src/app.py
```

For web platform with CORS:
```bash
npm run dev:web
# or
set PLATFORM=web && fastapi run ./src/app.py
```

The server will start on `http://localhost:8000`

## 📚 API Endpoints

### Users
- `GET /users/` - Get current user information
- `POST /users/` - Create new user account

### Authentication

All requests require Firebase authentication token in the Authorization header:
```
Authorization: Bearer <firebase-token>
```

## 🛠️ Project Structure

```
src/
├── app.py                 # FastAPI application entry point
├── controllers/           # Business logic controllers
│   └── dataController.py # User data operations
├── models/               # Data models and schemas
│   ├── aiDataModels.py   # AI service data structures
│   └── dbModels.py       # Database models
├── routes/               # API route definitions
│   └── dataRoute.py      # User data routes
├── utils/                # Utility modules
│   ├── config.py         # Configuration management
│   ├── requestContext.py # Request context handling
│   └── verifyFBAuth.py   # Firebase authentication
└── prompts/              # AI prompt templates
    ├── translation.md    # Translation prompts
    └── word-guessing.md  # Word guessing prompts
```

## 🔧 Configuration

### Firebase Setup

1. Create a Firebase project in the Firebase Console
2. Generate a service account key:
   - Go to Project Settings > Service Accounts
   - Generate new private key
   - Download the JSON file as `certs/admin_service.json`

3. Configure environment variables with Firebase credentials

### Platform Configuration

The service supports both mobile and web platforms:

- **Mobile**: Direct API communication
- **Web**: CORS-enabled for browser requests

Set `PLATFORM=web` for web platform support.

## 🤖 AI Integration

### Prompt Templates

The service includes AI prompt templates for:
- **Translation**: Chinese-English translation tasks
- **Word Guessing**: Interactive word learning exercises

### LLM Services

Integration with AI services for:
- Content generation
- Translation assistance
- Learning recommendations

## 🔒 Security

### Authentication Flow

1. Client sends Firebase token in Authorization header
2. Service verifies token using Firebase Admin SDK
3. Token payload provides user context for requests
4. All database operations are scoped to authenticated user

### Request Context

Each request includes:
- Authenticated user information
- HTTP client for downstream requests
- Configuration settings

## 🚀 Deployment

### Docker Support

The service can be containerized using the provided Docker configuration.

### Environment Variables

Ensure all required environment variables are set:
- Firebase credentials
- Database service URLs
- Platform configuration

## 🔮 Future Enhancements

### Planned Features

- **AI Content Generation**: Enhanced LLM integration for dynamic content
- **Caching**: Redis integration for improved performance
- **Rate Limiting**: API rate limiting and throttling
- **Monitoring**: Application performance monitoring
- **Testing**: expand tests

### Technical Improvements

- **Async Optimization**: Enhanced async/await patterns
- **Error Handling**: Improved error handling and logging
- **Documentation**: OpenAPI/Swagger documentation

## 🧪 Development

### Code Organization

- **Controllers**: Business logic and orchestration
- **Models**: Data structures and validation
- **Routes**: API endpoint definitions
- **Utils**: Shared utilities and helpers

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🔗 Related Projects

- [HuaYoo-app](../HuaYoo-app/) - React Native mobile application
- [HuaYooORM](../HuaYooORM/) - PostgreSQL database service