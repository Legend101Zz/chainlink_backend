const express = require("express");
const { exec } = require("child_process");
const app = express();
const port = 3000;

app.get("/test", (req, res) => {
  res.send("Test route hit!");
});

app.get("/memex/reddit/:subreddit/:postId", (req, res) => {
  const { subreddit, postId } = req.params;

  exec(
    `python3 reddit_script.py ${subreddit} ${postId}`,
    (error, stdout, stderr) => {
      if (error) {
        console.error(`Error: ${error.message}`);
        res.status(500).send("Internal Server Error");
        return;
      }
      console.log(`Python Output: ${stdout}`);
      res.send(`Python Output: ${stdout}`);
    }
  );
});

app.listen(port, () => {
  console.log(`Server is listening at http://localhost:${port}`);
});
