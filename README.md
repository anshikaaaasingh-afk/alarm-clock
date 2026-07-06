# ⏰ Python Alarm Clock

A simple, lightweight desktop alarm clock built with Python. Set an alarm time, and the app will alert you with a sound when it goes off — complete with snooze and stop controls.

## Features

- 🕒 Set an alarm for any time of day
- 🔔 Plays a sound when the alarm triggers
- 😴 Snooze functionality
- 🖥️ Simple, clean GUI (Tkinter)
- 🔁 Runs in the background while you work

## Demo

<!-- Add a screenshot or GIF of the app here -->
```
[Screenshot / GIF placeholder]
```

## Tech Stack

- **Python 3.x**
- **Tkinter** — GUI
- **playsound / pygame** — audio playback
- **datetime / time** — alarm scheduling

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/anshikaaaasingh-afk/alarm-clock.git
   cd alarm-clock
   ```

2. Install dependencies
   ```bash
   pip3 install -r requirements.txt
   ```

3. Run the app
   ```bash
   python3 alarm_clock.py
   ```

## Usage

1. Launch the app.
2. Enter the desired alarm time in `HH:MM:SS` (24-hour) format.
3. Click **Set Alarm**.
4. When the time hits, an alert sound will play.
5. Click **Snooze** to delay by a few minutes, or **Stop** to dismiss.

## Project Structure

```
alarm-clock/
├── alarm_clock.py       # Main application logic
├── assets/
│   └── alarm_sound.mp3  # Alarm sound file
├── requirements.txt
└── README.md
```

## Future Improvements

- [ ] Multiple simultaneous alarms
- [ ] Custom alarm sounds (user upload)
- [ ] Day-of-week repeat scheduling
- [ ] System tray/background mode
- [ ] Cross-platform notification support

## License

This project is licensed under the MIT License.

## Author

**Anshika Singh**
GitHub: [@anshikaaaasingh-afk](https://github.com/anshikaaaasingh-afk)
