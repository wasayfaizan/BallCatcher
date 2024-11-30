<body>
    <header>
        <h1>BallCatcher Game</h1>
        <p>A fun hand-tracking game where you catch falling balls using your hand!</p>
    </header>
    <section>
        <h2>Overview</h2>
        <p>
            This is a simple game where a ball falls from the top of the screen, and you have to use your hand (tracked by your webcam) to catch it. Every time the ball is caught, the score increases and a beep sound is played.
        </p>
        <h2>Features</h2>
        <ul>
            <li>Hand detection using MediaPipe to track the wrist position</li>
            <li>Falling ball physics with random spawn locations</li>
            <li>Score tracking that increases with every catch</li>
            <li>Beep sound when the ball is caught</li>
        </ul>
        <h2>How to Run</h2>
        <p>Follow these steps to run the game:</p>
        <ol>
            <li>Clone this repository to your local machine using the following command:</li>
            <pre><code>git clone https://github.com/yourusername/catch-ball-game.git</code></pre>
            <li>Install the required dependencies:</li>
            <pre><code>pip install opencv-python mediapipe pygame numpy</code></pre>
            <li>Run the game script:</li>
            <pre><code>python3 main.py</code></pre>
            <li>Make sure you have a working webcam connected to your computer for hand tracking.</li>
        </ol>
        <h2>Gameplay Instructions</h2>
        <p>
            - The game will open a window showing the webcam feed.
            - A red ball will fall from the top of the screen.
            - Move your hand (specifically your wrist) to catch the ball. 
            - Every time you catch the ball, your score increases by 1 and a beep sound will play.
            - To quit the game, press the <strong>q</strong> key.
        </p>
        <h2>File Structure</h2>
        <p>The repository contains the following files:</p>
        <ul>
            <li><code>main.py</code>: The main game script.</li>
            <li><code>README.html</code>: This readme file with instructions.</li>
        </ul>
    <footer>
        <p>&copy; 2024 BallCatcher Game</p>
    </footer>
</body>
</html>
