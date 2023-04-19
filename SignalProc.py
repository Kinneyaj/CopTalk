import pyaudio
import wave
import speech_recognition as sr
import threading
import TextAnalyzer
import GUI


class SignalProcessor():
  # Set parameters for recording
  FORMAT = pyaudio.paInt16
  CHANNELS = 2
  RATE = 44100
  CHUNK = 1024
  RECORD_SECONDS = 30
  detect_seconds = RECORD_SECONDS
  event_seconds = 120
  WAVE_OUTPUT_FILENAME = "output.wav"

  eventActive = False
  running = True
  transcript = ""

  # Create PyAudio object
  p = pyaudio.PyAudio()

  input_index = None
  info = p.get_host_api_info_by_index(0)
  num_devices = info.get('deviceCount')

  def __init__(self):

    # Find the index of the Stereo Mix input
    for i in range(self.num_devices):
      #print(p.get_device_info_by_index(i))
      if (self.p.get_device_info_by_host_api_device_index(
          0, i).get('maxInputChannels')) > 0:
        if "Stereo Mix" in self.p.get_device_info_by_host_api_device_index(
            0, i).get('name'):
          self.input_index = i
          print(i)

  def recordAudio(self):
    #print("recording audio")

    # Create stream object
    stream = self.p.open(format=self.FORMAT,
                         channels=self.CHANNELS,
                         rate=self.RATE,
                         input=True,
                         input_device_index=self.input_index,
                         frames_per_buffer=self.CHUNK)

    if self.eventActive:
      #record events in 60s clips
      self.RECORD_SECONDS = self.event_seconds
    else:
      #detect speech in 10s clips
      self.RECORD_SECONDS = self.detect_seconds

    # Record audio
    self.frames = []
    for i in range(0, int(self.RATE / self.CHUNK * self.RECORD_SECONDS)):
      try:
        self.data = stream.read(self.CHUNK)
        self.frames.append(self.data)
      except(OSError):
        self.p.terminate()

    # Stop recording
    stream.stop_stream()
    stream.close()

    self.writeAudio()

  def detectEvent(self):
    #print("detecting event")
    self.recordAudio(self, self.detect_seconds)
    self.writeAudio()
    self.convertSpeechToText()
    self.writeText()

  def writeAudio(self):
    #print("writing audio to file")

    # Save the recorded audio to a WAV file
    wf = wave.open(self.WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(self.CHANNELS)
    wf.setsampwidth(self.p.get_sample_size(self.FORMAT))
    wf.setframerate(self.RATE)
    wf.writeframes(b''.join(self.frames))
    wf.close()

  def convertSpeechToText(self):
    #print("converting speech to text")

    #Pass the file through Speech-to-Text
    r = sr.Recognizer()
    with sr.AudioFile(self.WAVE_OUTPUT_FILENAME) as source:
      r.adjust_for_ambient_noise(source)
      audio = r.record(source)

    # recognize speech using Google Speech Recognition
    try:
      self.transcript = r.recognize_google(audio, language='en-US')
      print(self.transcript)
      TextAnalyzer.rawText(self.transcript)
    except sr.UnknownValueError:
      self.transcript = ""
    except sr.RequestError as e:
      print(
        "Could not request results from Google Speech Recognition service; {0}"
        .format(e))
      self.transcript = ""
    except Exception as e:
      print("Unexpected Error")

    self.writeText()

  def writeText(self):
    #print("writing text to file")

    if self.transcript == "":
      print("no speech detected")
      if self.eventActive == True:
        #print("event complete")
        #end of event
        self.eventActive = False
        self.running = False
    else:
      st = TextAnalyzer.rawText(self.transcript)
      highlights, st = GUI.colorTostr(st)
      GUI.live_update(st)
      #write transcripts to file
      if self.eventActive == False:
        self.eventActive = True
        with open("transcript.txt", "w") as f:
          f.write(self.transcript)
      else:
        with open("transcript.txt", "a") as f:
          f.write(" " + self.transcript)

  def sdr_start(self):

    #sp = SignalProcessor()

    self.recordAudio()

    while self.running == True:

      thread1 = threading.Thread(target=self.recordAudio)
      thread2 = threading.Thread(target=self.convertSpeechToText)

      thread1.start()
      thread2.start()

      thread1.join()
      thread2.join()

    self.p.terminate()
