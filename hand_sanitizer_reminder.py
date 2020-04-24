import subprocess, time


hand_sanitizer_reminder_file = open("hand_sanitizer_reminder", "w+")
hand_sanitizer_reminder_file.write("HAVE YOU SANITIZED YOUR HANDS, BOY?")

hand_sanitizer_reminder_file.close()



time_left_on_this_earth = 100000000000000000000000000000000000000000000000000000000000000000000

while time_left_on_this_earth > 0:
    if time_left_on_this_earth % 10 == 0:
        subprocess.Popen(['open', '-t', 'hand_sanitizer_reminder']) # -t is the TextEdit application on MacOSX
    time.sleep(1)
    time_left_on_this_earth -= 1
