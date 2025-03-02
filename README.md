A.  Grazioso Salvare Dashboard – Project Two
Overview
This project is a web-based dashboard built using Dash and MongoDB, designed to help Grazioso Salvare analyze rescue animal data from the Austin Animal Center. The dashboard integrates interactive data tables, visualizations, and geolocation mapping, allowing users to explore and filter animal outcome data effectively.

Project Structure
-  CRUD Module: A Python module for database interactions, including Create, Read, Update, and Delete operations in MongoDB.
-  Dash Web App: The frontend interface for interactive data visualization.
-  MongoDB Database: Stores animal rescue data, accessed through the CRUD module.

  
B.  Reflection on Project Two and Computer Science Principles
1. Code Maintainability, Readability, and Adaptability
One of the key aspects of this project was ensuring that the code is modular, reusable, and easy to maintain. The CRUD module from Project One was designed with clear function definitions, making it easy to integrate with the dashboard in Project Two.

Advantages of this approach:

-  The CRUD module can be reused in other applications without modification.
-  Debugging and updates are simpler because the database logic is separated from the frontend.
-  The scalability of the dashboard increases, as the backend remains flexible for future changes.
-  In future projects, I can reuse this CRUD module for different datasets, simply modifying query parameters.

2. Approach to Problem-Solving as a Computer Scientist
I approached this project using a structured problem-solving mindset:

-  Understanding the Requirements: The first step was analyzing Grazioso Salvare’s needs, identifying key database queries and UI features.
-  Database Design: Ensuring efficient queries for performance, using indexing and optimizing find() operations in MongoDB.
-  Frontend and Backend Integration: Building a clean API between the CRUD module and the Dash application.
-  Compared to previous coursework, this project required a real-world software engineering mindset, integrating databases, APIs, and user interfaces. This experience improved my ability to design scalable applications that meet business needs.

3. The Role of Computer Scientists and Its Importance
Computer scientists play a critical role in developing intelligent, data-driven solutions. This project demonstrates how software can be used in animal rescue operations, enabling Grazioso Salvare to:

-  Identify trends in animal outcomes.
-  Locate high-risk areas needing intervention.
-  Optimize rescue and adoption strategies.
-  This experience reinforced the importance of data management, analytics, and user-friendly design in making impactful decisions.
