# FLAMES Game Web Application

A modern web implementation of the popular FLAMES game using Python Flask and a beautiful responsive UI. FLAMES is a relationship game that predicts the relationship between two people based on their names.

## What is FLAMES?

FLAMES is an acronym for:
- **F** - Friends
- **L** - Love
- **A** - Affection
- **M** - Marriage
- **E** - Enemy
- **S** - Siblings

## Features

- 🎨 Modern and responsive web interface
- 💻 Clean and intuitive user experience
- 📱 Mobile-friendly design
- ⚡ Real-time relationship calculation
- 🎯 Input validation and error handling
- 🌈 Beautiful gradient background
- 🔄 Interactive form with instant results

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS, JavaScript
- **Styling**: Custom CSS with modern design principles
- **API**: RESTful endpoint for calculations

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/flames-game.git
cd flames-game
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- On Windows:
```bash
venv\Scripts\activate
```
- On macOS/Linux:
```bash
source venv/bin/activate
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## How to Play

1. Enter two names in the input fields
2. Click the "Calculate Relationship" button
3. The result will show the predicted relationship between the two names

## Project Structure

```
flames-game/
├── app.py              # Flask application
├── requirements.txt    # Python dependencies
├── templates/         # HTML templates
│   └── index.html     # Main web interface
└── README.md         # Project documentation
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Inspired by the traditional FLAMES game
- Built with Flask web framework
- Styled with modern CSS techniques
