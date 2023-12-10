# Reddit to Chainlink Oracle Bridge

This backend application acts as a bridge to fetch data from Reddit and provide it to Chainlink's Oracle. It serves as an intermediary to deliver Reddit-related information to the Chainlink network.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Endpoints](#endpoints)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Features

- Fetches data from Reddit using the Reddit API.
- Serves as a middleware to provide data to Chainlink's Oracle.
- Easily configurable using environment variables.

## Prerequisites

Before you begin, ensure you have the following installed:

- Node.js and npm
- Python
- Reddit API credentials (client ID, client secret, user agent)
- Chainlink Oracle setup

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Legend101Zz/chainlink_backend
   ```

2. Install dependencies:

   ```bash
   cd reddit-to-chainlink-oracle
   npm install
   ```

## Configuration

Create a `.env` file in the project root with the following configuration:

```env
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
REDDIT_USER_AGENT=your_reddit_user_agent
```

## Usage

Start the backend server:

```bash
npm start
```

The server will be running at http://localhost:3000 by default.

## Endpoints

- `/memex/reddit/:subreddit/:postId`: Fetches information about a Reddit post in the specified subreddit.

## Example

```bash
curl http://localhost:3000/memex/reddit/Chainlink/18f59sx
```

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License.
