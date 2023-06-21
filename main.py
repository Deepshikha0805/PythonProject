from plyer import notification
import time

def timer(reminder, seconds):
    notification.notify(
        title="Reminder",
        message=f"Alarm will go off in {seconds} seconds.",
        timeout=20
    )
    time.sleep(seconds)
    notification.notify(
        title="Reminder",
        message=reminder,
        timeout=20
    )

    # Play beep sound
    import winsound
    winsound.Beep(2500, 1000)

if __name__ == '__main__':
    words = input("What would you like to be reminded of: ")
    sec = int(input("Enter the number of seconds: "))
    timer(words, sec)
