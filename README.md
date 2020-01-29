# Image_Recognition_PiCamera_Google_AIY_Voice_Kit
## What is it'?'

This project is for Python3 programs of the image recognition, using the various Google APIs, for Raspberry Pi equipped with a Google AIY Voice Kit V1 and a Pi Camera module. 
Push the button of the Google AIY Voice kit and speak the command you want to recognize (objects, logos or texts), then Pi camera take a photo and the programs return the results of image recognition of the photo with the artificial voice, translated into the language you specified.
Currently Japanese, Spanish and English are adapted to, although other languages can be utilized by adding the phrases in "[word.py](https://github.com/kureuetan/Image_Recognition_PiCamera_Google_AIY_Voice_Kit/blob/master/words.py)".

Originally this project is inspired by the [Liz Myers' work](https://www.hackster.io/elizmyers/add-vision-to-the-aiy-voice-kit-e9ff3d). 
This project is more focus on non-English speakers (currently Japanese and Spanish) by making use of Google Translate API.
Concretely speaking, the process is as follows:

 1. When you push the button of Google AIY voice kit, the Pi Camera takes a picture and save it. 
 2. Say a command to the AIY speaker to specify the type of the analysis you make (object recognition, logo recognition or text recognition). Google SpeechToText API capture it and convert the sounds into texts.
 3. Send the image file to Google Cloud Vision API to analyze, which return the result of
    recognized objects by texts. 
 4. Translated into the language you defined by Google translate API and make them speak by artificial voice created by Google TextToSpeech API.

### Example videos

 - English version
<iframe width="560" height="315" src="https://youtube.com/embed/4hDf8eTBnf8?rel=0&autoplay=0" frameborder="0" allowfullscreen></iframe>
 
 - Japanese version
<iframe width="560" height="315" src="https://youtube.com/embed/WwGZajUqfpk?rel=0&autoplay=0" frameborder="0" allowfullscreen></iframe>

You can also find the detailed process explained on my web site.
->  [Website link (only in Japanese)](https://kureuetan.com/web/raspberrypi/7430/)
 
## Getting Started

### Prerequisites

#### 1. AIY Voice Kit (V1)
 In order to make this program work, Raspberry Pi 3+ should be equipped with [AIY Voice Kit(V1)](https://aiyprojects.withgoogle.com/voice-v1/) and [AIY Kits OS](https://github.com/google/aiyprojects-raspbian/releases).
Please make sure if the following demo program works.

```
cd /home/pi/AIY-projects-python/src/examples
./voice/assistant_grpc_demo.py
```
#### 2. Pi Camera Module
Raspberry Pi 3+ should be equipped with Pi Camera Module.
Please make sure if the camera works successfully.
```
raspistill -rot 180 -o /home/pi/Pictures/testimg.jpg -w 640 -h 480
```
If a picture image is stored in the directory above, the camera succeeds to work.

### Camera preview settings
Before running the program, the Pi Camera should show preview images by writing the following commands.
```
raspistill -o /home/pi/aiyimage.jpg -s -t 0 -rot 180 -w 640 -h 480 --preview 500,90,640,480
```
This function can be set by the crontab, in order to show camera previews automatically each time Raspberry Pi starts.
```
crontab -e
```
The following text will be added in the end of the crontab texts.
```
@reboot raspistill -o /home/pi/aiyimage.jpg -s -t 0 -rot 180 -w 640 -h 480 --preview 500,90,640,480
```
The directory that saves the image can be changed anytime by editing the command above and the line 57 in "[visionRecog.py](https://github.com/kureuetan/Image_Recognition_PiCamera_Google_AIY_Voice_Kit/blob/master/visionRecog.py)"

### Enable the Google APIs

 To make programs works, some Google APIs needs to be activated. 
 - Make your project on your [Google Cloud Platform](https://console.cloud.google.com/)
 - Download json file like as you did when you make assistant.json in Google AIY demo program
 - Enable the following Google APIs
	 - [Cloud Text-to-Speech API](https://cloud.google.com/text-to-speech/docs/quickstart-client-libraries?#client-libraries-install-python)
	 - [Cloud Speech-to-Text API](https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries)
	 - [Cloud Vision API](https://cloud.google.com/vision/docs/libraries)
	 - [Cloud Translation API](https://cloud.google.com/translate/docs/basic/setup-basic)

[Warning]
Some Google APIs, especially "Cloud Speech to Text API", may charge you if your usage exceeds the free limit of each month. Make sure if you activate the 12-month, $300 free trial in the Google Cloud Platform.

## Installing
  
### Google APIs in the Raspberry Pi.
```
AIY-projects-shell.sh
pip3 install --upgrade google-cloud-texttospeech google-cloud-speech google-cloud-vision 
pip3 install google-cloud-translate==2.0.0
```
### Reproduction of sounds
As the reproduction of sounds, aplay for wav files and mpg321 for mp3 files are needed.
These two application will already be installed in most cases. If not, please install them.
```
aplay --version
mpg321 --version
```
If you input above and show the version of each, these are already installed.

### Reading a Google credentials
Before running programs, the Google credential information (json) needs to be loaded as follows.
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/your_credential_name.json"
```
You can preload it so that you don't have to input it each time.
```
nano ~/.profile
```
Edit '.profile' and add the following text in the end of it.
```
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/your_credential_name.json"
```

## Running the programs

### Clone the project from GitHub
Clone the files from this GitHub page.
```
cd /home/pi/
git clone https://github.com/kureuetan/Image_Recognition_PiCamera_Google_AIY_Voice_Kit.git
```
### Prepare
Copy the downloaded files to the directory you want to place
```
cp /home/pi/Image_Recognition_PiCamera_Google_AIY_Voice_Kit /home/pi/AIY-projects-python/src/examples/imageRecognition -r
```

**[if necessary]** Load the credential and set the camera preview, only in case you have **not** preset in the previous process.
```
raspistill -o /home/pi/aiyimage.jpg -s -t 0 -rot 180 -w 640 -h 480 --preview 500,90,640,480
export GOOGLE_APPLICATION_CREDENTIALS="/home/pi/your_credential_name.json"
```

#### Change language setting
The default setting is Japanese. If you want to change another language (English or Spanish), you edit the lines 28-35 of [vision_recog_with_button.py](https://github.com/kureuetan/Image_Recognition_PiCamera_Google_AIY_Voice_Kit/blob/master/vision_recog_with_button.py), by adding or deleting '#' of each line. 
For example, if you change them to as bellow, English version will be initiated.
```
# if you use the English version
vision_recog = VisionRecog()

# if you use the Spanish version
#vision_recog = VisionRecog('es','es-ES')

# if you use the Japanese version
#vision_recog = VisionRecog('ja','ja-JP')
```

### And RUN!
Run the program
```
cd /home/pi/AIY-projects-python/src/examples/imageRecognition
./vision_recog_with_button.py
```
When you run the program, you hear the voice saying 'Push the button and say commands. "What is this?", "Can you read this?" or "What logo is this?"' in your language set, while the list of the effective commands will be shown in the terminal screen.

![](https://kureuetan.com/wp-content/uploads/button1-800x315.png)

Then if you push the AIY kit button...

![](https://kureuetan.com/wp-content/uploads/button2-1.png)

When you see the phrase "Start listening" in the terminal screen, the voice recognition starts. You can talk to the speaker, using preset commands like "What is this?" Then the program will respond the results by artificial voice in the language you set.
