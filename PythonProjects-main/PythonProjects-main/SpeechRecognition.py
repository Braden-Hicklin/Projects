from datetime import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import wolframalpha

# speech engine initialization
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # 0 = male, 1 = female
activationWord = 'tupper'

# configure browser
# set the path
opera_path = r"J:\Opera\launcher.exe"
webbrowser.register('opera', None, webbrowser.BackgroundBrowser(opera_path))

appId = 'H6RU57-JVXVTH98GK'
wolframClient = wolframalpha.Client(appId)

def speak(text, rate = 120): 
    engine.setProperty('rate', rate) # how fast the AI is talking
    engine.say(text) # responding
    engine.runAndWait() # timeout between message

def parseCommand(): # interpreting what is coming through the mic
    listener = sr.Recognizer()
    print('Listening for a command')

    with sr.Microphone() as source:
        listener.pause_threshold = 2    # how long you can pause while talking
        input_speech = listener.listen(source)

    try:
        print('Recognizing speech... ')
        query = listener.recognize_google(input_speech, language='en_gb') 
        print(f'The input speech was: {query}')
    except Exception as exception:
        print('I did not quite catch that')
        speak('I did not quite catch that')
        print(exception)
        return 'None'
    
    return query

def search_wikipedia(query = ''): # search wikipedia
    searchResults = wikipedia.search(query) # search wikipedia for results
    if not searchResults: # if no results
        print('No wikipedia result')
        return 'No result received'
    try: # if results found
        wikiPage = wikipedia.page(searchResults[0]) # pick top result
    except wikipedia.DisambiguationError as error: # if there is a disambiguation error
        wikiPage = wikipedia.page(error.options[0])
    print(wikiPage.title)
    wikiSummary = str(wikiPage.summary)
    return wikiSummary

def listOrDict(var):
    if isinstance(var, list):
        return var[0]['plaintext']
    else:
        return var['plaintext']

def search_wolframalpha(query = ''):
    response = wolframClient.query(query)

    # @success: Wolfram Alpha was able to resolve the query
    # @numpods: Number of results returned
    # pod: List of results. This can also contain subpods

    if response['@success'] == 'false':
        return 'Could not compute'
    
    else:
        result = ''
        # question
        pod0 = response['pod'][0]
        pod1 = response['pod'][1]
        # may contain the answer, has the highest confidence value
        # if it's primary, or has the title of result or definition, then it's the official result
        if (('result') in pod1['@title'].lower()) or (pod1.get('@primary', 'false') == 'true') or ('definition' in pod1['@title'].lower()):
            # get result
            result = listOrDict(pod1['subpod'])
            # remove the bracketed section
            return result.split('(')[0]
        else:
            question = listOrDict(pod0['subpod'])
            # remove the bracketed section
            return question.split('(')[0]
            # search wikipedia instead
            speak('Computation failed, checking wikipedia instead')
            return search_wikipedia(question)

# main loop
if __name__ == '__main__':
    speak('Hello Braden.')

    while True:
        # parse as a list
        query = parseCommand().lower().split()

        if query[0] == activationWord or query[0] == 'copper' or query[0] == 'helper' or query[0] == 'topper':
            query.pop(0)

            # list commands
            if query[0] == 'say':
                if 'hello' in query:
                    speak('Greetings, all.')
                else:
                    query.pop(0) # remove say
                    speech = ' '.join(query)
                    speak(speech)

            # navigation
            if query[0] == 'go' and query[1] == 'to':
                speak('Opening...')
                query = ' '.join(query[2:])
                webbrowser.get('opera').open_new(query)

            # wikipedia
            if query[0] == 'explain':
                query = ' '.join(query[1:])
                speak('Querying the universal encyclopedia')
                speak(search_wikipedia(query))

            # math
            if query[0] == 'compute' or query[0] == 'computer':
                query = ' '.join(query[1:])
                speak('Computing')
                try:
                    result = search_wolframalpha(query)
                    speak(result)
                except:
                    speak('Unable to compute')

            # record some notes for me
            if query[0] == 'log': 
                speak('Ready to record some notes')
                newNote = parseCommand().lower()
                now = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

                with open('note_%s.txt' % now, 'w') as newFile:
                    newFile.write(newNote)
                speak('Note written')

            # respect
            if query[0] == 'thank' and query[1] == 'you':
                speak('You are welcome')
            
            # birthday
            if query[0] == 'how' and query[1] == 'old' and query[2] == 'are' and query[3] == 'you':
                result = search_wolframalpha('how long has it been since may eighteenth twenty twenty-three')
                speak(result)

            # rest
            if query[0] == 'exit':
                 speak('Goodbye Braden')
                 break
