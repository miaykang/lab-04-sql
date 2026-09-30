SELECT 
    users.user_id,
    users.name AS author_name,
    users.email,
    posts.post_id,
    posts.title,
    posts.created_at AS post_date
FROM users
JOIN posts ON users.user_id = posts.user_id
WHERE posts.created_at >= '2026-01-05';