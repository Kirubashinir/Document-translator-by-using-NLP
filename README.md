# NLP Document Translator & Text-to-Speech Application

A comprehensive web application that uses Natural Language Processing (NLP) to extract text from documents, detect languages, translate content, and convert text to speech.

## Features

### 🔍 **Document Processing**
- **Multi-format Support**: PDF, DOCX, TXT, XLSX, PPTX
- **Advanced Text Extraction**: Handles complex documents with tables and formatting
- **Smart Encoding Detection**: Automatically detects file encoding for text files

### 🌍 **Language Processing**
- **Automatic Language Detection**: Uses advanced NLP to detect source language
- **35+ Language Support**: Translate between major world languages
- **Confidence Scoring**: Shows detection confidence levels
- **Chunked Translation**: Handles large documents by splitting into manageable chunks

### 🎵 **Text-to-Speech**
- **High-Quality TTS**: Google Text-to-Speech integration
- **Multiple Languages**: Generate speech in target language
- **Audio Controls**: Built-in player with progress tracking
- **Download Options**: Save audio files locally

### 💻 **Modern Web Interface**
- **Responsive Design**: Works on desktop, tablet, and mobile
- **Drag & Drop Upload**: Easy file uploading
- **Real-time Progress**: Visual feedback for all operations
- **Toast Notifications**: User-friendly error and success messages

## Supported Languages

English, Spanish, French, German, Italian, Portuguese, Russian, Japanese, Korean, Chinese, Arabic, Hindi, Tamil, Telugu, Bengali, Urdu, Thai, Vietnamese, Dutch, Swedish, Danish, Norwegian, Finnish, Polish, Czech, Hungarian, Romanian, Bulgarian, Croatian, Slovak, Slovenian, Estonian, Latvian, Lithuanian, Maltese, Irish, Welsh

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Internet connection (for translation and TTS services)

### Quick Start

1. **Download/Clone the project**
   ```bash
   # If you have git
   git clone <repository-url>
   cd nlp-translator
   ```

2. **Run the application**
   - **Windows**: Double-click `run_app.bat`
   - **Manual**: Run `python app.py`

3. **Open your browser**
   - Navigate to `http://localhost:5000`

### Manual Installation

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run tests**
   ```bash
   python simple_test.py
   ```

3. **Start the application**
   ```bash
   python app.py
   ```

## Usage Guide

### 1. Upload Document
- Click the upload area or drag & drop your file
- Supported formats: PDF, DOCX, TXT, XLSX, PPTX
- Maximum file size: 16MB

### 2. Review Analysis
- View detected language and confidence score
- Check word and character counts
- Preview extracted text

### 3. Translate
- Select target language from dropdown
- Click "Translate" button
- Review translated text

### 4. Generate Speech
- Click "Generate Speech" after translation
- Use audio controls to play/pause
- Download audio file if needed

### 5. Download Results
- Download translated text as TXT file
- Download generated audio as MP3 file

## File Structure

```
nlp-translator/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── run_app.bat           # Windows startup script
├── debug_app.bat         # Debug mode script
├── simple_test.py        # Quick functionality test
├── README.md             # This file
├── templates/
│   └── index.html        # Main web interface
├── static/
│   ├── css/
│   │   └── style.css     # Application styles
│   └── js/
│       └── app.js        # Frontend JavaScript
├── uploads/              # Temporary file storage
└── audio/                # Generated audio files
```

## API Endpoints

### File Upload
- **POST** `/api/upload`
- Upload and extract text from documents

### Translation
- **POST** `/api/translate`
- Translate text between languages

### Text-to-Speech
- **POST** `/api/tts`
- Generate speech from text

### Language List
- **GET** `/api/languages`
- Get supported languages

### File Downloads
- **POST** `/api/download/text`
- Download translated text
- **GET** `/api/audio/<filename>`
- Serve audio files

## Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Run the test script
   python simple_test.py
   
   # Install missing dependencies
   pip install -r requirements.txt
   ```

2. **Translation Errors**
   - Check internet connection
   - Verify language codes are supported
   - Try with smaller text chunks

3. **File Upload Issues**
   - Ensure file format is supported
   - Check file size (max 16MB)
   - Verify file is not corrupted

4. **Audio Generation Problems**
   - Check internet connection
   - Verify target language supports TTS
   - Try with shorter text

### Debug Mode
Run `debug_app.bat` for detailed error information and component testing.

### Log Files
Check console output for detailed error messages and debugging information.

## Technical Details

### Backend Technologies
- **Flask**: Web framework
- **deep-translator**: Translation service
- **langdetect**: Language detection
- **gTTS**: Google Text-to-Speech
- **python-docx**: Word document processing
- **pdfminer.six**: PDF text extraction
- **openpyxl**: Excel file processing
- **python-pptx**: PowerPoint processing

### Frontend Technologies
- **HTML5**: Modern web standards
- **CSS3**: Responsive design with Flexbox/Grid
- **JavaScript ES6+**: Modern JavaScript features
- **Font Awesome**: Icons
- **Google Fonts**: Typography

### NLP Features
- **Language Detection**: Statistical analysis of text patterns
- **Text Preprocessing**: Cleaning and normalization
- **Chunked Processing**: Handling large documents
- **Confidence Scoring**: Reliability metrics

## Performance Considerations

- **File Size**: Larger files take longer to process
- **Translation Speed**: Depends on text length and internet speed
- **Memory Usage**: Large documents may require more RAM
- **Concurrent Users**: Single-threaded Flask development server

## Security Notes

- Files are temporarily stored and automatically cleaned up
- No persistent storage of user data
- All processing happens locally except translation/TTS API calls
- Use HTTPS in production environments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source. Please check the license file for details.

## Support

For issues and questions:
1. Check this README
2. Run `simple_test.py` for diagnostics
3. Use `debug_app.bat` for detailed troubleshooting
4. Check console logs for error messages

## Version History

- **v1.0**: Initial release with basic functionality
- **v1.1**: Added multi-format document support
- **v1.2**: Enhanced UI and error handling
- **v1.3**: Added batch processing and improved performance