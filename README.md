# clg_bot
# College Chatbot using Rasa

This project is a conversational AI chatbot developed using Rasa to assist students, faculty, and visitors with information related to Nagarjuna College. The chatbot can respond to frequently asked questions, provide course and admission details, event information, and other campus-related queries.

## Features

- General information about the college and its departments
- Details about academic courses and specializations
- Admission process and important dates
- Contact details and office hours
- Event schedules and announcements
- Built with Rasa for natural language understanding and dialogue management
- Custom actions for dynamic responses

## Technology Stack

- Rasa (NLU and Core)
- Python 3.8+
- Custom Actions (Python-based)
- Rasa X (Optional for interactive learning and monitoring)

## Project Structure

college-chatbot/
├── data/
│ ├── nlu.yml
│ ├── rules.yml
│ └── stories.yml
├── domain.yml
├── actions/
│ └── actions.py
├── config.yml
├── credentials.yml
├── endpoints.yml
├── tests/
└── README.md

markdown
Copy
Edit

## Installation and Setup

1. Clone the repository:
git clone https://github.com/yourusername/college-chatbot.git
cd college-chatbot

cpp
Copy
Edit

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate # For Windows: venv\Scripts\activate

markdown
Copy
Edit

3. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit

4. Train the Rasa model:
rasa train

markdown
Copy
Edit

5. Run the chatbot:
rasa run actions &
rasa shell

python
Copy
Edit

## Example Intents

- `greet`: "Hello", "Hi"
- `ask_courses`: "What courses are available?"
- `ask_admissions`: "How can I apply?"
- `ask_fees`: "What is the fee structure?"
- `goodbye`: "Bye", "Thanks"

## Custom Actions

Custom actions are defined in the `actions/actions.py` file. These are used for responses that require logic, such as displaying a list of courses or dates.

Example:

```python
class ActionShowCourses(Action):
 def name(self):
     return "action_show_courses"

 def run(self, dispatcher, tracker, domain):
     courses = ["B.Tech", "MBA", "MCA"]
     dispatcher.utter_message(text="We offer the following courses: " + ", ".join(courses))
     return []
Testing
To run tests:

bash
Copy
Edit
rasa test
To test conversations:

bash
Copy
Edit
rasa test conversations
Deployment
This chatbot can be deployed using:

Rasa X for interactive learning

Docker containers

Messaging channels like Telegram, WhatsApp, or integrated into a website using a webchat widget

Developed By
Anirudh
Nagarjuna College
Academic Year: 2022 - 2026

License
MIT License

Copyright (c) 2025 Anirudh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
