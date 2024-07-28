## Chess Robot Connecting Remote and In-person Players

# Project Overview
During COVID, my friends and I got into playing online chess, however, we missed the physical presence the chess pieces. So, we created a Chess Robot that bridges the gap between remote and in-person chess players. We combine a physical robotic chessboard with a web application, allowing anyone to engage in real-time chess matches regardless of their location.

# Features
- Robotic Chessboard: A physical board that mirrors the moves made in an online chess game.
- Computer Vision: Utilizes OpenCV (Python) to detect and track the movement of chess pieces.
- Hardware Integration: Uses Arduino and Raspberry Pi for controlling the robotic movements.
- Web Application: A full-stack application for online play, built with React.js, Node.js, and GraphQL.
- Database: Secure authentication and game data storage using PostgreSQL.

# The Tech Stack
- Frontend: React.js
- Backend: Node.js, GraphQL
- Database: PostgreSQL
- Computer Vision: OpenCV (Python)
- Hardware: Arduino, Raspberry Pi

# Setup Instructions

**Hardware Setup**
- Arduino and Raspberry Pi: Assemble the robotic arm and connect the sensors and actuators.
- Chessboard: Position the camera to capture the four corners of the chess board to integrate the chessboard with the hardware components.

**1. Clone the Repo**

```git clone https://github.com/yourusername/chess-robot.git```

**2. Install Dependencies**

```cd chess-robot```

```npm install```

**3.  Set up PostgreSQL**
- Install PostgreSQL and create a database.
- Update the database configuration in the backend code.

**4. Run the Backend**

```node server.js```

**5. Run the Frontend:**
```npm start```


