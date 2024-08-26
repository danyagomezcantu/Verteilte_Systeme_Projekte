# Task Scheduler for Distributed Systems

## Project Overview

This project involves the development and implementation of a task scheduler designed for distributed systems. The project explores various scheduling algorithms, evaluates their effectiveness, and addresses the challenges encountered during implementation. The scheduler was developed using Python, and Docker containers were utilized to simulate clients in a distributed environment. This setup allows for a flexible and scalable system that can manage tasks across multiple nodes.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Scheduling Algorithms](#scheduling-algorithms)
6. [System Architecture](#system-architecture)
7. [Testing](#testing)
8. [Results and Discussion](#results-and-discussion)
9. [Contributing](#contributing)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)

## Features

- **Multiple Scheduling Algorithms:** Implementation of various scheduling algorithms, including Round Robin, First-Come, First-Served (FCFS), Priority Scheduling, and Shortest Job Next (SJN).
- **Distributed Environment Simulation:** Simulation of a distributed environment using Docker containers, facilitating the testing of task scheduling across multiple nodes.
- **Scalable Architecture:** A flexible system architecture that allows for easy scalability, supporting the addition of more nodes as needed.
- **Comprehensive Testing Suite:** A testing suite to evaluate the performance of different scheduling algorithms under various conditions.

## Installation

### Prerequisites

- Python 3.11.0
- Docker
- Git

### Steps

1. **Clone the repository:**

   ```bash
   git clone https://github.com/danyagomezcantu/Verteilte_Systeme_Projekte.git
   cd Verteilte_Systeme_Projekte
   ```

2. **Set up the virtual environment:**

   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. **Install the required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Build Docker containers:**

   ```bash
   docker-compose up --build
   ```

## Usage

### Running the Scheduler

1. **Start the system:**

   ```bash
   python main.py
   ```

2. **Configure scheduling algorithm:**

   The scheduler supports multiple algorithms. To choose an algorithm, modify the `config.py` file:

   ```python
   SCHEDULING_ALGORITHM = 'RoundRobin'  # Options: 'RoundRobin', 'FCFS', 'Priority', 'SJN'
   ```

3. **Monitor the system:**

   The logs and outputs will be displayed in the terminal and also saved to the `logs/` directory.

## Scheduling Algorithms

- **Round Robin:** Cycles through tasks in a fixed order, distributing them evenly across available nodes.
- **First-Come, First-Served (FCFS):** Tasks are handled in the order they arrive.
- **Priority Scheduling:** Tasks are assigned based on predefined priorities.
- **Shortest Job Next (SJN):** Tasks with the shortest execution time are scheduled first.

## System Architecture

The system architecture consists of a master node responsible for task distribution and several worker nodes that execute the tasks. Docker containers were used to simulate these nodes, allowing for easy scalability and isolation of the different components.

- **Master Node:** Manages task distribution and algorithm selection.
- **Worker Nodes:** Execute the tasks based on the selected scheduling algorithm.

## Testing

The system includes a comprehensive testing suite that simulates various load conditions to evaluate the performance of different scheduling algorithms. To run the tests:

```bash
python -m unittest discover tests/
```

## Results and Discussion

Our testing revealed that the Round Robin and Priority Scheduling algorithms provided the most balanced performance in terms of task distribution and resource utilization. FCFS was simple to implement but often led to inefficiencies under heavy loads. SJN, while optimal in theory, was challenging to implement in a dynamic environment where task execution times were not known in advance.

## Contributing

We welcome contributions! Please fork the repository, create a new branch, and submit a pull request. Ensure that your code adheres to our coding standards and includes appropriate tests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to our advisors and peers who provided invaluable feedback during the project.
- The research and development of this project were supported by the distributed systems community and various open-source tools.
