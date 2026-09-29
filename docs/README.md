
# Introduction

yachat is an LLM web client. It supports multiple users, multiple languages, and multiple database connections for persistent data storage, such as Mysql, PostgreSQL, and Sqlite.

> Nothing is difficult if you put your heart into it.

## Features

This project consists of two parts, the client-side and the server-side:

- Client-side, based on [Nuxt](https://nuxt.com/), project address: [https://github.com/hdrbv/yachat](https://github.com/hdrbv/yachat)
- Server-side, based on [Django](https://djangoproject.com/), project address: [https://github.com/hdrbv/yachat/back_end_server](https://github.com/hdrbv/yachat/back_end_server)

### Client-side
- User system, supporting user registration, login, password modification, and more.
- Multi-language user interface, supporting multiple languages.
- Persistent data storage, supporting Mysql, PostgreSQL, and Sqlite databases.
- Asynchronous conversation, supporting multiple conversations simultaneously.
- Management of historical conversations.
- Continuous chat, allowing ChatGPT clients to answer questions based on their historical chat records, resulting in better answers.
- Web search capability, allowing ChatGPT to retrieve the latest information.
- Convenient tools, supporting one-click message and code block copying, as well as message editing.
- Common command management, allowing users to store and edit their own common commands.
- PWA, supporting installation to the desktop.
- User Token Usage Statistics.
- Supports configuring multiple API Keys.

### Server-side
- The server-side has an administrative panel.
- User management.
- Conversation and message management.
- Common configurations.
