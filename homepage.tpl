<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" type="text/css" href="../static/style.css">
    <title>Chiedilo a Jerry</title>
</head>
<body>
  <center><br>
    <h1>Chiedilo a Jerry</h1><br>
        <h2>Fammi una domanda!</h2>
        <form action="/ask" method="post" target="iframe">
          <input name="question" type="text" size="50%" />
          <input type="submit" value="Ask!" />
        </form><br>
        <iframe name="iframe"
                width="50%"
                height="98%"
                frameBorder="0"
                scrolling="no" />
    </center><br><br>
</body>
</html>
