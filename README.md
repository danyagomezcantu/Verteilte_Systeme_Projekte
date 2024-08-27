# Verteilte Systeme: Task Scheduler Project

## Project Overview

This project explores the development and implementation of a task scheduler designed for distributed systems. The primary goal is to implement and compare various task scheduling algorithms, utilizing Python and Docker to simulate a distributed environment where tasks are managed and executed across multiple clients.

## Goals and Objectives

The project was initiated with the following goals:
- **Implement Various Scheduling Algorithms:** We aimed to implement several scheduling strategies, including:
  - First-Come, First-Served (FCFS)
  - Shortest Job Next (SJN)
  - Priority Scheduling
  - Round Robin
  - Shortest Remaining Time (SRT)
  - Multiple-Level Queues Scheduling
- **Simulate a Distributed Environment:** Use Docker containers to simulate multiple clients that execute tasks based on the implemented scheduling algorithms.
- **Compare Performance:** Evaluate the effectiveness of the scheduling algorithms using metrics like turnaround time, waiting time, and CPU utilization.

## What Has Been Implemented

### Implemented Features:
- **First-Come, First-Served (FCFS) Scheduling:** The FCFS scheduling algorithm has been successfully implemented. It provides a simple, non-preemptive approach where tasks are executed in the order they arrive.
- **Dockerized Environment:** The project includes a Docker setup where each client runs in its own container, simulating a distributed system.
- **RESTful API:** A basic REST API has been developed using Flask, enabling task distribution and status monitoring across the clients.

### What Is Missing:
- **Advanced Scheduling Algorithms:** Other scheduling algorithms, such as SJN, Priority Scheduling, and Round Robin, were planned but have not yet been implemented.
- **Comprehensive Error Handling:** The system lacks robust error handling mechanisms, particularly in the API and client communication.
- **Performance Evaluation:** While the infrastructure for testing and evaluation exists, extensive performance benchmarking has not yet been completed.

## System Requirements

- **Python 3.8+**
- **Docker**
- **Docker Compose**

## Basic Instructions

- **To run the project:**
  1. Ensure Docker and Docker Compose are installed on your system.
  2. Build and run the Docker containers using Docker Compose.
  3. Access the RESTful API at `http://localhost:5000` to interact with the task scheduler.

## Challenges and Learning

During the development, several challenges were encountered:
- **Docker Setup:** Initial difficulties were faced in setting up and managing Docker containers effectively.
- **Scheduling Complexity:** Adapting theoretical scheduling algorithms to practical implementation was more complex than anticipated.

## Future Work

The project is a work in progress with several areas identified for future improvement:
- **Implement Remaining Scheduling Algorithms:** Completing the implementation of SJN, Priority Scheduling, Round Robin, etc.
- **Enhance Error Handling:** Introduce comprehensive error handling across all components of the system.
- **Performance Testing:** Conduct thorough testing and benchmarking to evaluate the performance of different scheduling strategies.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or additions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- Danya Gómez - [danya_carolina.gomez_cantu@smail.th-koeln.de](mailto:danya_carolina.gomez_cantu@smail.th-koeln.de)
- Sven Heiter - [sven.heiter@smail.th-koeln.de](mailto:sven.heiter@smail.th-koeln.de)
