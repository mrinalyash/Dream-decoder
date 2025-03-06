# Dream Decoder

Dream Decoder is an AI-powered tool that interprets dreams using Mistral AI. Simply input a dream description, and the model provides an insightful analysis based on symbolic meanings and psychological interpretations.

## Features
- 🔮 **AI-Powered Dream Interpretation**: Uses Mistral AI to analyze and interpret dreams.
- 🧠 **Context-Aware Analysis**: Provides responses based on dream symbols and psychological meanings.
- 🌐 **API-Based Processing**: Uses the Mistral AI API for generating interpretations.
- 📜 **Simple & Interactive CLI**: Run the script to get immediate dream interpretations.

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- `pip` (Python package manager)
- `requests` and `python-dotenv` libraries

### Steps
1. **Clone the repository**:
   ```sh
   git clone https://github.com/mrinalyash/Dream-decoder.git
   cd Dream-decoder
   ```
2. **Create a virtual environment (optional but recommended)**:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```sh
   pip install -r requirements.txt
   ```
4. **Set up API key**:
   - Create a `.env` file in the project root.
   - Add your Mistral API key:
     ```sh
     MISTRAL_API_KEY=your_api_key_here
     ```

## Usage
To run the Dream Decoder:
```sh
python main.py
```
You'll be prompted to enter a dream description, and the AI will generate an interpretation.

## API Access Requirements
Dream Decoder uses the **Mistral AI API** for dream interpretation. Ensure you have:
- A valid **Mistral AI API key**
- Access to **chat/completions** endpoint

## Troubleshooting
❌ **MISTRAL_API_KEY is not set**:
   - Ensure you have a `.env` file with the correct API key.

❌ **Unauthorized (401 Error)**:
   - Check if the API key is correct and active.

❌ **Other API errors**:
   - Verify your API access level in Mistral AI's developer portal.
   - Check your internet connection.

## Contributing
Pull requests are welcome! Feel free to contribute by improving responses, optimizing code, or adding new features.

## License
This project is open-source and available under the **MIT License**.

---
✉️ **Have feedback or suggestions?** Open an issue or reach out!

