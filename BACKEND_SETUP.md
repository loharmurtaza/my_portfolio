# Portfolio Backend Setup

This guide will help you set up the Python backend for your portfolio's contact form.

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Email Settings

1. Copy the email configuration template:
   ```bash
   copy email_config.env .env
   ```

2. Edit the `.env` file with your email credentials:
   ```
   EMAIL_ADDRESS=your-email@gmail.com
   EMAIL_PASSWORD=your-app-password
   RECIPIENT_EMAIL=your-email@gmail.com
   ```

### 3. Gmail Setup (Recommended)

For Gmail, you'll need to:

1. **Enable 2-Factor Authentication** on your Google account
2. **Generate an App Password**:
   - Go to Google Account settings
   - Security → 2-Step Verification → App passwords
   - Generate a password for "Mail"
   - Use this password in your `.env` file

### 4. Run the Backend Server

```bash
python app.py
```

The server will start on `http://localhost:5000`

### 5. Run the Frontend

In a separate terminal, start the frontend:

```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Testing

1. Open your portfolio website
2. Click "Hire Me" button
3. Fill out the contact form
4. Click "Send Message"
5. Check your email for the message

## API Endpoints

- `GET /api/health` - Health check
- `POST /api/contact` - Submit contact form

## Troubleshooting

### Common Issues:

1. **"Failed to send message" error**:
   - Check if the backend server is running
   - Verify email credentials in `.env` file
   - Check if Gmail app password is correct

2. **CORS errors**:
   - Make sure Flask-CORS is installed
   - Check that the frontend is making requests to the correct backend URL

3. **Email not received**:
   - Check spam folder
   - Verify the recipient email address
   - Check Gmail security settings

## Alternative Email Providers

You can use other email providers by updating the SMTP settings in `.env`:

### Outlook/Hotmail:
```
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
```

### Yahoo:
```
SMTP_SERVER=smtp.mail.yahoo.com
SMTP_PORT=587
```

## Security Notes

- Never commit your `.env` file to version control
- Use app passwords instead of your main email password
- Consider using environment variables in production
