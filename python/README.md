## Apps

Those are the apps the I want to test.

### Expected routes

- `/` : Liveness endpoint;
- `/live` : Liveness endpoint;
- `/v1/users/<user_id>` : Get user by id (UUID);
    - `cache` param is used to specify if it the result should be cached;
- `/v1/users` : Search users by name (if no name qs is provided `*` is used) and cache the result;
    - `cache` param is used to specify if it the result should be cached;
- `/sleep/users/<user_id>` : Return a randomly generated user and applies a sleep;
- `/sleep/users` : Return a list of randomly generated users and apply a sleep;
