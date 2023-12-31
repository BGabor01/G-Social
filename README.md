# G-Social
A simple social media platform. <br>
Trello table: https://trello.com/b/iaBLXGKE/g-social

## Project Overview

### Project Components

| Component        | Description                                                          |
|------------------|----------------------------------------------------------------------|
| **Database**     | MySQL                                                                |
| **Message Broker for Celery** | Redis for managing Celery tasks and queues                    |
| **RPC with Celery** | RabbitMQ for handling RPC calls within Celery tasks                 |
| **Web Server**   | Nginx                                                                |
| **Django App**   | `user_app` - Handles user authentication and profile management       |
| **Celery Worker** | Handles asynchronous tasks such as email sending and RPC operations |

### Django `user_app` Details

#### Models

| Model            | Description                        |
|------------------|------------------------------------|
| `UserProfileModel` | Stores user profile information    |

#### Views

| View                | Description                                | Serializer                     |
|---------------------|--------------------------------------------|--------------------------------|
| `CreateUserView`      | CreateAPIView for creating new users            | `RegistrationSerializer`       |
| `RetrieveUserDataView` | RetrieveAPIView for retrieving a user's data      | `UserDataSerializer`           |
| `UpdateProfileView`   | UpdateAPIView for updating a user's profile     | `UserProfileUpdateSerializer`  |

#### Signals
| Name            | Description                        |
|------------------|------------------------------------|
| `create_profile` | When a new user is created, creates a new profile record for the user   |

#### Celery Tasks

| Task                | Description                                  |
|---------------------|----------------------------------------------|
| `send_welcome_email` | Sends a welcome email to new users. Triggered by the `create_profile` signal. |

#### Permissions

| Permission          | Description                                        |
|---------------------|----------------------------------------------------|
| `IsOwner`             | Ensures a user is the owner of the profile to update |

## Docker Compose Setup - production

### Services

| Service       | Technology       | Description                                           |
|---------------|------------------|-------------------------------------------------------|
| **rabbitmq**  | RabbitMQ         | Used for RPC calls within Celery tasks                |
| **redis**     | Redis            | Message broker service for Celery task management     |
| **mysql**     | MySQL            | Database service                                      |
| **nginx**     | Nginx            | Web server, serves static and media files             |
| **django**    | Django/Gunicorn  | Runs the Django application using Gunicorn            |
| **celery**    | Celery           | Asynchronous task worker for handling background tasks |

### Volumes

| Volume          | Purpose                           |
|-----------------|-----------------------------------|
| `mysql_data`     | Persistent data for MySQL        |
| `rabbitmq_data`  | Persistent data for RabbitMQ     |
| `redis_data`     | Persistent data for Redis        |
| `static_volume`  | Stores Django static files       |
| `media_volume`   | Stores Django media files        |

## Nginx Configuration

- Handles static and media file serving.
- Proxies requests to the Django application.
