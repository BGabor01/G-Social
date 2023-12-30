# G-Social
A simple social media platform. <br>
Trello table: https://trello.com/b/iaBLXGKE/g-social

## Project Overview

### Project Components

| Component  | Description                                                    |
|------------|----------------------------------------------------------------|
| **Database**   | MySQL                                                          |
| **Message Broker** | RabbitMQ for RPC calls                                       |
| **Web Server** | Nginx                                                          |
| **Django App** | `user_app` - Handles user authentication and profile management |

### Django `user_app` Details

#### Models

| Model            | Description                        |
|------------------|------------------------------------|
| `UserProfileModel` | Stores user profile information    |

#### Views

| View                | Description                                | Serializer                     |
|---------------------|--------------------------------------------|--------------------------------|
| `CreateUserView`      | API view for creating new users            | `RegistrationSerializer`       |
| `RetrieveUserDataView` | API view for retrieving a user's data      | `UserDataSerializer`           |
| `UpdateProfileView`   | API view for updating a user's profile     | `UserProfileUpdateSerializer`  |

#### Signals
| Name            | Description                        |
|------------------|------------------------------------|
| `create_profile` | When a new user is created, creates a new profile record for the user   |


#### Permissions

| Permission          | Description                                        |
|---------------------|----------------------------------------------------|
| `IsOwner`             | Ensures a user is the owner of the profile to update |

## Docker Compose Setup - production

### Services

| Service  | Technology   | Description                                   |
|----------|--------------|-----------------------------------------------|
| **rabbitmq** | RabbitMQ     | Message broker service                        |
| **mysql**    | MySQL        | Database service                              |
| **nginx**    | Nginx        | Web server, serves static and media files     |
| **django**   | Django/Gunicorn | Runs the Django application using Gunicorn |

### Volumes

| Volume          | Purpose                           |
|-----------------|-----------------------------------|
| `mysql_data`     | Persistent data for MySQL        |
| `rabbitmq_data`  | Persistent data for RabbitMQ     |
| `static_volume`  | Stores Django static files       |
| `media_volume`   | Stores Django media files        |

## Nginx Configuration

- Handles static and media file serving.
- Proxies requests to the Django application.
