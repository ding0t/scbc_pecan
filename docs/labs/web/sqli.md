---
title: SQL Injection
tags:
    - picoCTF
    - web-exploitation
    - difficulty::medium
---

Not effectively sanitising user input before passing them to a database query.

```sql
SELECT * FROM users WHERE user_name='admin' AND password='password'
```

Common  SQLi

```sql
admin' OR 1=1 -- //
```