flask_social_media_project/
│
├── .venv/                # Virtual environment (library root)
│
├── blueprints/           # Flask Blueprints for routing
│   ├── post.py           # Post routes (e.g., create post, fetch posts)
│   └── user.py           # User routes (e.g., register, login)
│
├── models/               # Database models
│   ├── post.py           # Post model (e.g., title, content, user_id)
│   └── user.py           # User model (e.g., username, email, password)
│
├── services/             # Business logic services
│   ├── post.py           # Post-related logic (e.g., creating, updating posts)
│   └── user.py           # User-related logic (e.g., authentication, validation)
│
├── static/               # Static files (e.g., CSS, JavaScript)
│
├── templates/            # HTML templates
│
├── app.py                # Application entry point (Flask app initialization)
├── config.py             # Configuration settings (e.g., database URI, environment variables)
└── db.py                 # Database setup and initialization
