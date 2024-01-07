# User app Details

## Models

| Model            | Description                        |
|------------------|------------------------------------|
| `UserProfileModel` | Stores user profile information    |

## Views

| View                | Description                                | Serializer                     |
|---------------------|--------------------------------------------|--------------------------------|
| `CreateUserView`      | CreateAPIView for creating new users            | `RegistrationSerializer`       |
| `RetrieveUserDataView` | RetrieveAPIView for retrieving a user's data      | `UserDataSerializer`           |
| `UpdateProfileView`   | UpdateAPIView for updating a user's profile     | `UserProfileUpdateSerializer`  |

## Signals
| Name            | Description                        |
|------------------|------------------------------------|
| `create_profile` | When a new user is created, creates a new profile record for the user   |

## Celery Tasks

| Task                | Description                                  |
|---------------------|----------------------------------------------|
| `send_welcome_email` | Sends a welcome email to new users. Triggered by the `create_profile` signal. |

## Permissions

| Permission          | Description                                        |
|---------------------|----------------------------------------------------|
| `IsOwner`             | Ensures a user is the owner of the profile to update |