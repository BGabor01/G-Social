# Post app Details

## Models

| Model        | Description                            |
|--------------|----------------------------------------|
| `PostModel` | Stores user posts    |

## Views

| View                  | Description                                                | Serializer                |
|-----------------------|------------------------------------------------------------|---------------------------|
| `ListOrCreatePostView`   | API view for listing or creating posts. Allows authenticated users to list existing posts or create new ones. Utilizes `PostSerializer` for serialization. | `PostSerializer`   |
| `UpdateOrDeletePostView` | API view for updating or deleting a post. Authenticated users and post owners can update or delete their posts. Uses `PostSerializer` for serialization. | `PostSerializer`           |
| `RetrievePostView`      | API view for retrieving a single post. Authenticated users can retrieve the details of a specific post. Uses `PostSerializer` for serialization. | `PostSerializer`           |


## Permissions

| Permission          | Description                                        |
|---------------------|----------------------------------------------------|
| `IsOwner`             | Ensures user is the owner of post|

## Paginations

| Class name          | Type                                     |
|---------------------|----------------------------------------------------|
| `PostCursorPagination` | CursorPagination |

