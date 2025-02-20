# WhatsApp Typing Status Simulator

A Node.js script to simulate the "Typing..." status in WhatsApp groups using `whatsapp-web.js`.

## Features
- Simulates typing status in multiple WhatsApp groups.
- Uses `LocalAuth` to save session data locally.
- Easy to set up and run.

## Prerequisites
- Node.js (v14 or higher)
- A WhatsApp account

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/keerthi-kumar-k-j/whatsapp-typing-status.git
2. Install dependencies:
   ```
   npm install
## Usage
1. Run the script:
   ```
   node index.js
   ```
2. Scan the QR code using your WhatsApp mobile app.

3. The script will simulate typing in the specified groups.

## Configuration
Update the group names array in index.js with your group names.To extract your WhatsApp group ids run the script:
``` 
node groupid.js
```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.

## License
This project is licensed under the MIT License. See LICENSE for details.
