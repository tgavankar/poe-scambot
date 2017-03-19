import threading
import winsound

class BeepThread(threading.Thread):
    """Thread that handles audio notifications."""
    
    def __init__(self, spawner):
        """Initializes the thread with a reference to the creator thread."""
        threading.Thread.__init__(self)
        self.spawner = spawner
        self.start()
        
    def run(self):
        """Main action of the thread. Plays a tone."""
        winsound.Beep(440, 1000)
    
    def kill(self):
        """Thread dies in 1 second anyways."""
        pass